from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.


def index(request):
    '''
    function to display the index page
    '''
    image = Image.objects.all()
    return render(request, 'index.html', {"image": image})


def image(request, image_id):

    image = Image.objects.get(id=image_id)

    return render(request, 'image.html', {"image": image})

def search_results(request):
    '''
    search function to display search search_results
    args:
    order defines category
    '''
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
