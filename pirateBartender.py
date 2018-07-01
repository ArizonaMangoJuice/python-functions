import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

result = {};

def styleofDrinks():
    for question in questions:
        typeOfDrink = input(questions[question] + "  ")
        if typeOfDrink == question or typeOfDrink == 'y' or typeOfDrink == 'yes':
            result[question] = ingredients.get(question)
    # print(result)
    constructDrink(result)
    # return result

def constructDrink(preference):
    drinkList = []
    
    for ingredient in preference:
        drink = random.choice(preference[ingredient])
        drinkList.append(drink)
        # print(random.choice(preference[ingredient]))
        
    print(drinkList)
    
    


    # print(questions[question])
if __name__ == '__main__':
    styleofDrinks()
    # constructDrink(ingredients)
