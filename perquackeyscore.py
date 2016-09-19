import time

print "Ready?"
print "Go"
points = 0
wordlist = []
starttime = time.time()
three = []
four = []
five = []
six = []
seven = []
eight = []
#Append the number after the "<=" in the following line to change the amount of time given. It's in seconds
while time.time() - starttime <= 180:
    word = str(raw_input("Word: "))
    wordcount = len(list(word))

    if word in wordlist:
        print "Sorry! That word has already been used"
    else:
        wordlist.append(word)
        if wordcount == 3:
            three.append(word)
            if len(three) == 1:
                points += 60
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(three) == 2:
                points += 70
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(three) == 3:
                points += 80
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(three) == 4:
                points += 90
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(three) == 5:
                points += 100
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(three) >= 5:
                print "Too many three letter words! No points awarded"
        elif wordcount == 4:
            four.append(word)
            if len(four) == 1:
                points += 120
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(four) == 2:
                points += 140
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(four) == 3:
                points += 160
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(four) == 4:
                points += 180
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(four) == 5:
                points += 200
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(four) >= 5:
                print "Too many four letter words! No points awarded"
        elif wordcount == 5:
            five.append(word)
            if len(five) == 1:
                points += 200
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(five) == 2:
                points += 250
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(five) == 3:
                points += 300
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(five) == 4:
                points += 350
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(five) == 5:
                points += 400
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(five) >= 5:
                print "Too many five letter words! No points awarded"
        elif wordcount == 6:
            six.append(word)
            if len(six) == 1:
                points += 300
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(six) == 2:
                points += 400
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(six) == 3:
                points += 500
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(six) == 4:
                points += 600
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(six) == 5:
                points += 700
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(six) >= 5:
                print "Too many three six letter words! No points awarded"
        elif wordcount == 7:
            seven.append(word)
            if len(seven) == 1:
                points += 500
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(seven) == 2:
                points += 650
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(seven) == 3:
                points += 800
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(seven) == 4:
                points += 950
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(seven) == 5:
                points += 1100
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(seven) >= 5:
                print "Too many seven letter words! No points awarded"
        elif wordcount >= 8:
            eight.append(word)
            if len(eight) == 1:
                points += 750
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(eight) == 2:
                points += 1000
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(eight) == 3:
                points += 1250
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(eight) == 4:
                points += 1500
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(eight) == 5:
                points += 1750
                print "Good! Current time is",time.time() - starttime,", and your current score is", points
            elif len(eight) >= 5:
                print "Too many eight letter words! No points awarded"
    worddump = []
print "Times up! Your score is ", points,". Your total words were",wordlist
