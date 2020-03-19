#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  increaseList = []
  check = [AskFor for AskFor in recipe.keys()]
  Have = [have for have in ingredients.keys()]
  for (Recipekey,RecipeValue), (IngredientKey2,IngredientValue2) in zip(recipe.items(), ingredients.items()):
    if(IngredientValue2 <  RecipeValue ):
      return 0
    elif (len(check) != len(Have)):
      return 0
    else:
      increaseList.append(IngredientValue2//RecipeValue)
  minasdf = min(increaseList)
  return minasdf


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
  print(recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10}, {'milk': 198, 'butter': 52, 'cheese': 10}))