from math import acos
import random
import time
 
def abilitymodifiers():
    
    print ("Determining Ability Modifiers...")
    time.sleep(1)

    if int(s_strength) == (2, 3):
        str_am = -4
    if int(s_strength) == (4, 5):
        str_am = -3
    if int(s_strength) == (6, 7):
        str_am = -2
    if int(s_strength) == (8, 9):
        str_am = -1
    if int(s_strength) == (10, 11):
        str_am = 0
    if int(s_strength) == (12, 13):
        str_am = 1
    if int(s_strength) == (14, 15):
        str_am = 2
    if int(s_strength) == (16, 17):
        str_am = 3 
    if int(s_strength) == (18, 19):
        str_am = 4
    if int(s_strength) == (20, 21):
        str_am = 5

    if int(s_dexterity) == (2, 3):
        dex_am = -4
    if int(s_dexterity) == (4, 5):
        dex_am = -3
    if int(s_dexterity) == (6, 7):
        dex_am = -2
    if int(s_dexterity) == (8, 9):
        dex_am = -1
    if int(s_dexterity) == (10, 11):
        dex_am = 0
    if int(s_dexterity) == (12, 13):
        dex_am = 1
    if int(s_dexterity) == (14, 15):
        dex_am = 2
    if int(s_dexterity) == (16, 17):
        dex_am = 3 
    if int(s_dexterity) == (18, 19):
        dex_am = 4
    if int(s_dexterity) == (20, 21):
        dex_am = 5

    if int(s_constitution) == (2, 3):
        con_am = -4
    if int(s_constitution) == (4, 5):
        con_am = -3
    if int(s_constitution) == (6, 7):
        con_am = -2
    if int(s_constitution) == (8, 9):
        con_am = -1
    if int(s_constitution) == (10, 11):
        con_am = 0
    if int(s_constitution) == (12, 13):
        con_am = 1
    if int(s_constitution) == (14, 15):
        con_am = 2
    if int(s_constitution) == (16, 17):
        con_am = 3 
    if int(s_constitution) == (18, 19):
        con_am = 4
    if int(s_constitution) == (20, 21):
        con_am = 5

    if int(s_intel) == (2, 3):
        int_am = -4
    if int(s_intel) == (4, 5):
        int_am = -3
    if int(s_intel) == (6, 7):
        int_am = -2
    if int(s_intel) == (8, 9):
        int_am = -1
    if int(s_intel) == (10, 11):
        int_am = 0
    if int(s_intel) == (12, 13):
        int_am = 1
    if int(s_intel) == (14, 15):
        int_am = 2
    if int(s_intel) == (16, 17):
        int_am = 3 
    if int(s_intel) == (18, 19):
        int_am = 4
    if int(s_intel) == (20, 21):
        int_am = 5

    if int(s_wisdom) == (2, 3):
        wis_am = -4
    if int(s_wisdom) == (4, 5):
        wis_am = -3
    if int(s_wisdom) == (6, 7):
        wis_am = -2
    if int(s_wisdom) == (8, 9):
        wis_am = -1
    if int(s_wisdom) == (10, 11):
        wis_am = 0
    if int(s_wisdom) == (12, 13):
        wis_am = 1
    if int(s_wisdom) == (14, 15):
        wis_am = 2
    if int(s_wisdom) == (16, 17):
        wis_am = 3 
    if int(s_wisdom) == (18, 19):
        wis_am = 4
    if int(s_wisdom) == (20, 21):
        wis_am = 5

    if int(s_charisma) == (2, 3):
        char_am = -4
    if int(s_charisma) == (4, 5):
        char_am = -3
    if int(s_charisma) == (6, 7):
        char_am = -2
    if int(s_charisma) == (8, 9):
        char_am = -1
    if int(s_charisma) == (10, 11):
        char_am = 0
    if int(s_charisma) == (12, 13):
        char_am = 1
    if int(s_charisma) == (14, 15):
        char_am = 2
    if int(s_charisma) == (16, 17):
        char_am = 3 
    if int(s_charisma) == (18, 19):
        char_am = 4
    if int(s_charisma) == (20, 21):
        char_am = 5

    print ("Ability Modifiers Set!")
    print ("Strength:", str_am, "Dexterity:", dex_am, "Constitution:", con_am, "Intelligence:", int_am, "Wisdom:", wis_am, "Charisma:", char_am)

