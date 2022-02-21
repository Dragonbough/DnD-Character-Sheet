import random
def abilityscores():

    rollorpick = input ("Do you want to roll or pick your ability scores?")
    if rollorpick == ("pick, p"):
        print ("You may assign each of these numbers once to one of the abilities: 15,14,13,12,10,8")
    if rollorpick == ("roll", "r"):
        print ("Rolling for stats...")
        stat1 = random.randint(1, 6)
        stat2 = random.randint(1, 6)
        stat3 = random.randint(1, 6)
        stat4 = random.randint(1, 6)
        statlist = [stat1, stat2, stat3, stat4]
        droppedstat = min (statlist)
        print (droppedstat)

def bground():
    
    print ("What is your character's background?")
    print ("Acolyte?")
    b_acolyte = input ("Y or N?")
    if b_acolyte == "y":
        c_bground = "Acolyte"
        abilityscores()
    if b_acolyte == "n":
        print ("Charlatan?")
        b_charlatan = input ("Y or N?")
    if b_charlatan == "y":
        c_bground = "Charlatan"
        abilityscores()
    if b_charlatan == "n":
        print ("Criminal?")
        b_criminal = input ("Y or N?")
    if b_criminal == "y":
        c_bground = "Criminal"
        abilityscores()
    if b_criminal == "n":
        print ("Entertainer?")
        b_entertainer = input ("Y or N?")
    if b_entertainer == "y":
        c_bground = "Entertainer"
        abilityscores()
    if b_entertainer == "n":
        print ("Folk Hero?")
        b_folk_h = input ("Y or N?")
    if b_folk_h == "y":
        c_bground = "Folk Hero"
        abilityscores()
    if b_folk_h == "n":
        print ("Guild Artisan?")
        b_guild_a = input ("Y or N?")
    if b_guild_a == "y":
        c_bground = "Guild Artisan"
        abilityscores()
    if b_guild_a == "n":
        print ("Hermit?")
        b_hermit = input ("Y or N?")
    if b_hermit == "y":
        c_bground = "Hermit"
        abilityscores()
    if b_hermit == "n":
        print("Noble?")
        b_noble = input ("Y or N?")
    if b_noble == "y":
        c_bground = "Noble"
        abilityscores()
    if b_noble == "n":
        print("Outlander?")
        b_outlander = input ("Y or N?")
    if b_outlander == "y":
        c_bground = "Outlander"
        abilityscores()
    if b_outlander == "n":
        print ("Sage?")
        b_sage = input ("Y or N?")
    if b_sage == "y":
        c_bground = "Sage"
        abilityscores()
    if b_sage == "n":
        print ("Sailor?")
        b_sailor = input ("Y or N?")
    if b_sailor == "y":
        c_bground = "Sailor"
        abilityscores()
    if b_sailor == "n":
        print ("Soldier?")
        b_soldier = input ("Y or N?")
    if b_soldier == "y":
        c_bground = "Soldier"
        abilityscores()
    if b_soldier == "n":
        print ("Urchin?")
        b_urchin = input ("Y or N?")
    if b_urchin == "y":
        c_bground = "Urchin"
        abilityscores()
    if b_urchin == "n":
        bground() 

def race():

    print ("What is your character's race?")
    print ("Human?")
    r_human = input ("Y or N?")
    if r_human == "y":
        c_race = "Human"
        bground()
    if r_human == "n":
        print ("Dragonborne?")
        r_dragonborne = input ("Y or N?")
    if r_dragonborne == "y":
        c_race = "Dragonborn"
        bground()
    if r_dragonborne == "n":
        print ("Dwarf?")
        r_dwarf = input ("Y or N?")
    if r_dwarf == "y":
        c_race = "Dwarf"
        bground()
    if r_dwarf == "n":
        print ("Elf?")
        r_elf = input ("Y or N?")
    if r_elf == "y":
        c_race = "Elf"
        bground()
    if r_elf == "n":
        print ("Gnome")
        r_gnome = input ("Y or N?")
    if r_gnome == "y":
        c_race = "Gnome"
        bground()
    if r_gnome == "n":
        print ("Half-Elf?")
        r_h_elf = input ("Y or N?")
    if r_h_elf == "y":
        c_race = "Half-Elf"
        bground()
    if r_h_elf == "n":
       print ("Halfling?")
       r_halfling = input ("Y or N?")
    if r_halfling == "y":
       c_race = "Halfling"
       bground()
    if r_halfling == "n":
        print ("Half-Orc")
        r_h_orc = input ("Y or N?")
    if r_h_orc == "y":
        c_race = "Half-Orc"
        bground()
    if r_h_orc == "n":
        print ("Tiefling")
        r_tiefling = input ("Y or N?")
        if r_tiefling == "y":
        c_race = "Tiefling"
        bground()
    if r_tiefling == "n":
        race()

def cclass():
    
    print("What is your character's class?")
    print ("Fighter?")
    c_fighter = input("Y or N?")
    if c_fighter == "n":
        print ("Barbarian?")
        c_barbarian = input("Y or N?")
        if c_barbarian == "n":
            print ("Bard?")
            c_bard = input("Y or N?")
            if c_bard == "n":
                print ("Cleric?")
                c_cleric = input("Y or N?")
                if c_cleric == "n":
                    print ("Druid?")
                    c_druid = input("Y or N?")
                    if c_druid == "n":
                        print ("Monk?")
                        c_monk = input("Y or N?")
                        if c_monk == "n":
                            print ("Paladin?")
                            c_paladin = input("Y or N?")
                            if c_paladin == "n":
                                print ("Ranger?")
                                c_ranger = input("Y or N?")
                                if c_ranger == "n":
                                    print ("Rogue?")
                                    c_rogue = input("Y or N?")
                                    if c_rogue == "n":
                                        print ("Sorcerer?")
                                        c_sorcerer = input("Y or N?")
                                        if c_sorcerer == "n":
                                            print ("Warlock")
                                            c_warlock = input("Y or N?")
                                            if c_warlock == "n":
                                                print ("Wizard?")
                                                c_wizard = input("Y or N?")
                                                if c_wizard == "n":
                                                    cclass()
    if c_fighter == "y":
        c_class = "Fighter"
        race()
    if c_barbarian == "y":
        c_class = "Barbarian"
        race()
    if c_bard == "y":
        c_class = "Bard"
        race()
    if c_cleric == "y":
        c_class = "Cleric"
        race()
    if c_druid == "y":
        c_class = "Druid"
        race()
    if c_monk == "y":
        c_class = "Monk"
        race()
    if c_paladin == "y":
        c_class = "Paladin"
        race()
    if c_ranger == "y":
        c_class = "Ranger"
        race()
    if c_rogue == "y":
        c_class = "Rogue"
        race()
    if c_sorcerer == "y":
        c_class = "Sorcerer"
        race()
    if c_warlock == "y":
        c_class = "Warlock"
        race()
    if c_wizard == "y":
        c_class = "Wizard"
        race()

def name():
    ch_name=input("What is your character's name?")
    print("So your character name is ", ch_name , "?")
    ch_name_c = input("Y or N?")
    if ch_name_c == "n":
        name()
    if ch_name_c == "y":
        cclass()

name()





                
                                 
    
    
    
        
    
        

    
    
 

