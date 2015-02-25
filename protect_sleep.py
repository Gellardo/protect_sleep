#!/usr/bin/python
#
# main script for using protect_sleep, providing the whole functionality
import time

##policies -> per weekday and deadline correction for different programms
daily_deadlines = {'1': '23:00', '2': '23:00', '3': '23:00', '4': '23:00', '5': '23:00', '6': '23:00', '0': '23:00'}
sleep_minutes = 5

def notify_user():
    print("hey man, go to sleep")

def is_deadline_broken(deadlines, c_d, c_t):
    """
    return True if the time c_t lies within a 4 hours time window after
    one of the deadlines of dl_t

    format of deadlines: { 'D':'HH:MM' }
    format of c_d, c_t: 'D', 'HH:MM'
    """
    c_t = c_t.split(':')
    c_t = int(c_t[0])*60 + int(c_t[1])

    #loop to check the current day and the day before
    for i in [0,1]:
        dl_t = deadlines[str( (int(c_d)-i)%7 )]
        dl_t = dl_t.split(':')
        #correct the minute representation of the time depending on the day modification
        dl_t = int(dl_t[0])*60 + int(dl_t[1]) - i*24*60

        if( dl_t < c_t and dl_t+4*60 > c_t ):
            return True
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

            if( is_deadline_broken(daily_deadlines, curr_day, current_time) ):
                deadline_broken = True
                sleep_minutes = 1

    ##if deadline is broken, notify the user
        if(deadline_broken):
            notify_user()

    #sleep and wait for configured number of minutes
        time.sleep(sleep_minutes*60)
