#Two child classes, separate attribs.

#defines the parent class
class Media:
    name = ""
    upc = ""
    release = ""
    
class Music(Media):
    artist = ""
    format = ""
    
class Book(Media):
    author = ""
    publisher = ""