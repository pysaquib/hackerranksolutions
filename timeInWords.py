def timeInWords(h, m):
    inWords = ""
    hours = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    minutesIn = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    minutesPart = ["twenty", "thirty", "forty", "fifty"]

    if(m == 0):
        inWords = hours[h] + " o' clock"
    if(m > 0 and m <= 19 and m!=15):
        if(m==1):
            inWords = hours[m] + " minute past " + hours[h]
        else:
            inWords = hours[m] + " minutes past " + hours[h]
    if(m == 15):
        inWords = "quarter past " + hours[h]
    if(m > 19 and m < 30):
        mNew = str(m)
        mNew1 = int(mNew[0])
        mNew2 = int(mNew[1])
        inWords = minutesPart[mNew1-2] + " " + hours[mNew2] + " minutes past " + hours[h]
    if(m == 30):
        inWords = "half past " + hours[h]
    if(m > 30 and m < 60 and m!=45):
        mNew = 60 - m
        mNewx = str(mNew)
        mNew1 = int(mNewx[0])
        if(mNew<10):
            mNew2 = 0
        else:
            mNew2 = int(mNewx[1])
        if(mNew < 20):
            if(mNew == 1):
                inWords = hours[mNew] + " minute to " + hours[h+1]
            else:
                inWords = hours[mNew] + " minutes to " + hours[h+1]
        elif(mNew >= 20):
            inWords = minutesPart[mNew1-2] + " " + hours[mNew2] + " minutes to " + hours[h+1]
    if(m == 45):
        inWords = "quarter to "+hours[h+1]
    return inWords

h = int(input("Enter hour : "))
m = int(input("Enter minutes : "))

if(h > 0 and h <= 12 and m >= 0 and m < 60):
    print(timeInWords(h, m))
else:
    print("Wrong Input")
