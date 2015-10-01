import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

###Setting global drink variable
global your_drink
your_drink = {}


def check_YN(n):
    """Function to Verify user input is valid""" 
    
    ### Ensures the value entered is not an integer or float
    while True:
        try:
            int(n)
            n = (raw_input("Please enter [y/n]"))
        except ValueError:
            break
    ### Ensures the input is valid and capitalizes for uniformity
    while True:
        if n.upper() == "Y" or "YES" or "N" or "No":
            break
        else:
            n = (raw_input("Please enter [y/n]"))
        


def what_do_you_like():
    """Function to ask user about drink preferences"""
    ### Asks each question listed in questions dictionary
    for key in questions:
        n = (raw_input(questions[key]))
        n = n.upper()
        check_YN(n)
        
        ### Assigns ingregient value a Boolean depending on user answer    
        if n == "Y":
            your_drink[key] = True
        else:
            your_drink[key] = False



def drink_maker():
    """Function to construct drink from questions asked"""
    mixed_drink = []
    
###  Checks drink selection dictionary for users desired drink attributes, 
###  Selects one ingredient at random from desired category
###  and appends ingredient to drink list. 
    
    for key in your_drink:
        if your_drink[key] == True:
            mixed_drink.append(random.choice(ingredients[key]))
        else:
            continue
    
    ### Convert list to string
    drink = '\n'.join(mixed_drink) 
    
    print"Here is what you should put in your drink!!!"
    print drink





what_do_you_like()

drink_maker()

