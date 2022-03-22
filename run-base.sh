#!/bin/sh
FEDORA_VERSION=35
sudo podman run -it --rm --name gpiobase --device=/dev/gpiochip4 localhost/fedora-gpio-python:${FEDORA_VERSION}