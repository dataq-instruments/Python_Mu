# Python_Mu
A Mu project for DI-1110, DI-2108, DI-4108, DI-4208 

**Prerequisites**:

Install Python

After installing Python, one needs to pyserial module under command prompt

python -m pip install -U pyserial --user

Turn 21xx/11xx/41xx/47xx into CDC mode: plug the device to USB port, if the LED already blinks Yellow, stop, you are already in CDC mode. If not, once the LED turns blinking Green, push and hold the button immediately (within 5 second time frame), the LED should turn white, hold until LED turns Red, then release the button, now the LED will blink yellow to indicate CDC mode. If you need to exit CDC mode, repeate the same action and a green blinking LED will indicate LibUSB mode.

From Device Manager, find out the COM port of the device connected to, and modify the program accordingly

![alt text](https://www.dataq.com/resources/repository/matlab_devicemanager.png)

**To test the project**

Make sure the COM port matches the one assigned to the device

Run it 

Push the waveform icon to generate live waveform

![alt text](https://www.dataq.com/resources/repository/mu.gif)

**Other Examples**

https://github.com/dataq-instruments/Python1110

https://github.com/dataq-instruments/Simple-Python-Codes-for-DI-1110

https://github.com/dataq-instruments/Simple-Python-Codes

https://github.com/dataq-instruments/Python245

https://github.com/dataq-instruments/Python


