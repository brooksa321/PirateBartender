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

global your_drink
your_drink = {}

def check_YN(n):
    """Function to Verify user input is Y or N""" 
    while True:
        try:
            int(n)
            n = (raw_input("Please enter [y/n]"))
        except ValueError:
            break

    while True:
        if n.upper() == "Y" or n.upper() == "N":
            break
        else:
            n = (raw_input("Please enter [y/n]"))
        


def what_do_you_like():
    """Function to ask user about drink preferences"""
    for key in questions:
        n = (raw_input(questions[key]))
        n = n.upper()
        check_YN(n)
            
        if n == "Y":
            your_drink[key] = ingredients[key]
        else:
            continue


        print your_drink




what_do_you_like()

