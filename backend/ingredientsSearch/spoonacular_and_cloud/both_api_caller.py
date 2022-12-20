import sys

from both_api import both_api

# An example of a call to both Google Cloud Vision API and Spoonacular API
image_url = 'https://bigoven-res.cloudinary.com/image/upload/t_recipe-1280/spaghetti-amatriciana.jpg'

both_api = both_api()

print(both_api.get_recipe_from_cloud(image_url))






# test = spoon_api.get_top_ingredient("car")
# print(test[0])