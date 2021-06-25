#!/usr/bin/python
# -*- coding: UTF-8 -*-

#
#    this is an UART-LoRa device and thers is an firmware on Module
#    users can transfer or receive the data directly by UART and dont
#    need to set parameters like coderate,spread factor,etc.
#
#    It dont suport LoRaWAN protocol!!!!!!!!!
#    
#    this script is suitable for Raspberry Pi 3B+ 4B and zero series
#    and PC dont have GPIO to control HAT,It should be setted by
#    GUI and combine with jumpers at first,please refer to another script
#    named main_on_pc.py!!!!
#

import sys
import sx126x
import threading
import time
import select
import termios
import tty

old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())


#
#    it must close the uart to login shell and open the hardware uart with
#    command `sudo raspi-config`
#
#    when HAT link to Pi,it should be removed the M0 and M1 jumpers on HAT
#

def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000
#   
#   serial_num
#       Pi3B+ or Pi4B use "/dev/ttyS0"
#       Pi zero series use "/dev/ttyAMA0"
#
#    frequence is 850 to 930 ,or 410 to 493 MHz
#
#    address is 0 to 65535
#        under the same frequence,if set 65535,the node can receive 
#        messages from another node of address is 0 to 65534 and similarly,
#        the address 0 to 65534 of node can receive messages while 
#        the another note of address is 65535 sends.
#        otherwise two node must be same the address and frequence
#
#    power is 10,13,17,22 dBm
#
#    rssi is True or False
#        It will print the rssi value when receive every one message
#
#    choose and uncomment below one line (433,470,868 or 915)

#node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=433,addr=30,power=22,rssi=False)
#node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=470,addr=20,power=22,rssi=True)
node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=868,addr=21,power=22,rssi=True)
#node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=915,addr=50,power=22,rssi=True)

def send_deal():
    get_rec = ""
    print("")
    print("input a string such as \033[1;32m20,Hello World\033[0m,it will send `Hello World` to node of address 20 ",flush=True)
    print("please input and press Enter key:",end='',flush=True)

    while True:
        rec = sys.stdin.read(1)
        if rec != None:
            if rec == '\x0a': break
            get_rec += rec
            sys.stdout.write(rec)
            sys.stdout.flush()

    get_t = get_rec.split(",")
    node.set(node.freq,int(get_t[0]),node.power,node.rssi)
    node.send(get_t[1])

    print('\x1b[2A',end='\r')
    print("                                                                                         ")
    print("                                                                                         ")
    print("                                                                                         ")
    print('\x1b[3A',end='\r')

try:
    time.sleep(1)
    print("Press \033[1;32mEsc\033[0m to exit")
    print("Press \033[1;32mi\033[0m   to send")
    
    node.send("CPU Temperature:"+str(get_cpu_temp())+" C")
    
    while True:

        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            c = sys.stdin.read(1)
            # dectect key Esc
            if c == '\x1b': break
            # dectect key i
            if c == '\x69':
                send_deal()
            sys.stdout.flush()
        node.receive()
except:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    print("")
    print("")
    print("")

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
print("")
print("")
print("")
