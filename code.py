import board
import math
from keybow2040 import Keybow2040, number_to_xy, hsv_to_rgb
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

i2c = board.I2C()
keybow = Keybow2040(i2c)
keys = keybow.keys
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

keymap =    ["rad1",
             "rad1",
             "mpc toggle",
             "toggle_disp1",
             "rad2",
             "rad2",
             "mpc stop",
             "volm",
             "rad3",
             "rad3",
             "mpc prev",
             "vold",
             "rad4",
             "rad4",
             "mpc next",
             "volu"]

def rainbow_on():
    global step
    step += 1
    for i in range(16):
        x, y = number_to_xy(i)
        hue = (x + y + (step / 20)) / 8
        hue = hue - int(hue)
        hue = hue - math.floor(hue)
        r, g, b = hsv_to_rgb(hue, 1, 1)
        keys[i].set_led(r, g, b)

def rainbow_off():
    for i in range(16):
        keys[i].set_led(0, 0, 0)

def countup():
    global counter
    counter = (counter + 1) % len(things)

for key in keys:
    @keybow.on_press(key)
    def press_handler(key):
        keycode = keymap[key.number]
        layout.write(keycode)
        keyboard.send(Keycode.ENTER)
        key.set_led(*rgb)

    @keybow.on_hold(key)
    def hold_handler(key):
        countup()
        print(counter)
        print(things[counter])
        layout.write("scrntg")
        keyboard.send(Keycode.ENTER)

rgb = (255, 255, 255)
step = 0
counter = 0
things = [ rainbow_on, rainbow_off ]

while True:
    keybow.update()
    things[counter]()
