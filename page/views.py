from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from random import sample
from page.models import Page

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
    page= get_object_or_404(Page, slug=page_slug)

    context=dict(
        page=page,
    )
    return render(request, "page/page_detail.html", context)

