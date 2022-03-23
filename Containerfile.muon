ARG  FEDORA_VERSION=latest
FROM fedora-gpio-python:${FEDORA_VERSION}

COPY . /opt/app-root/src

CMD /bin/bash -c 'python3 -u /opt/app-root/src/blink.py'