import time
import winsound
import os


def set_alarm():
    print("Alarm Clock")
    print("1. Set alarm after X minutes")
    print("2. Set alarm at a particular time")

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        minutes = float(input("Enter the number of minutes until the alarm: "))
        seconds = minutes * 60
        print(f"Timer Set for {seconds} seconds.")
        while seconds > 0:
            print(f"Timer Time Left: {seconds}")
            time.sleep(1)
            seconds -= 1
            os.system("cls")
        play_alarm_sound()
    elif choice == "2":
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"Current Time is: {current_time}")
        alarm_time = input("Enter the alarm time in HH:MM format: ")
        print(f"Timer set for: {alarm_time}")
        while True:
            current_time = time.strftime("%H:%M")
            if current_time == alarm_time:
                play_alarm_sound()
                break
            time.sleep(1)
    else:
        print("Invalid input. Please enter 1 or 2.")


def play_alarm_sound():
    frequency = 2500
    duration = 3000
    winsound.Beep(frequency, duration)
    print("Alarm!")


set_alarm()
