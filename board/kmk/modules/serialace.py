from usb_cdc import data

from kmk.modules import Module
from kmk.utils import Debug

debug = Debug(__name__)


from kmk.extensions.rgb import RGB, AnimationModes

class SerialACE(Module):
    buffer = bytearray()
    rgb = None
    
    def __init__(self, rgb: RGB):
        super().__init__()
        self.rgb = rgb

    def setColorFunc(self, h,s,v):
        self.rgb.hue = h
        self.rgb.sat = s
        self.rgb.val = v
        self.rgb.animation_mode = AnimationModes.STATIC
        self.rgb.animate()

    def during_bootup(self, keyboard):
        try:
            data.timeout = 0
        except AttributeError:
            pass

    def before_matrix_scan(self, keyboard):
        pass

    def after_matrix_scan(self, keyboard):
        pass

    def process_key(self, keyboard, key, is_pressed, int_coord):
        return key

    def before_hid_send(self, keyboard):
        # Serial.data isn't initialized.
        if not data:
            return

        # Nothing to parse.
        if data.in_waiting == 0:
            return

        
        self.buffer.extend(data.read())
        idx = self.buffer.find(b'\n')

        # No full command yet.
        if idx == -1:
            return

        # Split off command and evaluate.
        line = self.buffer[:idx]
        self.buffer = self.buffer[idx + 1 :]

        if "green" in line:
            self.setColorFunc(85,255,255)
        elif "red" in line:
            self.setColorFunc(0,255,255)
        elif "off" in line:
            self.rgb.off()


    def after_hid_send(self, keyboard):
        pass

    def on_powersave_enable(self, keyboard):
        pass

    def on_powersave_disable(self, keyboard):
        pass
