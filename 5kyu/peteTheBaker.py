    
def cakes(recipe, available):
    maxNumOfCakes = []
    for ingredient in recipe:
        if ingredient not in available:
            return 0
        maxNumOfCakes.append(available[ingredient] // recipe[ingredient])
    return min(maxNumOfCakes)

print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
