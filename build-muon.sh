#!/bin/sh
FEDORA_VERSION=35
sudo podman build --build-arg FEDORA_VERSION=${FEDORA_VERSION} --tag muon:${FEDORA_VERSION} -f Containerfile.muon .