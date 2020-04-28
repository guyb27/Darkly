#!/usr/bin/env bash
echo "Enter IP address"
read IP
echo "Enter PORT (only 80, 8080)"
read PORT
echo "WAIT.................................."
curl  -d 'username=root&password=dragon&Login=Login' -X POST "http://${IP}:${PORT}/admin/"
