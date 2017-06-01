import subprocess
import time
import random
import sys

# autoclicker developed for NMZ zone prayer restore clicking
# runnable only on linux systems
# ----------------------
# Levon Dovlatyan
# version 0.3
# 8 June 2016
# ----------------------


try:
	time_arg = sys.argv[1]
except:
	time_arg = 2**16
	


def training(train_time=time_arg):
	i = 0	
	
	random.seed() # initialize random seed generator - use current system time as the hashable object
	while i < int(train_time):

		
		# move mouse over the correct point on the screen
		# use the 'xdotool getmouselocation' command in terminal to get coordinates for current location
		#mouse_X = 784
		#mouse_Y = 294
		#subprocess.call(["xdotool", "mousemove", str(mouse_X), str(mouse_Y)])

		# press down on the mouse
		subprocess.call(["xdotool", "key", "up"])
	
		# sleep for a random interval between 0.1 - 0.5 seconds
		upper_range = random.randint(300,500)
		lower_range = random.randint(100,250)
		time.sleep(random.randint(lower_range,upper_range) / 1000.0)
	
		# release mouse click
		subprocess.call(["xdotool", "key", "up"])

		# random delay before next click
		upper_range = random.randint(400,600)
		lower_range = random.randint(100,300)
		time.sleep(random.randint(lower_range,upper_range) / 1000.0)

		# repeat to turn off prayer
		subprocess.call(["xdotool", "key", "up"])
		upper_range = random.randint(300,500)
		lower_range = random.randint(100,250)
		time.sleep(random.randint(lower_range,upper_range) / 1000.0)
		subprocess.call(["xdotool", "key", "up"])
	
		#sleep for random interval between 20-55 seconds
		sleep_time = random.randint(1500,5300)
		i += sleep_time / 100.0
		print "current: " + str(sleep_time / 100.0) + " | total: " + str(i) + " / " + str(train_time)
		time.sleep(sleep_time / 100.0)
		
if __name__ == "__main__":
	training()
