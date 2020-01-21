#!/usr/bin/env bash

DEPS="ntp python3-dev virtualenvwrapper"

if [[ "$EUID" -ne "0" ]] ; then
    echo "Script must be run as root." >&2
    exit 1
fi

apt-get install -y aptitude
aptitude update
[[ -f /.vagrant_provisioned ]] && echo "Provisioning ran already." && \
    aptitude install -y ${DEPS} && \
    exit 0


printf "#!/bin/sh\nntpdate ntp.ubuntu.com\n" > /etc/cron.daily/ntpdate
chmod 755 /etc/cron.daily/ntpdate
touch /.vagrant_provisioned
echo "Provisioning successful!"
