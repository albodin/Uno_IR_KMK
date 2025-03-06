from kmk.keys import make_consumer_key

# We'll also be using the uno keyboard definition
from uno import Uno_IR

keyboard = Uno_IR()


# We'll use the RGB LED to indicate stuff about what's going on
from kmk.extensions.rgb import RGB
import microcontroller
rgb = RGB(pixel_pin=microcontroller.pin.GPIO4, num_pixels=1)
keyboard.extensions.append(rgb)

from kmk.modules.serialace import SerialACE
keyboard.modules.append(SerialACE(rgb))

# Create the custom key that we'll be sending on click
customKey = make_consumer_key(code=589, names=('CUSTOM_LIKE', 'CLIKE'))
keyboard.keymap = [[customKey]]

# I've enabled debugging just 'cause it helps if something goes wrong, but you don't have to.
keyboard.debug_enabled = True

# This next line is how you tell it all to start, it's necessary.
if __name__ == '__main__':
    keyboard.go()
