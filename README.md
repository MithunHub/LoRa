# LoRa

## LoRa WaveShare

#### Manual of LoRa

 `LoRa SX1268` https://www.waveshare.com/w/upload/c/c4/SX1268_V1.0.pdf

Schematic https://www.waveshare.com/w/upload/0/09/SX1262_LoRa_HAT_SchDoc.pdf



#### Operation Example

[CN] https://www.waveshare.net/wiki/SX1262_915M_LoRa_HAT 

[EN] https://www.waveshare.com/wiki/SX1262_915M_LoRa_HAT


## GPIO

#### GPIO Homepage

https://sourceforge.net/projects/raspberry-gpio-python/

#### RPi.GPIO Module Basics

https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/


## PySerial

#### PySerial Homepage

https://pyserial.readthedocs.io/en/latest/pyserial.html

#### PySerial API

==This page is very important== 

https://pyserial.readthedocs.io/en/latest/pyserial_api.html



#### What is ttyS0?

In the sample program what does it mean? What I understand is that we open the serial port. Now, what is the use of this?

```python
ser = serial.Serial("/dev/ttyS0",9600)
```

where `9600` is the baud rate. 

More aboout ` ttyS0` [what is ttyS0](https://unix.stackexchange.com/questions/307390/what-is-the-difference-between-ttys0-ttyusb0-and-ttyama0-in-linux)



What is the differnce between miniUART and normal UART? and 

Raspberry Pi UART Pin connection and how many UART in Raspberry pi has? [Link here](https://raspberrypi.stackexchange.com/questions/45570/how-do-i-make-serial-work-on-the-raspberry-pi3-or-later-model/45571#45571)

###

#### How to make sure that the serial port is open?

```python
 import serial
 import time

 ser = serial.Serial()
 ser.braudrate = 115200
 ser.port = "/dev/ttyS0" 
 ser.open()

 print(ser.name)
 if ser.isOpen():
    print("serial is open!")

 ser.close()
```

[Link here](https://stackoverflow.com/questions/21050671/how-to-check-if-device-is-connected-pyserial/49450813)

and 

```python
ser = serial.Serial(DEVICE,BAUD,timeout=1)
if(ser.isOpen() == False):
    ser.open()
```

[Link here](https://stackoverflow.com/questions/6178705/python-pyserial-how-to-know-if-a-port-is-already-open)


