# import calendar
from tkinter import *
import socket
import struct
import sys
import time
import datetime as datetime
import win32api
import pytz

# window=Tk()
window =Tk()


def window_GUI_daylight_off():
    window.title("Time Fix")
    window.geometry("500x350")
    hour_decrease=utcTime.hour-1
    win32api.SetSystemTime(utcTime.year, utcTime.month, utcTime.weekday(),utcTime.day, hour_decrease, utcTime.minute, utcTime.second,0)
    # tz=pytz.timezone()
    localTime = datetime.datetime.fromtimestamp(epoch_time)
    forChangedTime=[localTime.day,"-",localTime.month,"-",localTime.year, "--->", localTime.hour-1,":",localTime.minute,":",localTime.second]
    # localTime.year, localTime.month,localTime.day,localTime.hour-1, localTime.minute, localTime.second
    # localTime- (utcTime.hour-1)

    for_gui=str("Time updated to: " + localTime.strftime("%d-%m-%Y %I:%M%p") + " from " + server)

    j= Label(text="You Time Fixed", fg="green", padx= 30, pady=20, font=("Helvetica", 17)).pack()
    v=StringVar()
    w = Label(textvariable=v, fg="green", padx= 5, pady=50, font=("Helvetica", 14)).pack()
    v.set(for_gui)
    j= Label(text="Time set in system", fg="green", padx= 30, pady=20, font=("Helvetica", 17)).pack()
    x=StringVar()
    w = Label(textvariable=x, fg="green", padx= 5, pady=50, font=("Helvetica", 14)).pack()
    x.set(forChangedTime)
    # Button(wiindow, text="Exit", width=14, command= close_window.grid(row=7, column=0)
    # def close_window():
    #     window.destroy()
    #     exit()


def window_GUI_daylight_on():
    window.title("Time Fix")
    window.geometry("500x350")
    win32api.SetSystemTime(utcTime.year, utcTime.month, utcTime.weekday(),utcTime.day, utcTime.hour, utcTime.minute, utcTime.second,0)
    localTime = datetime.datetime.fromtimestamp(epoch_time)
    for_gui=str("Time updated to: " + localTime.strftime("%d-%m-%Y %I:%M%p") + " from " + server)
    j= Label(text="You Time Fixed", fg="green", padx= 30, pady=20, font=("Helvetica", 17)).pack()
    v=StringVar()
    w = Label(textvariable=v, fg="green", padx= 5, pady=50, font=("Helvetica", 14)).pack()
    v.set(for_gui)

# def daylight_on():
#     win32api.SetSystemTime(utcTime.year, utcTime.month,utcTime.weekday(), utcTime.day, utcTime.hour, utcTime.minute, utcTime.second, 0)
#     localTime = datetime.datetime.fromtimestamp(epoch_time)
#     print ("Time updated to: " + localTime.strftime("%d-%m-%Y %I:%M%p") + " from " + server)
    # print(utcTime)

# def daylight_off():
#     hour_decrease=utcTime.hour-1
#     win32api.SetSystemTime(utcTime.year, utcTime.month, utcTime.weekday(),utcTime.day, hour_decrease, utcTime.minute, utcTime.second,0)
#     localTime = datetime.datetime.fromtimestamp(epoch_time)
#     print ("Time updated to: " + localTime.strftime("%d-%m-%Y %I:%M%p") + " from " + server)
#     window_GUI()


# v=StringVar()
# w = Label( textvariable=v, fg="green", padx= 5, pady=50, font=("Helvetica", 17)).pack()
# v.set()
    # print(utcTime)          ,'%Y %b %a %d %I:%M%p')

# List of servers in order of attempt of fetching
server_list = [ 'time.windows.com', '0.uk.pool.ntp.org', 'pool.ntp.org']

