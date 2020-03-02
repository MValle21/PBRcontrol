#!/bin/bash

echo "Execute in /home/bioarineo as sudoer and in tmux only!!!"
read -n 1 -s

apt update

echo "Setting up MySQL database..."

apt -y install default-mysql-server
service mysql start

mysql < "database-setup.sql"

echo "Setting up Python environment..."

apt -y install python3-pip

pip3 install importlib
pip3 install numpy
pip3 install mysql-connector
pip3 install JPype1
pip3 install Flask
pip3 install Flask-RESTful
pip3 install pycrypto
pip3 install pyserial
pip3 install mettler_toledo_device

apt-get -y install libatlas3-base

echo "Installing Java dependencies..."

apt -y install default-jre

echo "PBRControl is ready to run!"
