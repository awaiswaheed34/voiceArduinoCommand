from cmath import pi
import speech_recognition as sr
import serial
import time
r = sr.Recognizer()
ArduinoSerial = serial.Serial('com5',9600)
time.sleep(2)
mic = sr.Microphone()
lst = ["on 1","off 1" , "on 2" , "off 2" , "on 3" , "off 3"]
flag = 0
while(True):
    with mic as source:
        
        r.adjust_for_ambient_noise(source)
        print("LISTENING.................")
        audio = r.listen(source, phrase_time_limit=3)
        print("CONVERTING........")
        try:
            txt = r.recognize_google(audio )
                
        except:
            txt = ""
        # if(flag>=len(lst)):
        #     flag = 0
        # txt =lst[flag]
        # flag+=1
        
        
        print()
        print(txt)
        if "exit" in txt:
            break
        if "on"  in txt:
            ArduinoSerial.write(str.encode('0'))
            if "2" in txt:
                ArduinoSerial.write(str.encode('2'))
            elif "1" in txt:
                ArduinoSerial.write(str.encode('1'))
            elif "3" in txt:
                ArduinoSerial.write(str.encode('3'))
        elif "off" in txt.lower():
            ArduinoSerial.write(str.encode('9'))
            if "1" in txt:
                ArduinoSerial.write(str.encode('1'))
            elif "2" in txt:
                ArduinoSerial.write(str.encode('2'))
            elif "3" in txt:
                ArduinoSerial.write(str.encode('3'))
        
        time.sleep(1)