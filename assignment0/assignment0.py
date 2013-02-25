#!/usr/bin/python

# code by Luis Perez

# Problem 1 - Complete

'''
' Problem 2 - coding of the FuzzBizz problem found here:
' http://www.codinghorror.com/blog/2007/02/why-cant-programmers-program.html
'''
def fuzzbizz ():
    i = 1;
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0 :
            value = 'FuzzBizz'
        elif i % 3 == 0 :
            value = 'Fuzz'
        elif i % 5 == 0 :
            value = 'Bizz'
        else :
            value = i
        print value
        i = i + 1
    return;

'''
' Problem 3 : Functions that swaps the most common and least common
' characters in a string
' Theres probaly a better way. .isalpha() and .count() would have come in useful
'''
def swapchars (string):
    # counting the characters
    count = {}
    for letter in string:
       if letter == " ":
           continue
       if count.has_key(letter):
        count[letter] += 1
       else:
        count[letter] = 1

    # error checking
    if len(count) == 0:
        print "You passed in an letter-less string"
        return;

    # looking for the mininum and maximum
    min = len(string)
    max = 0
    for key in count:
        if count[key] > max:
            c_letter = key
            max = count[key]
        if count[key] < min:
            l_letter = key
            min = count[key]

    # swapping the characters (had to make a new string :( )
    new = ""
    for letter in string:
        if letter == c_letter:
            new += l_letter
        elif letter == l_letter:
            new += c_letter
        else:
            new += letter
    print new

    # all done
    return;

'''
' Problem 4: Functions that concatenates strings
'''
def sortcat (num, *strings):

    # sorting input and concatenating
    length = len(strings);
    sorted_strings = sorted(strings, key = len, reverse=True)

    # error checking
    if num < -1 or num > length:
        print "Incorrect usage"
        return;

    print "".join(sorted_strings[0:num])
    return;

'''
' Problem 5: Look Away Simulation
'''

def lookaway (trials):
    import random
    if trials < 0:
        print "Improper trial number."
        return;
    else:
        trial = trials

    # 0 is symbolic for looking ahead (ie, loosing)
    won = 0
    while trial > 0:

        # the game
        mario = True
        warrio = True
        peach = True
        games = 0
        while (games < 5):
            if mario or warrio or peach:
                mario = False if random.randint(0,5) == 0 else mario
                warrio = False if random.randint(0,5) == 0 else warrio
                peach = False if random.randint(0,5) == 0 else peach
            else:
                won += 1
                break
            games += 1

        trial -= 1

    # all done
    print "Luigi won " + str(won) + " times out of " + str(trials) + " games"
    return;

'''
' Problem 8: Harvard Shuttle Boy (done in a few minutes cuz I ran out of time)
'''
def shuttleboy():
    import time
    import urllib
    import json
    url = "http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass%20Ave%20Garden%20St&output=json"
    json_data = urllib.urlopen(url)
    data = json.load(json_data)
    now = time.mktime(time.localtime())
    times = {}
    i = 0
    for trip in data:
        time_string = trip[u'departs'][0:10] + " " + trip[u'departs'][11:]
        depart = time.mktime(time.strptime(time_string,"%Y-%m-%d %H:%M:%S"))
        times[i+1] = round((depart - now)/60)
        times[i+2] = (depart - now) % 60
        times[i] = time_string[11:16]
        i = i + 3

    print "Today is " + time.asctime() + ".\n\n"
    i = 0
    while i < 9:
        var = "The next shuttle" if i == 0 else "There's another that"
        print var + " arrives at " + str(times[i]) + " (in about " + str(times[i+1]) + " minutes and " + str(times[i+2]) + " seconds).\n"
        i = i + 3
    return;
print("I love the Crimson tech department! All done! Woooooooooooot")
