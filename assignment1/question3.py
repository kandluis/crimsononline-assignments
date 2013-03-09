"""question 3

a)  Implement classes representing people and buildings. People should support
    name and gender, seamlessly verifying that gender is either M or F (if it
    isn't, what's the best way to inform the calling code that a mistake was
    made?) and enforcing capitalization of both first name and last name.

b)  Buildings should support a function enter that takes a person and a room
    number. The building should then keep track of anyone who enters/leaves the
    building and respond to some type of where_is(person) query with the room
    number that person is in. Ensure, naturally, that no one can be in more
    than one building at a time.

c)  Make the building class iterable over the people in it. That is, make it
    possible to write a for loop of the form:
        for person in building:
            ...

d)  Implement a class that represents an office building, an object that
    behaves the same as a building but only allows people to enter if they are
    on a list of employees passed in when the OfficeBuilding is instantiated.
    You may want to look up the super function in the Python documentation
    concerning classes.

e)  Implement a class that represents a house. The House class should implement
    enter to take only a Person object, and the House class should not support
    where_is at all. It should instead support at_home(Person), a function that
    returns a Boolean.

f)  Modify all buildings, houses included, to remember their location as an
    (x, y) tuple. Then make it possible to call some function that takes such
    a tuple and returns the building object at that tuple or None if no
    building exists at that location. You may choose whether any given location
    can only hold one building or multiple buildings, but you need to handle
    this corner case in some logical fashion.

g)  With a minimum of code duplication, modify the Building class so that
    bldg[roomnumber] = person accomplishes the same thing as
    bldg.enter(person, roomnumber). Be careful with how you do this if you
    chose to inherit any classes from Building (which you should have).
"""

locations = {}

def find((x,y)):
    if locations.has_key((x,y)):
        return locations[(x,y)]
    else:
        None
        
def add(building,(x,y)):
    if locations.has_key((x,y)):
        print("There's a building already there!")
        find((x,y))
        return False
    else:
        locations[(x,y)] = building
        return True

class Person(object):
    def __init__(self,name,gender):
        import string
        self.name = string.capwords(name)
        if gender == "M" or gender == "F" or gender == "m" or gender == "f":
            self.gender = gender.capitalize()
        else:
            raise ValueError("Gender should be \"F\" or \"M\"")

        # keeps track of people so they can't be in multiple buildings
        self.in_building = False
        self.room = None
        self.building = None

        print("New person created.\nName: {}\nGender: {}".format(self.name,self.gender))

            
class Building(object):
    def __init__(self,name,(x,y)):
        if add(self,(x,y)):
            self.rooms = {}
            self.count = 0
            self.location = (x,y)
            self.name = "Building: " + name
            print("New building constructed. {}".format(self.name))
        else:
            return;

    def enter(self, person, room_no):
        if self.rooms.has_key(room_no):
            print("{} is already in that room.".format(self.rooms[room_no].name))
        elif person.in_building:
            print("{} is already in {}.".format(person.name,person.building))
        else:
            self.rooms[room_no] = person
            self.count += 1
            person.building = self.name
            person.room = room_no
            person.in_building = True
            print("{} has entered into room {}".format(person.name,person.room))

    def where_is(self, person):
        if self.rooms.has_key(person.room):
            print("{} is in room {}.".format(person.name,person.room))
        elif person.in_building:
            print("{} is in {}.".format(person.name,person.building))
        else:
            print("{} is not in any building.".format(person.name))

    def exit(self,person):
        if self.rooms.has_key(person.room):
            # removing the person
            self.rooms.pop(person.room,None)
            self.count -= 1
            person.in_building = False
            person.bulding = None
            person.room = None
            
        return where_is(self,person)

    # making the class iterable 
    def __iter__(self):
        self.current = 0
        return self

    def next(self):
        if self.current >= self.count:
            raise StopIteration
        else:
            self.current += 1
            return self.rooms[self.rooms.keys()[self.current-1]]

    # making the class array-like, bldg[person] = bldgn.enter(person)
    def __setitem__(self,room_no,person):
        self.enter(person,room_no)

class Office(Building):

    def __init__(self,name,employees,(x,y)):
        super(Office,self).__init__(self.name,(x,y))
        import string
        self.employees = [employee.capitalize() for employee in employees]

    def enter(self, person, room_no):
        if person.name in self.employees:
            super(Office,self).enter(person,room_no)
        else:
            print("{} is not an employee at {}".format(person.name,self.name))
        
class House(Building):
    def __init__(self,name,(x,y)):
        super(House,self).__init__(self.name,(x,y))
        self.family = []
        
    def enter(self,person):
        self.family.append(person)
        person.building = "Home"
        person.in_building = True

    def at_home(self,person):
        return (person in self.family)

    # overriding it. Not sure how to "uninherit"
    def where_is(self):
        print("Did you mean \"at_home\"")

    # since enter is different, need to rewrite exit
    def exit(self,person):
        if person in self.family:
            # removing the person
            self.family.remove(person)
            self.count -= 1
            person.in_building = False
            person.bulding = None
        else:
            print("Wrong home?")

    # since enter is different, the "next" method for iterating is different
    def next(self):
        if self.current >= self.count:
            raise StopIteration
        else:
            self.current += 1
            return self.family[self.current-1]
        
    # overriding the "__setitem__"
    def __setitem__(self,key,person):
        self.enter(person)
