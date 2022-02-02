#Two child classes, separate attribs.

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