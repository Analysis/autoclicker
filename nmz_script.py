import subprocess
import time
import random
import sys

try:
	time_arg = sys.argv[1]
except:
	time_arg = 2**16
	


def training(train_time=time_arg):
	i = 0	
	
	random.seed()
	while i < int(train_time):
		subprocess.call(["xdotool", "keydown", "up"])
		upper_range = random.randint(300,500)
		lower_range = random.randint(100,250)
		time.sleep(random.randint(lower_range,upper_range) / 1000.0)
		subprocess.call(["xdotool", "keyup", "up"])
		upper_range = random.randint(400,600)
		lower_range = random.randint(100,300)
		time.sleep(random.randint(lower_range,upper_range) / 1000.0)
		sleep_time = random.randint(1500,5300)
		i += sleep_time / 100.0
		print "current: " + str(sleep_time / 100.0) + " | total: " + str(i) + " / " + str(train_time)
		time.sleep(sleep_time / 100.0)
		
if __name__ == "__main__":
	training()
