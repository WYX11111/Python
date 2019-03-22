import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

gpio_in = 7

gpio.setup(gpio_in,gpio.IN)
while(1):
	while gpio.input(gpio_in)==0:
		print "0"
		
	while gpio.input(gpio_in)==1:
		print "1"
