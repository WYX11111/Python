import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

gpio_trig=10
gpio_echo=12
gpio.setup(gpio_trig,gpio.OUT)
gpio.output(gpio_trig,gpio.LOW)
gpio.setup(gpio_echo,gpio.IN)

for times in range(1,6): # 重复测5次
    gpio.output(gpio_trig,gpio.HIGH) # 需要10μs以上
    i=1
    i=1
    i=1
    gpio.output(gpio_trig,gpio.LOW)
    while gpio.input(gpio_echo)==0:
        continue
    t1=time.time()
    while gpio.input(gpio_echo)==1:
        continue
    t2=time.time()
    distance=(t2-t1)*340/2
    print(distance)
    time.sleep(0.1)
