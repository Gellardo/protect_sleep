#!/usr/bin/python
#
# main script for using protect_sleep, providing the whole functionality
import time

##policies -> per weekday and deadline correction for different programms
daily_deadlines = {'1': '23:00', '2': '23:00', '3': '23:00', '4': '23:00', '5': '23:00', '6': '23:00', '0': '23:00'}
modifiers = {'firefox':'00:15','urxvt': '00:05'}
sleep_minutes = 5

def get_process_list():
    import subprocess
    string = subprocess.Popen(['ps','xo', 'comm'], stdout=subprocess.PIPE).communicate()[0]
    string = string.decode()
    return string.split('\n')[1:len(string)-3]

def notify_user():
    print("hey man, go to sleep")

def hours_to_minutes(time):
    """
    input: 'HH:MM', output: same time in minutes
    """
    time = time.split(':')
    return int(time[0])*60 + int(time[1])
def minutes_to_hours(time):
    """
    input: time in minutes, output: same in 'HH:MM'
    """
    return str(time // 60) + ':' + str(time % 60)

def modify_time(processes, c_t, debug=False):
    """
    return the current time c_t warped into the future depending on running processes.
    """
    delta_t = 0
    for p in processes:
        if p in modifiers:
            delta_t = max(hours_to_minutes(modifiers[p]), delta_t)
    if delta_t > 0 and debug:
        print('added this many minutes:',str(delta_t))
    return minutes_to_hours(hours_to_minutes(c_t) + delta_t)

def is_deadline_broken(deadlines, c_d, c_t, debug=False):
    """
    return True if the time c_t lies within a 4 hours time window after
    one of the deadlines of dl_t

    format of deadlines: { 'D':'HH:MM' }
    format of c_d, c_t: 'D', 'HH:MM'
    """
    c_t = hours_to_minutes(c_t)

    #loop to check the current day and the day before
    for i in [0,1]:
        dl_t = deadlines[str( (int(c_d)-i)%7 )]
        #correct the minutes representation of the time depending on the day modification
        dl_t = hours_to_minutes(dl_t) - i*24*60

        if( dl_t < c_t and dl_t+4*60 > c_t ):
            if debug:
                print('deadline broken')
            return True
    if debug:
        print('no deadline broken')
    return False

if __name__ == '__main__':
    #mainloop
    deadline_broken = False

    while(True):
        #checking for deadlines
        curr_day = time.strftime('%w')

        if( daily_deadlines[curr_day] ):
        #if we have a deadline for today
            current_time = time.strftime('%H:%M')

            #look for corrections for open programms
            processes = get_process_list()
            current_time = modify_time(processes, current_time)

            if( is_deadline_broken(daily_deadlines, curr_day, current_time) ):
                deadline_broken = True
                sleep_minutes = 1

    ##if deadline is broken, notify the user
        if(deadline_broken):
            notify_user()

    #sleep and wait for configured number of minutes
        time.sleep(sleep_minutes*60)
