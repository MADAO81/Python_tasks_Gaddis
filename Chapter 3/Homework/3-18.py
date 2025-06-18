print("What kind of diet do your friends follow?")
vegan = str(input("Vegan: "))
vegetarian = str(input("Vegetarian: "))
gluten_free = str(input("Gluten free: "))

if vegan == "yes" and vegetarian == "yes" and gluten_free == "yes":
    print("Here's restaurants for you:")
    print("Chief's cuisine.")
    print("Cafe around the corner.")
elif vegan == "no" and vegetarian == "yes" and gluten_free == "yes":
    print("Here's restaurants for you:")
    print("Cafe around the corner.")
    print("Central pizzeria.")
    print("Chief's cuisine.")
    print("Italian mom's dishes.")
elif vegan == "no" and vegetarian == "no" and gluten_free == "yes":
    print("Here's restaurants for you:")
    print("Chief's cuisine.")
    print("Cafe around the corner.")
    print("Central pizzeria.")
    print("Italian mom's dishes.")
elif vegan == "no" and vegetarian == "yes" and gluten_free == "no":
    print("Here's restaurants for you:")
    print("Chief's cuisine.")
    print("Cafe around the corner.")
    print("Central pizzeria.")
elif vegan == "no" and vegetarian == "no" and gluten_free == "no":
    print("Here's restaurants for you:")
    print("Chief's cuisine.")
    print("Cafe around the corner.")
    print("Central pizzeria.")
    print("Italian mom's dishes.")
    print("Joe's hamburgers.")

  
  