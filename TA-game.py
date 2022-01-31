from PIL import Image

def start(nice=0,mean=0,name=""):
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    if name != "":
        print("\nThank you for playing again, {}. ".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat name? \n>>>").capitalize()
                if name != "":
                    print("\nHey, {}!".format(name))
                    print("\nSmall game to work through a few things. \nThere will be choices and a tally.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger is looking to chat. \nWill you be nice and chat a bit, \nor mean and walk? (N/M) \n>>").lower()
        if pick == "n":
            print("\nAaay, you've brightened someone's day.")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nAlright then.. scowls all around.")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name)
    
def show_score(nice,mean,name):
    print("\n{}, current totals: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))
    
def score(nice,mean,name):
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)
        
def win(nice,mean,name):
    print("Nice {}! \nYou're just so nice.".format(name))
    again(nice,mean,name)
    
def lose(nice,mean,name):
    img = Image.open(r"shit.png")
    img.show()
    print("\nWell, shoot. Aight then, {}, guess that's how it's going down, huh.".format(name))
    again(nice,mean,name)
    
def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nPlay again? (Y/N): \n>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nThanks anyhow!")
            stop = False
            quit()
        else:
            print("\n Use Y for Yes and N for No: \n>>")
            
def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)



if __name__ == "__main__":
    start()

