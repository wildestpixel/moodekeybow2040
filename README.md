# moodekeybow2040

A Circuitpython Script (working with 6.2 and 7 beta at present) to aneable console input controlling MoodeAudio player https://github.com/moode-player.

Working in conjunction with https://github.com/antiprism/mpd_oled and incorporating a time and temperature / humidity clock UI on an Adafruit i2C SSD1306 OLED, the overall effect is relatively polished.

Of the scripts, those bashs scripts should be placed in /usr/local/bin and made executable via sudo chmod +x, and the timetemp.py and fonts files should stay in the Scripts folder recursively under /home/pi. Naturally you would need a DPS310 to run as is but can be easily modified to run with bme280 etc. etc.

Runnning the buttons from the main Circuitpython code.py you will note that there are 16 seperate commands linked to the buttons in an array 1 - 16 from bottom left of the Keybow2040 upwards in sequence and then from left to right - the last command occupying the top right of the Keybow2040 physically.

Pressing and holding any of the buttons (usually in practice the one linked with "mpc stop") turns out the lights on the keybow and also disables mpd_oled - both to allow you a dark peaceful room and prevent OLED burn.

The toggle_disp1 that is triggered from the top left button changes the display between mpd_oled and the timetemp python script, depending on what you want to see on the screen
