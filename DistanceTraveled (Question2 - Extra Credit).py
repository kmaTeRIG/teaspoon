
speedString = input ("What is the speed?")
hoursTraveledString = input ("How many hours were traveled?")
speed = int(speedString)
hoursTraveled = int(hoursTraveledString)
hour = 1
while (hour <= hoursTraveled):
    print ("Hour: ", hour)
    print ("Distance Traveled: ", hour*speed)
    hour = hour +1

