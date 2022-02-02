#Two child classes, separate attribs.
#Add method to parent class - "Both child classes should utilize polymorphism on the parent class method."

#defines the parent class
class Media:
    name = ""
    upc = ""
    release = ""

#defines first child class & attributes    
class Music(Media):
    artist = ""
    format = ""


#defines second child class & attributes    
class Book(Media):
    author = ""
    publisher = ""