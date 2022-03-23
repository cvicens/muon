#!/bin/sh
FEDORA_VERSION=35
sudo podman build --build-arg FEDORA_VERSION=${FEDORA_VERSION} --tag fedora-gpio-python:${FEDORA_VERSION} -f Containerfile.base .