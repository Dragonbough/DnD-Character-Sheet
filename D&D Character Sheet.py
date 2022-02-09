def name():
    ch_name=input("What is your character's name?")
    print("So your character name is ", ch_name , "?")
    ch_name_c=input("Y or N?")
    if ch_name_c == "n" or " n":
        name()
    if ch_name_c == "y" or " y":
        cclass()

name()

def cclass():
    print("What is your character's class?")
    print ("Fighter?")
    c_fighter=input("Y or N?")
    if c_fighter == "n" or " n":
        print ("Barbarian")
        c_barbarian=input("Y or N?")
    
        
    
        

    
    
 

