#An example of overloading constructor methods in python using @classmethod
#MyData contains a data attribute that is a list of values
#This MyData class can be initialized from:
#	a list (using the standard __init__ method)
#	a file (using the .fromfilename method)
#	a dictionary (using the .fromdict method)


class MyData:
    def __init__(self, data):
        "Initialize MyData from a sequence"
        self.data = data
     
    @classmethod
    def fromfilename(cls, filename):
        "Initialize MyData from a file"
        data = open(filename).readlines()
        return cls(data)
     
    @classmethod
    def fromdict(cls, datadict):
        "Initialize MyData from a dict's items"
        return cls(datadict.items())

#Different ways to initialize the MyData class and still have the data attribute
print MyData([1,2,3]).data 
print MyData.fromfilename("/folder/foobar").data 
print MyData.fromdict({"spam":"ham"}).data