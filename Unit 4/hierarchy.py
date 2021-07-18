
"""
Illustration of class hierarchy and polymorphism

We create a base class Adviser and two subclasses, Instructor and
Professor.
Each one has a custom version for advise().
"""

class Adviser(object):
    def __init__(self, name):
        self.name = name
        print("create Adviser name={}".format(name))

    def __str__(self):
        return "{}: name={}".format("Adviser", self.name)

    def advise(self, student):
        print("{} advises student {}".format(self, student))



class Instructor(Adviser):
    def __init__(self, name):
        # call the superclass constructor to initialize the object:
        # could do:   Adviser.__init__(self, name)
        #     OR:
        super().__init__(name)
        print("create Instructor name={}".format(name))

    def __str__(self):
        return "{}: name={}".format("Instructor", self.name)

    # overriden method:
    def advise(self, student):
        print("{} advises student {} with planning".format(self, student))


class Professor(Adviser):
    def __init__(self, name, adv_assign=0.1):
        # call the superclass constructor to initialize the object:
        Adviser.__init__(self, name)
        self.adv_asgn = adv_assign    # fraction of workload for advising
        print("create {}".format(self))

    def __str__(self):
        # to get the class name we can use self.__class__.__name__
        return "{}: name={} adv_assignment={}".format(self.__class__.__name__, self.name, self.adv_asgn)

    # overriden method:
    def advise(self, student):
        print("{} advises student {} with planning and research".format(self, student))


    
    
class Student(object):
    def __init__(self, name, startyear=2017):
        self.name = name
        self.start = startyear

    def __str__(self):
        return "Student: name={} start={}".format(self.name, self.start)

##############
alice = Adviser("Alice")
ian = Instructor("Ian")
peeta = Professor("Peeta")

sarah = Student("Sarah")
sam = Student("Sam")
santa = Student("Santa")

adv_lst = [alice, ian, peeta]
std_lst = [sarah, sam, santa]


def print_advisers(al):
    print("Our advisers:")
    for a in al:
        print(a)

def print_students(sl):
    print("Our students:")
    for s in sl:
        print(s)



def do_advising_session(al, sl):
    print("An advising session:")
    n = len(al)  # assume both lists have the same length
    # illustration of polymorphism: the right version of advise is called,
    #   depending on the class, determined at runtime.
    for i in range(0,n):
        al[i].advise(sl[i])

# getting read for advising:
print_advisers(adv_lst)
print_students(std_lst)
do_advising_session(adv_lst, std_lst)

