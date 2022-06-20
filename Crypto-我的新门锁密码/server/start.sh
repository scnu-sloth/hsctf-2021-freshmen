#!/bin/sh
# Add your startup script

# DO NOT DELETE
socat tcp-listen:9999,fork exec:"python3 /home/ctf/game.py",reuseaddr
sleep infinity;
