import subprocess
import time
import random

# autoclicker developed for NMZ zone prayer restore clicking
# runnable only on linux systems
# ----------------------
# Levon Dovlatyan
# version 0.2
# 8 June 2016
# ----------------------

random.seed() # initialize random seed generator - use current system time as the hashable object

while True:
	
	# move mouse over the correct point on the screen
	# use the 'xdotool getmouselocation' command in terminal to get coordinates for current location
	#mouse_X = 784
	#mouse_Y = 294
	#subprocess.call(["xdotool", "mousemove", str(mouse_X), str(mouse_Y)])

	# press down on the mouse
	subprocess.call(["xdotool", "mousedown", "1"])
	
	# sleep for a random interval between 0.1 - 0.5 seconds
	upper_range = random.randint(300,500)
	lower_range = random.randint(100,250)
	time.sleep(random.randint(lower_range,upper_range) / 1000.0)
	
	# release mouse click
	subprocess.call(["xdotool", "mouseup", "1"])

	# random delay before next click
	upper_range = random.randint(400,600)
	lower_range = random.randint(100,300)
	time.sleep(random.randint(lower_range,upper_range) / 1000.0)

	# repeat to turn off prayer
	subprocess.call(["xdotool", "mousedown", "1"])
	upper_range = random.randint(300,500)
	lower_range = random.randint(100,250)
	time.sleep(random.randint(lower_range,upper_range) / 1000.0)
	subprocess.call(["xdotool", "mouseup", "1"])
	
	#sleep for random interval between 20-55 seconds
	sleep_time = random.randint(1500,5300)
	print sleep_time / 100.0
	time.sleep(sleep_time / 100.0)
