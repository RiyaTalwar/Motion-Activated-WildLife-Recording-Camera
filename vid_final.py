import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(13, GPIO.OUT)         #LED output pin
GPIO.setup(19, GPIO.OUT)
GPIO.output(19, 1)


counter =0;
stop=1;
k=0;

while True:
       i=GPIO.input(11)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             GPIO.output(13, 0)  #Turn OFF LED
             time.sleep(1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(13, 1)  #Turn ON LED
             k=k+1;
             while (stop!=0):
                 counter = 0;
                 while (counter<1):
                     print("Video recording started...")
                     subprocess.call("avconv -t 00:00:05 -f video4linux2 -r 10 -s 640x480 -i /dev/video0 -y triggered_video"+str(k)+".avi",shell=True)
                     subprocess.call("MP4Box -add triggered_video.avi triggered_video.mp4",shell=True)
             # time.sleep(6)
                     print("Video Recorded...")
             # counter=counter+1;
                     counter=counter+1;
                 stop=stop-1;
             print("Done First")
             stop=1;
             print("Done")

             time.sleep(1)
