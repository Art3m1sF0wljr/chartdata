#!/usr/bin/python


import numpy as np
import time
import matplotlib.pyplot as plt
import Adafruit_BMP.BMP085 as BMP085

    
plt.ion()

#x=np.linspace(0,10000,10001)


while True:

    sensor = BMP085.BMP085()
    
    
    print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
    print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))

    f=open("all_time.txt", "a")
    f.write('{0:0.2f}'.format(sensor.read_temperature())+" "+'{0:0.2f}'.format(sensor.read_pressure())+" "+str(int(time.time()))+'\n')
    f.close()
    
    f=open("temp.txt", "a")
    f.write('{0:0.2f}\n'.format(sensor.read_temperature()))
    f.close()
    
    g=open("pres.txt", "a")
    g.write('{0:0.2f}\n'.format(sensor.read_pressure()))
    g.close()
    
    read=open("pres.txt", "r")
    last=read.readlines()
    lines=last[-10000:]
    read.close()
    
    a = np.array(lines)
    y = a.astype(np.float)
    
    read=open("temp.txt", "r")
    last=read.readlines()
    lines=last[-10000:]
    read.close()
    
    a = np.array(lines)
    z = a.astype(np.float)
    
    #fig, ax_left=plt.subplots()
    #ax_right=ax_left.twinx()
    #ax_left.plot(y, 'b-')
    #ax_right.plot(z, 'r-')
    
    
    
    plt.plot(z)
    
    plt.draw()
    plt.pause(0.0001)
    plt.clf()
    time.sleep(10)
    plt.plot(y)
    plt.draw()
    plt.pause(0.0001)
    plt.clf()
    
    #plt.clear()
    #plt.plot(y)
    #plt.show()
    
    time.sleep(10)
