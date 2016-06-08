#!/bin/bash

while [ 1 ]; do
	echo $[ ($RANDOM % 60) + 1 ]
	xdotool mousemove 618 307 &
	xdotool mousedown 1 &
	sleep 0.1
	xdotool mouseup 1 &
	sleep 2
done
