import time


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

        # print("Sto")
        print(time_sec)


# num = int(input("Set Your Timer in sec : "))
print("The count down begins\n")
countdown(60)
