First, we will start by using Raspberry Pi4B. This is the easiest way to start rather than Pi Zero. 


### Step 1: Opening the Serial Port 

Open the serial port of Raspberry Pi. 
```python
sudo raspi-config
```
![WechatIMG3694|40%](https://user-images.githubusercontent.com/20032975/123502315-0ef39580-d67e-11eb-8a00-69b0da34b722.jpeg)

<img src="https://user-images.githubusercontent.com/20032975/123502317-187cfd80-d67e-11eb-9795-2602ecdf15db.jpeg" width="550">

<img src="https://user-images.githubusercontent.com/20032975/123502319-1b77ee00-d67e-11eb-935e-d7375e782df8.jpeg" width="550">

<img src="https://user-images.githubusercontent.com/20032975/123502321-1f0b7500-d67e-11eb-8b61-6b45b1ea586f.jpeg" width="550">

The next step is the most important. Do not skip this just pressing `enter`. 

<img src="https://user-images.githubusercontent.com/20032975/123502322-216dcf00-d67e-11eb-861e-ee4b59f4deb4.jpeg" width="550">
<img src="https://user-images.githubusercontent.com/20032975/123502325-23d02900-d67e-11eb-8421-ead24f7f29e6.jpeg" width="550">
<img src="https://user-images.githubusercontent.com/20032975/123502327-26cb1980-d67e-11eb-8dbe-6d70c0878406.jpeg" width="550">

Alternatively, you can refer to here:

##### How to make sure that the serial port is open?

```python
 import serial
 import time

 ser = serial.Serial()
 ser.braudrate = 9600
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




### Step 2: Checking the Library Files
Check if these libraries are installed or not, if you are using latest version of `Python3`, most probably, these are already installed. 
```python
sudo apt-get install python-pip 
sudo pip install RPi.GPIO
sudo apt-get install python-smbus
sudo apt-get install python-serial
```
