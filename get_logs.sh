#!/bin/bash

SENSOR_USER="pi"
SENSOR_IP="192.168.1.122"
SENSOR_PORT=8444
SENSOR_LOG_DIR="/home/cowrie/cowrie/log/"

# Use scp to copy the json logs from the sensor and store it to the
# local json directory

scp -P ${SENSOR_PORT} ${SENSOR_USER}@${SENSOR_IP}:${SENSOR_LOG_DIR}/*json* json/
