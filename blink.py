import gpiod
import sys
import time
import os

import drivers

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()

display.lcd_display_string("Hi Microshift!", 1)  # Write line of text to first line of display
display.lcd_display_string("Muon (C)", 4)  # Write line of text to second line of display

if "LED_CHIP" in os.environ and "LED_LINE_OFFSET" in os.environ:
    pass
else:
    print('''LED_CHIP AND LED_LINE_OFFSET CANNOT BE EMPTY!!!''')
    sys.exit()

# Get environment variables
LED_CHIP = os.getenv('LED_CHIP')
LED_LINE_OFFSET = os.getenv('LED_LINE_OFFSET')
print("LED_CHIP=" + LED_CHIP + " LED_LINE_OFFSET=" + LED_LINE_OFFSET)

try:
    LED_CHIP = os.getenv('LED_CHIP')
    LED_LINE_OFFSET = int(os.getenv('LED_LINE_OFFSET'))
except ValueError:
    print('''LED_CHIP AND LED_LINE_OFFSET SHOUD BE INTEGERS''')

chip = gpiod.chip(LED_CHIP)
led = chip.get_line(LED_LINE_OFFSET)

config = gpiod.line_request()
config.consumer = "blink"
config.request_type = gpiod.line_request.DIRECTION_OUTPUT

led.request(config)

try:
    while True:
        led.set_value(0)
        display.lcd_display_string("LED OFF             ", 2)
        time.sleep(1)
        led.set_value(1)
        display.lcd_display_string("LED ON              ", 2)
        time.sleep(1)     
except KeyboardInterrupt:
    print("Shutdown requested...exiting")
    display.lcd_clear()
    display.lcd_display_string("Bye Human!", 1)  
except Exception:
    traceback.print_exc(file=sys.stdout)
led.set_value(0)
sys.exit(0)