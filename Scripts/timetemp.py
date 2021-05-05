import time , datetime
import subprocess
import adafruit_dps310
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
dps310 = adafruit_dps310.DPS310(i2c)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3d)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
#font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 10)
font = ImageFont.truetype('fonts/digital-7.mono.ttf', 24)
font2 = ImageFont.truetype('fonts/digital-7.mono.ttf', 36)
font3 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 8)
font4 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)

dateString = '%A %d %B'
timeString = '%H:%M:%S'

while True:

    strDate = datetime.datetime.now().strftime(dateString)
    result  = datetime.datetime.now().strftime(timeString)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)


    # Write four lines of text.
    (font_width, font_height) = font3.getsize(strDate)
#    draw.text((x, top + 48), "Temp = %.1f" % dps310.temperature + chr(176)+"C", font=font, fill=255)
#    draw.text((x, top + 56), "Pressure = %.1f hPa  " % dps310.pressure, font=font, fill=255)
    draw.text((x, top + 48), "%.1f" % dps310.temperature, font=font, fill=255)
    draw.text((44, top + 48), chr(176)+"c" , font=font4, fill=255)
    draw.text((64, top + 48), "%.0f" % dps310.pressure, font=font, fill=255)
    draw.text((110, top + 58), "hPa" , font=font3, fill=255)
    draw.text((x, top + 10), result, font=font2, fill=255)
    draw.text((width//2 - font_width//2, top + 0), strDate, font=font3, fill=255)
    draw.text((x, top + 39), "Temperature", font=font3, fill=255)
    draw.text((64, top + 39), "Pressure", font=font3, fill=255)
    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(0.1)




