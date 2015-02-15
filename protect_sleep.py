#!/usr/bin/python
import subprocess
import time

#subprocess.check_output(['echo','Hello World'], universal_newlines=True)
#subprocess.call(['espeak','Hello, how are you?'])
#time.strftime('%A(%w) %H:%M')

#setup (windows and stuff)
##commands on different os
###message on screen
###sound
def read_message(text='deadline close'):
    subprocess.call(['espeak',text])
###get process list
def get_processes():
    return ['firefox', 'bash', 'bash']
###?sleep

##policies -> per weekday and deadline correction for different programms
daily_deadlines = {'Monday': '24:00', 'Thuesday': '1:00', 'Wendsday': '1:00', 'Thursday': '1:00', 'Friday': '1:00', 'Saturday': '2:00', 'Sunday': '1:00'}
programm_adjustments = [('firefox','firefox', 5), ('flash','flashplugin',10)]
sleep_minutes=5

##windows

#mainloop
while(True):
##checking for deadlines
    curr_time = time.strftime('%H:%M')
    curr_processes = get_processes()
    deadline = closestDeadline(curr_processes, programm_adjustments)
    if(deadline < curr_time):
        deadline_broken = True

##if deadline is broken, notify the user
    if(deadline_broken):
        notify_user()

#sleep and wait for configured number of minutes
    time.sleep(sleep_minutes*60)
