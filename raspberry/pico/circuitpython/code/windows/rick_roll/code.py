import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import time

# Initialize Keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# press the "windows" + R
kbd.press(Keycode.GUI, Keycode.R)
time.sleep(0.09)
kbd.release(Keycode.GUI, Keycode.R)
time.sleep(0.16)

# https://youtu.be/dQw4w9WgXcQ
layout.write('https://youtu.be/dQw4w9WgXcQ\n')

time.sleep(3.00)

# press the "windows" + R
kbd.press(Keycode.F)
time.sleep(0.09)
kbd.release(Keycode.F)
time.sleep(0.16)
