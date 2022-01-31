

def getInfo():
    var1 = input("First numeric value: ")
    var2 = input("Second numeric value: ")
    compute(var1, var2)
    
    
def compute(var1, var2):
    try:
        var3 = int(var1) + int(var2)
        print("{} + {} = {}".format(var1, var2, var3))
    except ValueError:
        print("You didn't give number.")
    except:
        print("Oops, invalid. Closing.")

if __name__ == "__main__":
    getInfo() 