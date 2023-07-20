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
    found_foods = []
    for x in spicy_foods:
        found_foods.append(x.get("name"))
    return found_foods

def get_spiciest_foods(spicy_foods):
    found_foods = []
    for x in spicy_foods:
        if (x.get("heat_level") > 6):
            found_foods.append(x)
    return found_foods

def print_spicy_foods(spicy_foods):
    for x in spicy_foods:
        name = x.get("name")
        cuisine = x.get("cuisine")
        heat = x.get("heat_level") * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for x in spicy_foods:
        if (x.get("cuisine") == cuisine):
            return(x)

def print_spiciest_foods(spicy_foods):
    for x in spicy_foods:
        if (x.get("heat_level") > 5):
            name = x.get("name")
            cuisine = x.get("cuisine")
            heat = x.get("heat_level") * "🌶"
            print(f"{name} ({cuisine}) | Heat Level: {heat}")

def get_average_heat_level(spicy_foods):
    total_heat = 0
    for x in spicy_foods:
        total_heat += x.get("heat_level")
    return (total_heat/len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
