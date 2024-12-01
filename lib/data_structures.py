spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
     names_of_spicy = []
     
     for food in spicy_foods:
        names_of_spicy.append(food['name'])

     return(names_of_spicy)

def get_spiciest_foods(spicy_foods):
    spiciest = []  
    for food in spicy_foods:
        if 'heat_level' in food and food['heat_level'] > 5:
            spiciest.append(food)  
    return spiciest  



def print_spicy_foods(spicy_foods):
    # Loop through each food in the spicy_foods list
    for food in spicy_foods:
        # Get the name, cuisine, and heat level
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        
        # Generate the correct number of 🌶 emojis based on heat_level
        chili_emojis = "🌶" * heat_level
        
        # Print the food in the desired format
        print(f"{name} ({cuisine}) | Heat Level: {chili_emojis}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Iterate through each food in the list of spicy foods
    for food in spicy_foods:
        # If the cuisine matches, return the food dictionary
        if food["cuisine"] == cuisine:
            return food
    # Return None if no match is found
    return None

    pass

def print_spiciest_foods(spicy_foods):
     
     for food in spicy_foods:

         name = food["name"]
         cuisine = food["cuisine"]
         heat_level = food["heat_level"]

         chili_emojis = "🌶" * heat_level

         if 'heat_level' in food and food['heat_level'] > 5:
           print(f"{name} ({cuisine}) | Heat Level: {chili_emojis}") 
    

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    num_foods = len(spicy_foods)

    return total_heat // num_foods if num_foods > 0 else 0
    

def create_spicy_food(spicy_foods, spicy_food):
   spicy_foods.append(spicy_food)
    
    # Return the updated list
   return spicy_foods

