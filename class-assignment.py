#Two child classes, separate attribs.
#Add method to parent class - "Both child classes should utilize polymorphism on the parent class method."

#defines the parent class
class Media:
    name = "Media Name Goes Here"
    upc = "35416548"
    release = "02/02/22"
    
    def getName(self):
        msg = "\nMedia name: {}.".format(self.name)
        return msg
    
    #basic method that pulls name into var

#defines first child class & attributes    
class Music(Media):
    artist = "Nine Inch Nails"
    format = "vinyl"
    
    def getName(self):
        msg = "\nArtist name: {}.".format(self.artist)
        return msg

    #modify method to pull artist


#defines second child class & attributes    
class Book(Media):
    author = "Some Author"
    publisher = "Book co"
    
    def getName(self):
        msg = "\nAuthor name: {}.".format(self.author)
        return msg
    #modufy method to pull author
    
if __name__ == "__main__":
    media = Media()
    print(media.getName())
    music = Music()
    print(music.getName())
    book = Book()
    print(book.getName())


