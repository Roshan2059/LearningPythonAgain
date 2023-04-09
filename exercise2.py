import time as t
time = t.strftime('%H:%M:%S')
hour = int(t.strftime('%H'))
mins = t.strftime('%M')
sec = t.strftime('%S')
if(hour > 0 and hour < 12):
    print("good morning")
elif(hour > 12 and hour < 16):
    print("Good afternoon")
elif(hour > 16 and hour < 19):
    print("Good evening")
else:
    print("good Night")