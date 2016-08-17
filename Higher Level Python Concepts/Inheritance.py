#Example from learn python the hard way
#Displays impicit inheritance and the ability to override

class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

#Instantiating the parent and child classes
dad = Parent() 
son = Child()

#Both dad.implicit() and son.implicit() will print the same message because son.implicit() is inherited from the parent class
dad.implicit() 
son.implicit() 

#dad.override() will print "PARENT override()", but son.override() will print "CHILD override()" because
#the methods of the child class take priority and override the inherited methods
dad.override()
son.override()

#using super will call the parent class's altered() method, resulting in "PARENT altered()" being printed
dad.altered()
son.altered()