#An example of composition as an alternative to inheritance
#Example from learn python the hard way
#This is not a parent-child relationship expressed in a "is-a" manner
#This is a other-child relationship expressed in a "has-a" manner

class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit() # prints OTHER implicit()
son.override() # prints CHILD override()
son.altered()  # prints CHILD, BEFORE OTHER altered()
               #        OTHER altered()
               #        CHILD, AFTER OTHER altered()
