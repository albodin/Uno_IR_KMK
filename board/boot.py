import microcontroller
import digitalio
from kmk.bootcfg import bootcfg

button = digitalio.DigitalInOut(microcontroller.pin.GPIO5)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

bootcfg(
    cdc_console=True,
    cdc_data=True,
    storage=button.value
)