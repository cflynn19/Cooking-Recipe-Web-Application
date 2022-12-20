from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .both_api import both_api



# Create your views here.

# Configure on how to return appropriate HTML file given input type of text/image
def get_homepage(request):
    # return render(request, './homepage.html')
    """Process images uploaded by users"""
    if request.method == 'POST':
         form = ImageForm(request.POST, request.FILES)
         # For image inputs
         if form.is_valid():
             form.save()
             # Get the current instance object to display in the template
             api = both_api()
             #img_obj = form.instance
             img_path = '.' + form.instance.image.url
             keys = api.get_labels_as_string_from_local(img_path)
             receipes = api.get_recipe_from_local(img_path)
             receipe1 = receipes[0]
             print(f"results: {keys}")
             print("Receipe 1:")
             print(receipe1)
             content = {
                 'keys': keys,
                 'title': receipe1['title'],
                 'img_url': receipe1['image'],
                 'id': receipe1['id'],
                 'form': form,
             }
             return render(request, './result.html', content)
    else:
         form = ImageForm()
    return render(request, './homepage.html', {'form': form})