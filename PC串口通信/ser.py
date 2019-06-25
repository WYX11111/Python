import  serial

ser=serial.Serial("com12",115200,timeout=0.5)

ser.write("#1P1500#2P522#3P1389T1000\n\r".encode('utf-8'))
