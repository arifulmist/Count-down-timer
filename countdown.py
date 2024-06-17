# import the time module 
import time 

# define the countdown func. 
def countdown(t): 
	
	while t: 
		mins, secs = divmod(t, 60) 
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print(timer, end="\r") #Using end = ‘\r’ we force the cursor to go back to the start of the screen
		# (carriage return) so that the next line printed will overwrite the previous one.
		time.sleep(1) #time change every 1 sec
		t -= 1
	
	print('exam is over!!') 


# input time in seconds 
t = int(input("set the time in seconds to start the exam: ") )

# function call 
countdown(t) 
