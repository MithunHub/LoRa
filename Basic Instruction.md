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


## Install RealVNC server and viewer
It would be good to install RealVNC server

[Link here](https://www.raspberrypi.org/forums/viewtopic.php?t=214569)

```python
sudo apt-get install RealVNC-vnc-server
```
or 

```python
sudo apt-get install realvnc-vnc-server
```

```python
sudo apt-get install realvnc-vnc-viewer
sudo apt-get update
```

now to configure the settings in the terminal type the following.

```python
sudo raspi-config
```

Now go to - interfacing and scroll down to VNC click enter and click Enable.

Now to make sure everything is set in place and ready to rock and roll: complete the following in terminal

```python
sudo apt-get update
sudo apt-get upgrade
sudo reboot
```
Now your Pi is ready to use Real VNC. download RealVNC on your windows machine and launch it.
Back on your PI, double-click on the vnc server button in the upper right taskbar. copy IP under connectivity and paste that into your windows machine.

verbatim from here: [Link here](https://www.raspberrypi.org/forums/viewtopic.php?t=214569)



### How to use on Windows PC
install python3 on pc

open the cmd add python path to cmd,then install pyserial,see figure set_env.jpg
```
path=%path%;C:\Users\zhongshaohua\AppData\Local\Programs\Python\Python37
path=%path%;C:\Users\zhongshaohua\AppData\Local\Programs\Python\Python37\Scripts
pip3 install pyserial
```

open the manager to check the LoRa HAT COMx number and change it on pc_node_main.py file,like that
```
node = sx126x(serial_num = "COM8",freq=868,addr=65535,power=22,rssi=True)
```

run the code example
```
python C:\Users\zhongshaohua\Desktop\pc_node_main.py
```

