fuser -k -n tcp 2820
python3 -m http.server 2820 &

ssh -o ServerAliveInterval=60 -R qscdwe:80:localhost:2820 serveo.net
