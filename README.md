# LoRa and Raspberry Pi 4B/Zero
We aim to develop a peer-to-peer network, where one and multiple Raspberry Pis are collecting data and send to PC (may be regarded as an edge node). 

### File name and their meaning
- `pc_main.py`  This file is for PC, the default LoRa node's address is 100. We can test the LoRa's parameter settings by the RF module (see the basic instruction page). 
- `Rpi_main.py` This is for Raspberry pi, the default address of LoRa module is 21. Note that if we use multiple Pis, we need to set the node's address in this source code. 
- `BigData.py` We use this script to transfer a large file, the LoRa module's default address is 21. 


### LoRa manufacturer
In the following, we use the LoRa modules by [WaveShare](https://www.waveshare.com).

#### Manual of LoRa

 `LoRa SX1268` [Link here](https://www.waveshare.com/w/upload/c/c4/SX1268_V1.0.pdf) and its [Schematic](https://www.waveshare.com/w/upload/0/09/SX1262_LoRa_HAT_SchDoc.pdf) diagram.

#### Operation Example

You can see some basic examples in [CN](https://www.waveshare.net/wiki/SX1262_915M_LoRa_HAT) and also in [EN](https://www.waveshare.com/wiki/SX1262_915M_LoRa_HAT).
