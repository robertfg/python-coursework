def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError
    return product_idea + "inator"
