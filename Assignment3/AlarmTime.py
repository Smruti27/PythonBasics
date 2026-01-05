currentTime= int(input("Enter the current time in hours (0-23): "))
if currentTime < 0 or currentTime > 23:
    print("Invalid input. Please enter a value between 0 and 23.")
    exit()
hoursToWait= int(input("Enter the number of hours to wait: "))
alarmTime= (currentTime + hoursToWait) % 24
print("The alarm will go off at", alarmTime, "hours.")