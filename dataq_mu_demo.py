import sys
import serial
import time
import threading


#This sample program will start DATAQ Instrument (11xx/2108/4108/4208/4718) usb data acquisition products
#Please make sure the device is in CDC mode (blinking yellow when conntected)

#Windows
CONST_SER_PORT = 'COM5'   #for Windows get
5

#Linux
#CONST_SER_PORT = '/dev/ttyACM0'   #for Linux
#print("\nNiceness is " + str(os.nice(0)))

serDataq = serial.Serial(CONST_SER_PORT)
serDataq.set_buffer_size=4096

#   Three commands
#   Stop    Press Enter
#   Start   type "start" then Press Enter
#   Exit    type "exit"  then Press Enter, app must be in the stop state, before entering "exit"

def thread_function(name):   # Command function
    global command
    global loopFlg
    last_command = ""
    global threadFlg
    while threadFlg:
        command = sys.stdin.readline()[:-1]
        if command == "start":
            serDataq.write(b"start\r")
        if command == "":
            serDataq.write(b"stop\r")
        if command == "exit":
            if last_command == "":
                loopFlg = False
                threadFlg = False
        last_command = command
        if threadFlg == False:
            break



if __name__ == "__main__":
    loopFlg = True;
    threadFlg = True
    x = threading.Thread(target=thread_function, args=(1,),daemon=True)
    x.start()


    command = "";
    i = 0

    serDataq.write(b"stop\r")        #stop in case device was left scanning
    serDataq.write(b"eol 1\r")
    serDataq.write(b"encode 1\r")    #set up the device for ascii mode
    serDataq.write(b"slist 0 0\r")   #scan list position 0 channel 0 thru channel 3
    serDataq.write(b"slist 1 1\r")
    #serDataq.write(b"slist 2 2\r")
    #serDataq.write(b"slist 3 3\r")
    serDataq.write(b"srate 6000\r") #10000 scans/second
    serDataq.write(b"dec 100\r")    #100 scans/second
    serDataq.write(b"deca 2\r")     #50 scans/sec
    time.sleep(1)
    serDataq.read_all()              #flush all command responses
    serDataq.write(b"start\r")

    while loopFlg:
        i= serDataq.inWaiting()
        while i>0:
            bstr = serDataq.readline()
            i= serDataq.inWaiting()
            # convert byte string returned from Dataq hardware to string
            bstr = bstr[:-1]    # first remove "carriage return"
            s = str(bstr, 'utf-8')

            # turn string into tuple
            print ('(' + s + ')')
        pass
        time.sleep(.001)
    pass

    serDataq.close()
    time.sleep(.1)
    if os.name == 'nt':
        os._exit(0)
    else:
        os._exit(os.EX_OK)
