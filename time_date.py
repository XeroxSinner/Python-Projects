from datetime import datetime
import pytz

PST = pytz.timezone('US/Pacific')
EST = pytz.timezone('US/Eastern')
GMT = pytz.timezone('GMT')

Portland = datetime.now(PST)
NewYork = datetime.now(EST)
London = datetime.now(GMT)


open = Portland.replace(hour=9, minute=0, second=0, microsecond=0)
close = Portland.replace(hour=17, minute=0, second=0, microsecond=0)

openY = NewYork.replace(hour=9, minute=0, second=0, microsecond=0)
closeY = NewYork.replace(hour=17, minute=0, second=0, microsecond=0)

openL = London.replace(hour=9, minute=0, second=0, microsecond=0)
closeL = London.replace(hour=17, minute=0, second=0, microsecond=0)

#Just putting this here to verify I'm getting correct times
print(Portland.strftime("Portland: " "%X " "%Z"))
print(NewYork.strftime("New York: " "%X " "%Z"))
print(London.strftime("London: " "%X " "%Z"))


if Portland > open and Portland < close:
    print("Portland is open.")
else:
    print("Portland is closed.")
    
if NewYork > openY and NewYork < closeY:
    print("New York is open.")
else:
    print("New York is closed.")

if London > openL and London < closeL:
    print("London is open.")
else:
    print("London is closed.")
    
    
    
## Possibly cleaner to convert all times to UTC and then >/< UTC?
## Also need to review iterating through string, cause this is ugly AF

##Replace function -

# def replace(location, hour, min, sec, mics):
#     open = location.replace(hour=hour, minute=min, second=sec, microsecond=mics)
#     close = location.replace(hour=17, minute=0, second=0, microsecond=0)
#     return close

# replace("Portland", )
    