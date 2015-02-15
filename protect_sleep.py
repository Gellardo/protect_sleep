#!/usr/bin/python
#
# main script for using protect_sleep, providing the whole functionality
import time

##policies -> per weekday and deadline correction for different programms
#daily_deadlines = {'Monday': '24:00', 'Thuesday': '1:00', 'Wendsday': '1:00', 'Thursday': '1:00', 'Friday': '1:00', 'Saturday': '2:00', 'Sunday': '1:00'}
deadline = { 'today': '23:00' }
sleep_minutes = 5

def notify_user():
    print("hey man, go to sleep")

def is_deadline_broken(dl_t, c_t):
    """
    return True if the time given by dl_t is smaller than the time c_t

    format of dl_t and c_t: 'HH:MM'
    """
    #TODO need to think about handling the edge case 24:00
    dl_t = dl_t.split(':')
    c_t = c_t.split(':')

    if( int(dl_t[0]) < int(c_t[0]) ):
        return True
    elif( int(dl_t[0]) == int(c_t[0]) and int(dl_t[1]) <= int(c_t[1]) ):
        return True
    else:
        return False

if __name__ == '__main__':
    #mainloop
    while(True):
        #checking for deadlines
        curr_day = time.strftime('%w')
        if( deadline['today'] ): #|| deadline[curr_day]):
        #if we have a deadline for today
            deadline_time = deadline['today'] #deadline[curr_day]
            current_time = time.strftime('%H:%M')

            if( is_deadline_broken(deadline_time, current_time) ):
                deadline_broken = True
                sleep_minutes = 1

    ##if deadline is broken, notify the user
        if(deadline_broken):
            notify_user()

    #sleep and wait for configured number of minutes
        time.sleep(sleep_minutes*60)
