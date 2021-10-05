import notify2
import os
from playsound import playsound
import time


def clear():
    os.system("clear")

def inputData():
    # Function to gather the information for a pomodoro run

    # Initialize the checks for the input
    inputTimePomodoro = False
    inputTimeShortPause = False
    inputTimeLongPause = False
    inputNumPomodoro = False

    # Gather the information
    while not inputNumPomodoro:
        clear()
        try:
            numPomodoro = int(input("Please insert the number of Pomodoros you want to work as int: "))
            inputNumPomodoro = True
        except:
            pass

    while not inputTimePomodoro:
        clear()
        try:
            timePomodoro = int(input("Please insert the time for a Pomodoro in minutes as int: "))
            inputTimePomodoro = True
        except:
            pass


    while not inputTimeShortPause:
        clear()
        try:
            timeShortPause = int(input("Please insert the time for a short pause in minutes as int: "))
            inputTimeShortPause = True
        except:
            pass

    while not inputTimeLongPause:
        clear()
        try:
            timeLongPause = int(input("Please insert the time for a long pause in minutes as int: "))
            inputTimeLongPause = True
            clear()
        except:
            pass
    return numPomodoro, timePomodoro, timeShortPause, timeLongPause


if __name__ == "__main__":
    numPomodoro, timePomodoro, timeShortPause, timeLongPause = inputData()
    numPomodoroDone = 0
    while numPomodoro != 0:
        timeCountDownPomodoro = timePomodoro*60
        if numPomodoro > 1:
            strNumTimePomodoro = str(timePomodoro)+" minutes to Work! "+str(numPomodoro) +" Pomodoros left!"
        else:
            strNumTimePomodoro = str(timePomodoro)+" minutes to Work! "+str(numPomodoro) +" Pomodoro left!"

        notify2.init('Pomodoro')
        n = notify2.Notification("Work!",
                                     strNumTimePomodoro,
                                     "notification-message-im"   # Icon name
                                    )
        n.show()

        playsound("Oxygen-Sys-App-Message.ogg")

        while timeCountDownPomodoro != 0:


            minutes = int(timeCountDownPomodoro / 60)
            seconds = timeCountDownPomodoro % 60
            if seconds == 0:
                seconds = "00"
            if isinstance(seconds, int) and seconds < 10 and seconds > 0:
                seconds = "0"+str(seconds)
            clear()
            print("To quit press ctrl+c\nTime in Pomodoro left:\n")
            print(minutes, ":", seconds)
            time.sleep(1)
            timeCountDownPomodoro -= 1
        numPomodoro -= 1
        numPomodoroDone += 1
        if numPomodoro == 0:
            clear()
            if numPomodoroDone*timePomodoro == 1:

                notify2.init('Pomodoro')
                n = notify2.Notification("Done!",
                                         "You worked for " + str(numPomodoroDone*timePomodoro)+" minute!",
                                         "notification-message-im"   # Icon name
                                        )
                n.show()

                playsound("Oxygen-Sys-App-Message.ogg")

            else:
                notify2.init('Pomodoro')
                n = notify2.Notification("Done!",
                                         "You worked for " + str(numPomodoroDone*timePomodoro)+" minutes!",
                                         "notification-message-im"   # Icon name
                                        )
                n.show()

                playsound("Oxygen-Sys-App-Message.ogg")
            break
        if numPomodoroDone % 4 == 0:
            notify2.init('Pomodoro')
            n = notify2.Notification("Pause!",
                                     "Long pause! "+str(timeLongPause)+" minutes to relax!",
                                     "notification-message-im"   # Icon name
                                    )
            n.show()

            playsound("Oxygen-Sys-App-Message.ogg")
            timeLongPauseCounter = timeLongPause*60
            while timeLongPauseCounter != 0:
                minutes = int(timeLongPauseCounter / 60)
                seconds = timeLongPauseCounter % 60
                if seconds == 0:
                    seconds = "00"
                if isinstance(seconds, int) and seconds < 10 and seconds > 0:
                    seconds = "0"+str(seconds)
                clear()

                print("To quit press ctrl+c\nTime in long pause left:\n")
                print(minutes, ":", seconds)
                timeLongPauseCounter -= 1
                time.sleep(1)
        else:
            notify2.init('Pomodoro')
            n = notify2.Notification("Pause!",
                                     "Short pause! "+str(timeShortPause)+" minutes to relax!",
                                     "notification-message-im"   # Icon name
                                    )
            n.show()

            playsound("Oxygen-Sys-App-Message.ogg")
            timeShortPauseCounter = timeShortPause*60
            while timeShortPauseCounter != 0:
                minutes = int(timeShortPauseCounter / 60)
                seconds = timeShortPauseCounter % 60
                if seconds == 0:
                    seconds = "00"
                if isinstance(seconds, int) and seconds < 10 and seconds > 0:
                    seconds = "0"+str(seconds)
                clear()

                print("To quit press ctrl+c\nTime in short pause left:\n")
                print(minutes, ":", seconds)
                timeShortPauseCounter -= 1
                time.sleep(1)
