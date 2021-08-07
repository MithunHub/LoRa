# Notes

- This code is to send a LoRa message from Raspberry Pi (run `rasp_pi.py`) to PC (run `pc_main.py`). 
- The data is saved in _save_data_01.csv_ file, the data will be automatically appended. 


The following library would be useful 
- [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) for data handling and 
- [RaspberryPi Date and Time basic introduction](https://projects.raspberrypi.org/en/projects/generic-python-strftime)

The program is very simple to use. The only difference that I made from the base program is
- `def get_channel_rssi(self):` will return channel RSSI and noise RSSI register value
- using pandas, the data will be appended using 
```python
data_holder = pd.read_csv('save_data_01.csv')
day = strftime("%d %m %Y at %I:%M:%S%p")
new_data = pd.Series([str(day),str((r_buff[0]<<8)+r_buff[1]), str(-(256-r)),str(-(256-r1))], index= ['Time Rx','Node','Noise RSSI','Channel RSSI'])
data_holder = data_holder.append(new_data,ignore_index=True)
data_holder.to_csv('save_data_01.csv',index=False) 
```

The format of data saved in _save_data_01.csv_ has been mentioned in the first row of the _csv_ file and `index= ['Time Rx','Node','Noise RSSI','Channel RSSI']`. 

Happy coding 🐥
