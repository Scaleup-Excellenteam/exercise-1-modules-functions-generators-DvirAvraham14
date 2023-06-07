def get_recipe_price(prices, optionals=None, **ingredients):
    """
    Calculates the price of a recipe based on the prices of the ingredients.
    Args:
        prices: A dictionary containing the prices of the ingredients.
        optionals: A list of optional ingredients.
        **ingredients:  A dictionary containing the ingredients and their amounts.
    Returns:
        The function will return the price we have to pay for buying all the groceries.
    """
    total_price = 0

    # If no ingredients are provided, return 0
    if not ingredients:
        return total_price

    # Loop through all ingredients
    for ingredient, amount in ingredients.items():
        # Skip optional ingredients
        if optionals and ingredient in optionals:
            continue

        # Calculate the price of the ingredient based on its price per 100 grams
        price_per_100g = prices.get(ingredient, 0)
        price = price_per_100g * amount / 100

        # Add the price to the total price
        total_price += price

    return total_price


#test the function
if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))