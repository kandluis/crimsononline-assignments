#!/usr/bin/python

# code by Luis Perez

# modules
import random
import urllib
import json

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
        print "You passed in an empty string"
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
            
    # swapping the characters
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
    print won/trials
    return;

'''
' Problem 8: Harvard Shuttle Boy
'''           
def shuttleboy():
    import time
    url = "http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass%20Ave%20Garden%20St&output=json"
    json_data = urllib.urlopen(url)
    data = json.load(json_data)
    i = 0
    for trip in data:
        trip[u'departs'] = time.strptime(trip[u'departs'][11:],"%H:%M:%S")
        i += 1
    
    print "The next shuttle arrives at "
    

print("I love the Crimson tech department!")
