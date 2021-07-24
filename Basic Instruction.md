First, we will start by using Raspberry Pi4B. This is the easiest way to start rather than Pi Zero. 


### Step 1: Opening the Serial Port 

Open the serial port of Raspberry Pi. 
```python
sudo raspi-config
```
![img](https://user-images.githubusercontent.com/20032975/123502315-0ef39580-d67e-11eb-8a00-69b0da34b722.jpeg)

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


### Step 3: Clone GitHub

```python
sudo apt-get update 
sudo apt-get upgrade
sudo apt-get install git
```
Then, clone the git to your preferred directory, e.g., ``mkdir ~\git-repo\`` and ``cd git-repo``
```python
git clone https://github.com/MithunHub/LoRa.git
```
verbatim from here: [Link here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)


## How to use on Windows PC

### Step 1: Install Python3 and required packages
install `python3` on pc

Open the cmd add python path to cmd, then install `pyserial`, see figure set_env.jpg

```
path=%path%;C:\Users\zhongshaohua\AppData\Local\Programs\Python\Python37
path=%path%;C:\Users\zhongshaohua\AppData\Local\Programs\Python\Python37\Scripts
pip3 install pyserial
```

#### Alternative way, easiest!😊
if you are using `Anaconda + Spyder`, then `conda install -c anaconda pyserial`

### Step 2: Update the COM port driver 

Open Device manager in Windows PC, then go the Port, and manually update the driver from this source file [CP210x_USB_TO_UART Driver](https://github.com/MithunHub/LoRa/files/6834424/CP210x_USB_TO_UART.zip)


### Step 3: Obtain the address of LoRa HAT COMx and set it in the Python code
Open Device manager to check the LoRa HAT COMx number and change it on pc_main.py file, for example

```python
node = sx126x(serial_num = "COM8",freq=433,addr=100,power=22,rssi=True)
```

run the code example
```python
python3 C:\Users\zhongshaohua\Desktop\pc_node_main.py
```

# Important Additional Resources 

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


## Getting started with Pi Camera

[Link here](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/)


## Install and Update Anaconda in China

Anaconda is a Python distribution that contains common packages for data science. It is derived from conda, a package and environment manager. 

Simply put, just run these two commands separately in cmd.
```python
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```

[Tsinghua mirror for Anaconda](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

[CSDN link](https://blog.csdn.net/qq_37392932/article/details/81210470)

How to install a package in anaconda
```python
conda install package_name
```

## A good link to Print in Python
[Link here](https://realpython.com/python-print/)

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



