import ap

def print_app2():
    name = (__name__)
    return name

if __name__ == "__main__":
    print("I am running code from {} ".format(print_app2()))
    print("I am running code from {} ".format(ap.print_app()))  
    