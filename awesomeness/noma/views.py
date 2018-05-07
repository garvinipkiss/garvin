from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.


def index(request):
    '''
    function to display the index page
    '''
    images = Image.objects.all()
    return render(request, 'index.html', {"index": index})


def image(request, image_id):

    images = Image.objects.get(id=image_id)

    return render(request, "image.html", {"images": images})


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

def get_gamers(request):
    location_images = Image.gamers()
    return render(request, 'display.html', {"images": display_images})


def get_mixtape(request):
    display_images = Image.mixtape()
    return render(request, 'display.html', {"images": display_images})
