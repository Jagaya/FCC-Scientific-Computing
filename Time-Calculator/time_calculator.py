def add_time(start, duration, day=""):
    hour = int(start.split()[0].split(":")[0])
    minute = int(start.split()[0].split(":")[1])
    time = start.split()[1]
    
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    passH = int(duration.split(":")[0])
    passM = int(duration.split(":")[1])
    passD = 0

    minute += passM
    hour += passH + minute//60
    minute = minute %60

    while hour >= 12:
        if time == "AM":
            hour -= 12
            time = "PM"
        else:
            hour -=12
            passD += 1
            time = "AM"
    if hour == 0:
        hour = 12
            
    if day:
        day = day.casefold().capitalize()
        day = ", " + week[ (week.index(day) + passD)%7]
        
    new_time = str(hour) + ":" + "0"*(minute<10) + str(minute) + " " + time + day
    
    if passD > 0:
        if passD == 1:
            new_time += " (next day)"
        else:
            new_time += " (" + str(passD) + " days later)"

    return new_time