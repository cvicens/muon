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

chip=gpiod.Chip(LED_CHIP)

lines = chip.get_lines([ LED_LINE_OFFSET ])
lines.request(consumer='blink', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 0 ])

try:
    while True:
        lines.set_values([ 1 ])
        time.sleep(1)
        lines.set_values([ 0 ])
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutdown requested...exiting")
except Exception:
    traceback.print_exc(file=sys.stdout)
lines.set_values([ 0 ])
sys.exit(0)