#!/bin/sh

#make file executable with chmod +x requirements.sh
apt update
apt install python3-dev python3-pip libpq-dev python3-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev python3-pip -y
pip3 install pipenv
apt install nodejs npm -y
