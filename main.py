from os import system, name 
import time
import datetime

##########
#23/12/2018#
##########

#####################################
#
#   Hotel Reservation Program 2018
#   This Script, provides a simulation of  hotel reservation.
#
#   Usage: 
#   
#   Firstly, you need to enter your plan dates.
#   After that, you can list available rooms.
#   Lastly you can calculate the cost of your holiday.
#   If user has a plan more than 9 day, nightly fee = 16
#
#####################################

def start (): # The start function, let's user to type into information about plan.
    global mode
    print """Welcome to Hotel Reservation App 2018.

    Press 1 to Enter Date of Your Plan.
    Press 2 to List Available Rooms.
    Press 3 to Checkout."""

    mode = raw_input("Make Your Decision: ")

def ask(): # ask function works like, would you like to go on or quit?
    question = raw_input('Press Enter to Restart, q for Quit ')
    if (question == "q"):
        quit()
    else:
        clear()
        start()

def listAvailableRooms(checkInDate, checkOutDate): # This function lists the available rooms, which are located in reserved.txt. If rooms in that file are full on users date, then they will not occur to user.
    roomList = []
    unavailableRooms = []
    availableRooms = []
    reserved = []
    roomDates = []
    roomCodes = []    
    
    with open("rooms.txt", "r") as roomFile:
        for line in roomFile:
            roomList.append(line.split())
            
    with open ("reserved.txt", 'r') as reservedRoomFile:
        for line in reservedRoomFile:
            reserved.append(line.split())

    for room in reserved:
        roomDates.append(room[1].split('/'))
        roomCodes.append(room[0])

    for roomIndex in range(0, len(reserved)):
        roomDate = roomDates[roomIndex]
        reservedRoomStartDay = roomDate[0]
        reservedRoomStartMonth = roomDate[1]
        reservedRoomStartYear = roomDate[2]
        
        reservedRoomStopDay = roomDate[3]
        reservedRoomStopMonth = roomDate[4]
        reservedRoomStopYear = roomDate[5]

        startDate = datetime.datetime(day=int(reservedRoomStartDay),month=int(reservedRoomStartMonth),year=int(reservedRoomStartYear))
        endDate = datetime.datetime(day=int(reservedRoomStopDay),month=int(reservedRoomStopMonth),year=int(reservedRoomStopYear))

        userCheckInDay = checkInDate[0]
        userCheckInMonth = checkInDate[1]
        userCheckInYear = checkInDate[2]

        userCheckOutDay = checkOutDate[0]
        userCheckOutMonth = checkOutDate[1]
        userCheckOutYear = checkOutDate[2]

        userCheckInDate = datetime.datetime(day=userCheckInDay,month=userCheckInMonth,year=userCheckInYear)
        userCheckOutDate = datetime.datetime(day=userCheckOutDay,month=userCheckOutMonth,year=userCheckOutYear)

        global delta
        delta = userCheckOutDate - userCheckInDate
        
        for i in range(delta.days + 1):
            userDays = (userCheckInDate + datetime.timedelta(i))
            if startDate <= userDays <= endDate:
                print "oo"
                unavailableRooms.append(reserved[roomIndex][0])                
##            else:
##                print "This room is available."


    for i in roomList:
        current = (list(set(i) -set(unavailableRooms)))
        availableRooms.append(current)
        
    for i in availableRooms:
        i.sort(key=lambda x:x[0:-1])
        print i
    return

def getDate(): # gets plan date from user, while loop for each date info.
    global startDay, startMonth, startYear, stopDay, stopMonth, stopYear
    
    while True:
        try:
            startDay = int(raw_input("Please Enter Start Day of Your Plan: "))
            if (startDay > 31):
                clear()
                raise ValueError
            print ("Done, Day of Your Plan is %d" %(startDay))
            time.sleep(0.6)
            clear()
            break
        except (ValueError):
            print "Something Went Wrong, Please Try Again."

    while True:
        try:
            startMonth = int(raw_input("Please Enter Start Month of Your Plan: "))
            if (startMonth > 12):
                clear()
                raise ValueError
            print ("Done, Month of Your Plan is %d" %(startMonth))
            time.sleep(0.6)
            clear()
            break
        except (ValueError):
            print "Something Went Wrong, Please Try Again."

    while True:
        try:
            startYear = int(raw_input("Please Enter Start Year of Your Plan: "))
            if (startYear > 2030 or startYear < 2018):
                clear()
                raise ValueError
            print ("Done, Year of Your Plan is %d" %(
                startYear))
            time.sleep(0.6)
            clear()
            break
        except (ValueError):
            print "Something Went Wrong, Please Try Again."

    while True:
        try:
            stopDay = int(raw_input("Please Enter End Day of Your Plan: "))
            if (stopDay > 31):
                clear()
                raise ValueError
            print ("Done, Day of Your Plan is %d" %(stopDay))
            time.sleep(1)
            clear()
            break
        except (ValueError):
            print "Something Went Wrong, Please Try Again."

    while True:
        try:
            stopMonth = int(raw_input("Please Enter End Month of Your Plan: "))
            if (stopMonth > 12):
                clear()
                raise ValueError
            print ("Done, Month of Your Plan is %d" %(stopMonth))
            time.sleep(1)
            clear()
            break
        except (ValueError):
            print "Something Went Wrong, Please Try Again."

    while True:
        try:
            stopYear = int(raw_input("Please Enter End Year of Your Plan: "))
            if (stopYear > 2030 or stopYear < 2018):
                clear()
                raise ValueError
            print ("Done, Year of Your Plan is %d" %(
                stopYear))
            time.sleep(1)
            clear()
            break
        except (ValueError):
            print "Something Went Wrong, Please Try Again."
    
    print ("Your Plan's Start Date is %d/%d/%d" %(startDay, startMonth, startYear))
    print ("Your Plan's Stop Date is %d/%d/%d" %(stopDay, stopMonth, stopYear))
    
    return

def checkout(): # provides information of total cost about the user's plan.
    day = delta.days

    if (day == 1):
        print 'Your Plan Takes 1 day'

    else:
        print 'Your Plan Takes %d days' %(day)
    
    if (day < 10):
        print '%d x 20$' %(day)
        print '     = %d$' %(day * 20)

    else:
        print '%d x 16$' %(day)
        print '     = %d$' %(day * 16)
        
    return

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux 
    else: 
        _ = system('clear') 

start()

##################################################
# 
# mode 1,
# calls getDate function, to learn plan date from user.
# 
# mode 2,
# calls listAvailableRooms function to list available rooms on users plan date.
#
# mode 3,
# calls function checkout to provide fee information.
#
##################################################

while True: # this loop runs until ask() function returns exit.
    if (mode == "1"):
        clear()      
        getDate()
        checkInDate = (startDay, startMonth, startYear)
        checkOutDate = (stopDay, stopMonth, stopYear)
        ask()

    elif (mode == "2"):
        clear()
        listAvailableRooms(checkInDate, checkOutDate)
        ask()

    elif (mode == "3"):
        clear()
        
        checkout()
        ask()

    else:
        print "Nothing found, Try Again."
        print ("Your Plan's Start Date is %d/%d/%d" %(startDay, startMonth, startYear))
        print ("Your Plan's Start Date is %d/%d/%d" %(stopDay, stopMonth, stopYear))
        ask()
