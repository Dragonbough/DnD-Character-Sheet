
def race():

    print ("What is your character's race?")
    print ("Human?")
    r_human=input ("Y or N?")
    if r_human == "n":
        print ("Dragonborne?")
        r_dragonborne=input ("Y or N?")
        if r_dragonborne == "n":
            print ("Dwarf")


def cclass():

    print("What is your character's class?")
    print ("Fighter?")
    c_fighter=input("Y or N?")
    if c_fighter == "n":
        print ("Barbarian?")
        c_barbarian=input("Y or N?")
        if c_barbarian == "n":
            print ("Bard?")
            c_bard=input("Y or N?")
            if c_bard == "n":
                print ("Cleric?")
                c_cleric=input("Y or N?")
                if c_cleric == "n":
                    print ("Druid?")
                    c_druid=input("Y or N?")
                    if c_druid == "n":
                        print ("Monk?")
                        c_monk=input("Y or N?")
                        if c_monk == "n":
                            print ("Paladin?")
                            c_paladin=input("Y or N?")
                            if c_paladin == "n":
                                print ("Ranger?")
                                c_ranger=input("Y or N?")
                                if c_ranger == "n":
                                    print ("Rogue?")
                                    c_rogue=input("Y or N?")
                                    if c_rogue == "n":
                                        print ("Sorcerer?")
                                        c_sorcerer=input("Y or N?")
                                        if c_sorcerer == "n":
                                            print ("Warlock")
                                            c_warlock=input("Y or N?")
                                            if c_warlock == "n":
                                                print ("Wizard?")
                                                c_wizard=input("Y or N?")
                                                if c_wizard == "n":
                                                    cclass()
    if c_fighter == "y":
        cclass == "fighter"
        race()
    if c_barbarian == "y":
        cclass == "barbarian"
        race()
    if c_bard == "y":
        cclass == "bard"
        race()
    if c_cleric == "y":
        cclass == "cleric"
        race()
    if c_druid == "y":
        cclass == "druid"
        race()
    if c_monk == "y":
        cclass == "monk"
        race()
    if c_paladin == "y":
        cclass == "paladin"
        race()
    if c_ranger == "y":
        cclass == "ranger"
        race()
    if c_rogue == "y":
        cclass == "rogue"
        race()
    if c_sorcerer == "y":
        cclass == "sorcerer"
        race()
    if c_warlock == "y":
        cclass == "warlock"
        race()
    if c_wizard == "y":
        cclass == "wizard"
        race()

def name():
    ch_name=input("What is your character's name?")
    print("So your character name is ", ch_name , "?")
    ch_name_c=input("Y or N?")
    if ch_name_c == "n":
        name()
    if ch_name_c == "y":
        cclass()

name()





                
                                 
    
    
    
        
    
        

    
    
 

