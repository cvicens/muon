#!/bin/sh
FEDORA_VERSION=35
sudo podman run -it --rm --name muon --device=/dev/gpiochip4 -e LED_CHIP=gpiochip4 -e LED_LINE_OFFSET=28 localhost/muon:${FEDORA_VERSION}