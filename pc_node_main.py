#!/usr/bin/python
# -*- coding: UTF-8 -*-

#
#    this is an UART-LoRa device and thers is an firmware on Module
#    users can transfer or receive the data directly by UART and dont
#    need to set parameters like coderate,spread factor,etc.
#    |============================================ |
#    |   It does not suport LoRaWAN protocol !!!   |
#    | ============================================|
#   
#    This script is mainly for Raspberry Pi 3B+, 4B, and Zero series
#    Since PC/Laptop does not have GPIO to control HAT, it should be configured by
#    GUI and while setting the jumpers, 
#    Please refer to another script pc_node_main.py
#

import time
import sys
import serial


class sx126x:

    M0 = 22
    M1 = 27
    # if the header is 0xC0, then the LoRa register settings dont lost when it poweroff, and 0xC2 will be lost. 
    # cfg_reg = [0xC0,0x00,0x09,0x00,0x00,0x00,0x62,0x00,0x17,0x00,0x00,0x00]
    cfg_reg = [0xC2,0x00,0x09,0x00,0x00,0x00,0x62,0x00,0x17,0x00,0x00,0x00]
    get_reg = bytes(12)
    rssi = False
    addr = 65535
    serial_n = ""
    send_to = 0
    addr_temp = 65535
    freq = 868
    power = 22
    air_speed =2400

    SX126X_UART_BAUDRATE_1200 = 0x00
    SX126X_UART_BAUDRATE_2400 = 0x20
    SX126X_UART_BAUDRATE_4800 = 0x40
    SX126X_UART_BAUDRATE_9600 = 0x60
    SX126X_UART_BAUDRATE_19200 = 0x80
    SX126X_UART_BAUDRATE_38400 = 0xA0
    SX126X_UART_BAUDRATE_57600 = 0xC0
    SX126X_UART_BAUDRATE_115200 = 0xE0

    SX126X_AIR_SPEED_300bps = 0x00
    SX126X_AIR_SPEED_1200bps = 0x01
    SX126X_AIR_SPEED_2400bps = 0x02
    SX126X_AIR_SPEED_4800bps = 0x03
    SX126X_AIR_SPEED_9600bps = 0x04
    SX126X_AIR_SPEED_19200bps = 0x05
    SX126X_AIR_SPEED_38400bps = 0x06
    SX126X_AIR_SPEED_62500bps = 0x07

    SX126X_PACKAGE_SIZE_240_BYTE = 0x00
    SX126X_PACKAGE_SIZE_128_BYTE = 0x40
    SX126X_PACKAGE_SIZE_64_BYTE = 0x80
    SX126X_PACKAGE_SIZE_32_BYTE = 0xC0

    SX126X_Power_22dBm = 0x00
    SX126X_Power_17dBm = 0x01
    SX126X_Power_13dBm = 0x02
    SX126X_Power_10dBm = 0x03

    def __init__(self,serial_num,freq,addr,power,rssi):
        self.rssi = rssi
        self.addr = addr
        self.freq = freq
        self.serial_n = serial_num
        self.power = power
        self.send_to = addr

        # The hardware UART of Pi3B+,Pi4B is /dev/ttyS0
        self.ser = serial.Serial(serial_num,9600)
        self.ser.flushInput()

    def air_speed_cal(self,airSpeed):
        air_speed_c = {
            1200:self.SX126X_AIR_SPEED_1200bps,
            2400:self.SX126X_AIR_SPEED_2400bps,
            4800:self.SX126X_AIR_SPEED_4800bps,
            9600:self.SX126X_AIR_SPEED_9600bps,
            19200:self.SX126X_AIR_SPEED_19200bps,
            38400:self.SX126X_AIR_SPEED_38400bps,
            62500:self.SX126X_AIR_SPEED_62500bps
        }
        return air_speed_c.get(airSpeed,None)

    def power_cal(self,power):
        power_c = {
            22:self.SX126X_Power_22dBm,
            17:self.SX126X_Power_17dBm,
            13:self.SX126X_Power_13dBm,
            10:self.SX126X_Power_10dBm
        }
        return power_c.get(power,None)

    def buffer_size_cal(self,bufferSize):
        buffer_size_c = {
            240:self.SX126X_PACKAGE_SIZE_240_BYTE,
            128:self.SX126X_PACKAGE_SIZE_128_BYTE,
            64:self.SX126X_PACKAGE_SIZE_64_BYTE,
            32:self.SX126X_PACKAGE_SIZE_32_BYTE
        }
        return buffer_size_c.get(bufferSize,None)


    def send(self,data):
        # add the node address ,and the node of address is 65535 can konw who send messages
        l_addr = self.addr_temp & 0xff
        h_addr = self.addr_temp >> 8 & 0xff

        self.ser.write(bytes([h_addr,l_addr])+data.encode())
        # if self.rssi == True:
            # self.get_channel_rssi()
        time.sleep(0.1)

    def receive(self):
        if self.ser.inWaiting() > 0:
            time.sleep(0.2)
            r_buff = ""
            r_buff = self.ser.read(self.ser.inWaiting())
            self.ser.flushInput()

            print("receive message from address %d node "%((r_buff[0]<<8)+r_buff[1]))
            print("message is "+str(r_buff[2:]))
            # print the rssi
            if self.rssi:
                self.get_channel_rssi()                
            else:
                pass
                # print('\x1b[2A',end='\r')
            
    def get_channel_rssi(self):
        time.sleep(0.2)
        self.ser.flushInput()
        self.ser.write(bytes([0xC0,0xC1,0xC2,0xC3,0x00,0x02]))
        time.sleep(0.5)
        re_temp = bytes(5)
        if self.ser.inWaiting() > 0:
            time.sleep(0.1)
            re_temp = self.ser.read(self.ser.inWaiting())
        if re_temp[0] == 0xC1 and re_temp[1] == 0x00 and re_temp[2] == 0x02:
            print("the current noise rssi value: -{0}dBm".format(256-re_temp[3]))
            # the packet rssi dont work now
            # print("the last receive packet rssi value: -{0}dBm".format(256-re_temp[4]))
            print("",flush=True)
        else:
            # pass
            print("receive rssi value fail")
            # print("receive rssi value fail: ",re_temp)

        self.ser.flushInput()
    def free_serial(self):
        self.ser.close()
    #def relay(self):
    #def wor(self):
    #def remote_config(self):


