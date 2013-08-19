tornabot
========

Web application to control a raspberryPi robot


At first glance here we got a simple commands for control the camera and picobord.(the picoborg drivers and scripts should be installed)


+ on the client nc -l 5001 | mplayer -fps 25 -cache 1024 -
+ on the server will transmit with the camera raspivid -w 640 -h 480 -fps 10 -t 999999 -o - | nc [ip.client] 5001 &
