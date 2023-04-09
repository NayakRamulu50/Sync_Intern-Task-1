import datetime
import tkinter as tk
import winsound

def set_alarm():
    alarm_time = entry.get()
    alarm_hour = int(alarm_time[:2])
    alarm_minute = int(alarm_time[3:])
    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        if current_hour == alarm_hour and current_minute == alarm_minute:
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            print("Time's Up-----! Successfuly Completed \U0001F609")
            print("Set Another Time \U0001F610")
            break

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("300x150")

label = tk.Label(root, text="Enter the alarm time (24-hour format):", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

button = tk.Button(root, text="Set Alarm", font=("Arial", 12), command=set_alarm)
button.pack(pady=10)

root.mainloop()