'''
Returns the epoch time fetched from the NTP server passed as argument.
Returns none if the request is timed out (5 seconds).
'''
def gettime_ntp(addr='time.windows.com'):
    # http://code.activestate.com/recipes/117211-simple-very-sntp-client/
    TIME1970 = 2208988800
    client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    data = '\x1b' + 47 * '\0'
    try:
        # Timing out the connection after 5 seconds, if no response received
        client.settimeout(5.0)
        client.sendto(data.encode('utf-8'), (addr, 123))
        data, address = client.recvfrom( 1024 )
        if data:
            epoch_time = struct.unpack( '!12I', data )[10]
            epoch_time -= TIME1970
            print("epochtime",epoch_time)
            return epoch_time
    except socket.timeout:
        return None

if __name__ == "__main__":

    # Iterates over every server in the list until it finds time from any one.
    for server in server_list:
        epoch_time = gettime_ntp(server)
        if epoch_time is not None:

            # SetSystemTime takes time as argument in UTC time. UTC time is obtained using utcfromtimestamp()
            # utcTime = datetime.datetime.strptime("18/1/1 12:30" , "%y/%m/%d  %H:%M")
            # cld=calendar.month(2018,10)
            # for i, d in enumerate(self.itermonthdays(year, month), self.firstweekday):
            # for_year_month= (utcTime.year, utcTime.month)

            utcTime = datetime.datetime.utcfromtimestamp(epoch_time)




            # hour_cal=int(utcTime.hour)
            # minute_cal=int(utcTime.minute)
            # time_h_m=(hour_cal,minute_cal)
            # time_format= time_h_m.strftime("%I:%M%p")
            # print(time_format)
            # if hour_cal >= 12 and minute_cal>1:




            # check_utc=datetime.datetime.strftime(utcTime, '%I:%M%p' )
            # print("Check {}" .format(check_utc))
            march=3
            october=10
            march_day=25
            oct_day=28
            def for_march():
                utcTime.month==march
                return march
            def for_october():
                utcTime.month==october
                return october


            # print(for_year_month)
            ## off and on list first if Off and 1st elif On and  2nd elif On  3r elif off 4th elif on 5th elif -->
            if for_march() and utcTime.day<march_day:
                window_GUI_daylight_off()
            elif for_march() and utcTime.day> march_day:
                window_GUI_daylight_on()
            elif for_march() and utcTime.day == march_day and utcTime.hour >=2:
                window_GUI_daylight_on()
            elif for_march() and utcTime.day == march_day and utcTime.hour < 2:
                window_GUI_daylight_off()
            elif for_october() and utcTime.day < oct_day:
                window_GUI_daylight_on()
            elif for_october()  and utcTime.day>oct_day:
                window_GUI_daylight_off()
            elif for_october() and utcTime.day==oct_day and utcTime.hour >= 3:
                window_GUI_daylight_off()
            elif for_october() and utcTime.day==oct_day and utcTime.hour < 3:
                window_GUI_daylight_on()
            elif 4<=utcTime.month<=9:
                window_GUI_daylight_on()
            elif utcTime.month<3:
                window_GUI_daylight_off()
            elif utcTime.month >=11:
                window_GUI_daylight_off()

                # if utcTime.hour < 2 and utcTime.minute < 59:


                # elif utcTime.hour >= 2 and utcTime.minute > 1:
                    # daylight_on()


                # win32api.SetSystemTime(utcTime.year, utcTime.month, utcTime.weekday(), utcTime.day, utcTime.hour, utcTime.minute, utcTime.second, 0)
                # localTime = datetime.datetime.fromtimestamp(epoch_time)
                # print ("Time updated to: " + localTime.strftime("%d-%m-%Y %I:%M%p") + " from " + server)
                # win32api.SetSystemTime(utcTime.year, utcTime.month, utcTime.weekday(), utcTime.day, utcTime.hour, utcTime.minute, utcTime.second, 0)
                # localTime = datetime.datetime.fromtimestamp(epoch_time)
                # print ("Time updated to: " + localTime.strftime("%d-%m-%Y %I:%M%p") + " from " + server)


            # Local time is obtained using fromtimestamp()
            break
        else:
            print ("Could not find time from " + server)
window.mainloop()
