import gpiod
import sys
import time
import os

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

chip = gpiod.Chip(LED_CHIP)
led = chip.get_line(LED_LINE_OFFSET)

config = gpiod.line_request()
config.consumer = "Blink"
config.request_type = gpiod.line_request.DIRECTION_OUTPUT

led.request(config)

print(led.consumer)

while True:
    led.set_value(0)
    time.sleep(0.1)
    led.set_value(1)
    time.sleep(0.1)