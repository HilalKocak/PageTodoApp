from django.shortcuts import render
from django.http import HttpResponse, Http404
from random import sample
import random
from .fake_db.pages import FAKE_DB_PAGES
# Generated 8 image source id between 30 and 100
# FAKE_DB_PROJECTS = [
#     f"https://picsum.photos/id/{id}/400/250" for id in random.sample(range(30, 100), 8)

#     # f"https://picsum.photos/id/{id}/400/250" for id in range(21, 29))

# ]

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

# def about_us_view(request):
#     page_title = "About"
#     hero_content= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean maximus, ante eget venenatis lobortis, metus diam porta velit, vel dictum sapien sapien quis leo. Cras nec lobortis erat, nec eleifend ex. Vestibulum quis dolor sed diam mollis tincidunt. Praesent ac mauris et ligula consequat egestas ac a mauris. Sed at lobortis ante. Cras tempus felis id metus suscipit, eget semper mi efficitur. Nam ultricies lobortis justo nec varius."
#     context =dict(page_title=page_title,
#     hero_content = hero_content,
#     # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
#     )
#     return render(request, "page/about_us.html", context)

# def contact_us_view(request):
#     page_title = "Contact"
#     hero_content= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean maximus, ante eget venenatis lobortis, metus diam porta velit, vel dictum sapien sapien quis leo. Cras nec lobortis erat, nec eleifend ex. Vestibulum quis dolor sed diam mollis tincidunt. Praesent ac mauris et ligula consequat egestas ac a mauris. Sed at lobortis ante. Cras tempus felis id metus suscipit, eget semper mi efficitur. Nam ultricies lobortis justo nec varius."
#     context =dict(page_title=page_title,
#     hero_content = hero_content,
#     # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,

#     )
#     return render(request, "page/contact_us.html", context)

# def vision_view(request):
#     page_title = "Vision"
#     hero_content= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean maximus, ante eget venenatis lobortis, metus diam porta velit, vel dictum sapien sapien quis leo. Cras nec lobortis erat, nec eleifend ex. Vestibulum quis dolor sed diam mollis tincidunt. Praesent ac mauris et ligula consequat egestas ac a mauris. Sed at lobortis ante. Cras tempus felis id metus suscipit, eget semper mi efficitur. Nam ultricies lobortis justo nec varius."
#     context =dict(
#         page_title=page_title,
#         hero_content = hero_content,
#         # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
#         )
#     return render(request, "page/vision.html", context)   


def page_view(request, slug):
    result = list(filter(lambda x: (x['url']== slug), FAKE_DB_PAGES))
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

# def page_slug_learn(request, id):
#     print("x"* 30, id, "x"*30)
#     context = {'pk':id}
#     return render(request, "page/vision.html", context) 
