from django.shortcuts import render
from django.http import HttpResponse, Http404
from random import sample
import random
from .fake_db.pages import FAKE_DB_PAGES

FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/400" for id in range(10,14)
]

# Create your views here.
def home_view(request): 
    page_title="Home"
    hero_content= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean maximus, ante eget venenatis lobortis, metus diam porta velit, vel dictum sapien sapien quis leo. Cras nec lobortis erat, nec eleifend ex. Vestibulum quis dolor sed diam mollis tincidunt. Praesent ac mauris et ligula consequat egestas ac a mauris. Sed at lobortis ante. Cras tempus felis id metus suscipit, eget semper mi efficitur. Nam ultricies lobortis justo nec varius."
    print(request)
    context = {
        "page_title" : page_title,
    }
    context["hero_content"] = hero_content
    # context["FAKE_DB_PROJECTS"] = FAKE_DB_PROJECTS
    context["FAKE_DB_CAROUSEL"] = FAKE_DB_CAROUSEL
    return render(request, "page/homepage.html", context)

def page_view(request, page_slug):
    result = list(filter(lambda x: (x['url']== page_slug), FAKE_DB_PAGES))
    print((result))

    print("len result ", "*"*30)
    print(len(result))
    if result:
        context =  dict(
        page_title= result[0]['title'],
        detail = result[0]['detail'],
        # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
        )
        return render(request, "page/page_detail.html", context)
    raise Http404