def abilityscores():

    global s_strength, s_dexterity, s_constitution, s_intel, s_wisdom, s_charisma
    rollorpick = input ("Do you want to roll or pick your ability scores?")
    if rollorpick == "r":
        print ("Rolling for stats...")
        time.sleep(1)
        a_stat1 = random.randrange(1, 6)
        a_stat2 = random.randrange(1, 6)
        a_stat3 = random.randrange(1, 6)
        a_stat4 = random.randrange(1, 6)
        a_statlist = [a_stat1, a_stat2, a_stat3, a_stat4]
        a_statlist.remove(min(a_statlist))
        a_stat=sum(a_statlist)
       
        b_stat1 = random.randrange(1, 6)
        b_stat2 = random.randrange(1, 6)
        b_stat3 = random.randrange(1, 6)
        b_stat4 = random.randrange(1, 6)
        b_statlist = [b_stat1, b_stat2, b_stat3, b_stat4]
        b_statlist.remove(min(b_statlist))
        b_stat=sum(b_statlist)
        
        c_stat1 = random.randrange(1, 6)
        c_stat2 = random.randrange(1, 6)
        c_stat3 = random.randrange(1, 6)
        c_stat4 = random.randrange(1, 6)
        c_statlist = [c_stat1, c_stat2, c_stat3, c_stat4]
        c_statlist.remove(min(c_statlist))
        c_stat=sum(c_statlist)
        
        d_stat1 = random.randrange(1, 6)
        d_stat2 = random.randrange(1, 6)
        d_stat3 = random.randrange(1, 6)
        d_stat4 = random.randrange(1, 6)
        d_statlist = [d_stat1, d_stat2, d_stat3, d_stat4]
        d_statlist.remove(min(d_statlist))
        d_stat=sum(d_statlist)
        
        e_stat1 = random.randrange(1, 6)
        e_stat2 = random.randrange(1, 6)
        e_stat3 = random.randrange(1, 6)
        e_stat4 = random.randrange(1, 6)
        e_statlist = [e_stat1, e_stat2, e_stat3, e_stat4]
        e_statlist.remove(min(e_statlist))
        e_stat=sum(e_statlist)

        f_stat1 = random.randrange(1,6)
        f_stat2 = random.randrange(1,6)
        f_stat3 = random.randrange(1,6)
        f_stat4 = random.randrange(1,6)
        f_statlist = [f_stat1, f_stat2, f_stat3, f_stat4]
        f_statlist.remove(min(f_statlist))
        f_stat=sum(f_statlist)

        statlist = [a_stat, b_stat, c_stat, e_stat, d_stat, f_stat]
        print (statlist)
        reroll = input ("Reroll?")
        if reroll == "y":
            abilityscores()
        
        print ("Do you want to assign your scores manually or use Auto Assign?")
        m_or_n = input ("Y(Manual) or N(Auto)?")
        if m_or_n == "y":
            print ("What stat number will you assign to Strength?")
            s_strength = input (statlist)
            if int(s_strength) in statlist:
                statlist.remove(int(s_strength))
            else:
                print ("Invalid stat number")
            print("What stat number will you assign to Dexterity?")
            s_dexterity = input (statlist)
            if int(s_dexterity) in statlist:
                statlist.remove(int(s_dexterity))
            else:
                print ("Invalid stat number")
            print ("What stat number will you assign to Constitution?")
            s_constitution = input (statlist)
            if int(s_constitution) in statlist:
                statlist.remove(int(s_constitution))
            else:
                print ("Invalid stat number")
            print ("What stat number will you assign to Intelligence?")
            s_intel = input (statlist)
            if int(s_intel) in statlist:
                statlist.remove(int(s_intel))
            else:
                print ("Invalid stat number")
            print ("What stat number will you assign to Wisdom?")
            s_wisdom = input (statlist)
            if int(s_wisdom) in statlist:
                statlist.remove(int(s_wisdom))
            else:
                print ("Invalid stat number")
            print ("What stat number will you apply to Charisma?")
            s_charisma = input (statlist)
            if int(s_charisma) in statlist:
                statlist.remove(int(s_charisma))
                abilitymodifiers()
            else:
                print ("Invalid stat number")


                    
def bground():
    
    global b_acolyte, b_charlatan, b_criminal, b_entertainer, b_folk_h, b_guild_a, b_hermit, b_noble, b_outlander, b_sage, b_sailor, b_soldier, b_urchin
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
    if c_fighter == "y":
        c_class = "Fighter"
        race()
    if c_fighter == "n":
        print ("Barbarian?")
        c_barbarian = input("Y or N?")
    if c_barbarian == "y":
        c_class = "Barbarian"
        race()
    if c_barbarian == "n":
        print ("Bard?")
        c_bard = input("Y or N?")
    if c_bard == "y":
        c_class = "Bard"
        race()
    if c_bard == "n":
        print ("Cleric?")
        c_cleric = input("Y or N?")
    if c_cleric == "y":
        c_class = "Cleric"
        race()
    if c_cleric == "n":
        print ("Druid?")
        c_druid = input("Y or N?")
    if c_druid == "y":
        c_class = "Druid"
        race()
    if c_druid == "n":
        print ("Monk?")
        c_monk = input("Y or N?")
    if c_monk == "y":
        c_class = "Monk"
        race()
    if c_monk == "n":
        print ("Paladin?")
        c_paladin = input("Y or N?")
    if c_paladin == "y":
        c_class = "Paladin"
        race()
    if c_paladin == "n":
        print ("Ranger?")
        c_ranger = input("Y or N?")
    if c_ranger == "y":
        c_class = "Ranger"
        race()
    if c_ranger == "n":
        print ("Rogue?")
        c_rogue = input("Y or N?")
    if c_rogue == "y":
        c_class = "Rogue"
        race()
    if c_rogue == "n":
        print ("Sorcerer?")
        c_sorcerer = input("Y or N?")
    if c_sorcerer == "y":
        c_class = "Sorcerer"
        race()
    if c_sorcerer == "n":
        print ("Warlock")
        c_warlock = input("Y or N?")
    if c_warlock == "y":
        c_class = "Warlock"
        race()
    if c_warlock == "n":
        print ("Wizard?")
        c_wizard = input("Y or N?")
    if c_wizard == "y":
        c_class = "Wizard"
        race()
    if c_wizard == "n":
        cclass()

def name():
    ch_name=input("What is your character's name?")
    print("So your character name is ", ch_name , "?")
    ch_name_c = input("Y or N?")
    if ch_name_c == "n":
        name()
    if ch_name_c == "y":
        cclass()

name()