#
#    Need to disable the serial login shell and have to enable serial interface 
#    command `sudo raspi-config`
#    More details: see https://github.com/MithunHub/LoRa/blob/main/Basic%20Instruction.md
#
#    When the LoRaHAT is attached to RPi, the M0 and M1 jumpers of HAT should be removed.
#

#   serial_num
#       PiZero, Pi3B+, and Pi4B use "/dev/ttyS0"
#
#    Frequency is [850 to 930], or [410 to 493] MHz
#
#    address is 0 to 65535
#        under the same frequence,if set 65535,the node can receive 
#        messages from another node of address is 0 to 65534 and similarly,
#        the address 0 to 65534 of node can receive messages while 
#        the another note of address is 65535 sends.
#        otherwise two node must be same the address and frequence
#
#    The tramsmit power is {10, 13, 17, and 22} dBm
#
#    RSSI (receive signal strength indicator) is {True or False}
#        It will print the RSSI value when it receives each message
#

node = sx126x(serial_num = "COM8",freq=433,addr=100,power=22,rssi=True)
# node = sx126x(serial_num = "COM8",freq=868,addr=65535,power=22,rssi=True)


def send_deal():
    get_rec = ""
    print("")
    print("input a string such as Hello World,it will send `Hello World` to all node address is from 0 to 65535",flush=True)
    print("please input and press Enter key:",end='',flush=True)
    lines=sys.stdin.readlines()
    node.send(lines)
    
try:
    time.sleep(1)
    print("Press Ctrl+C to exit")

    while True:
        node.receive()
        
except:
    node.free_serial()
    pass
