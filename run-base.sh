#!/bin/sh
FEDORA_VERSION=35
sudo podman run -it --rm --name gpiobase --device=/dev/gpiochip4 --device=/dev/i2c-4 --volume $(pwd):/tmp/src:z localhost/fedora-gpio-python:${FEDORA_VERSION}