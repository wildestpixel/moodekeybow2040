# moodekeybow2040

A Circuitpython Script (working with 6.2 and 7 beta at present) to aneable console input controlling MoodeAudio player https://github.com/moode-player.

Working in conjunction with https://github.com/antiprism/mpd_oled and incorporating a time and temperature / humidity clock UI on an Adafruit i2C SSD1306 OLED, the overall effect is relatively polished.

Of the scripts, those bashs scripts should be placed in <code>/usr/local/bin</code> and made executable via <code>sudo chmod +x</code>, and the <code>timetemp.py</code> file and <code>fonts</code> folder should stay in the Scripts folder recursively under <code>/home/pi</code>. Naturally you would need a DPS310 to run as is but can be easily modified to run with bme280 etc. etc. To install the Deja Vu font that is required, simply get from apt with <code>sudo apt-get install ttf-dejavu</code>

A service file is included in the scripts folder which should be copied into <code>/etc/systemd/system</code> to enable the toggling between <code>mpd_oled</code> and <code>timetemp.py</code>

Runnning the buttons from the main Circuitpython code.py you will note that there are 16 seperate commands linked to the buttons in an array 1 - 16 from bottom left of the Keybow2040 upwards in sequence and then from left to right - the last command occupying the top right of the Keybow2040 physically.

Pressing and holding any of the buttons (usually in practice the one linked with <code>mpc stop</code>) turns out the lights on the keybow and also disables <code>mpd_oled</code> - both to allow you a dark peaceful room and prevent OLED burn.

The <code>toggle_disp1</code> that is triggered from the top left button changes the display between <code>mpd_oled</code> and the timetemp python script, depending on what you want to see on the screen

![Alt text](IMG_1076.jpg?raw=true "Title")
