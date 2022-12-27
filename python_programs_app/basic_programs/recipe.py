# Dictionary to store the recipes
recipes = {
    "cake": ["flour", "sugar", "eggs"],
    "pizza": ["flour", "tomato sauce", "cheese"],
    "omelette": ["eggs", "milk"],
    "sandwich": ["bread", "cheese", "lettuce"],
}

# Function to search for a recipe by ingredient
def search_recipe(ingredient):
    # List to store the matching recipes
    matching_recipes = []

    # Loop through all the recipes
    for recipe, ingredients in recipes.items():
        # If the ingredient is present in the recipe, add it to the list
        if ingredient in ingredients:
            matching_recipes.append(recipe)

    # Return the list of matching recipes
    return matching_recipes

# Driver code
def main():
    # Prompt the user to enter an ingredient
    ingredient = input("Enter an ingredient: ")

    # Search for recipes with the given ingredient
    matching_recipes = search_recipe(ingredient)

    # Print the list of matching recipes
    print("Recipes with %s:" % ingredient)
    for recipe in matching_recipes:
        print(recipe)

# Call the main function
main()