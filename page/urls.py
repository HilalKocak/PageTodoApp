from django.urls import path
from .views import ( # we can use . to represent this dir (views in this dir)
    home_view,
    #about_us_view,
    #contact_us_view,
    #vision_view,
    page_view,
   # page_slug_learn,
    )


urlpatterns = [
    path('', home_view, name="home"),
    #path('about/', about_us_view, name="about_us"), # about: what is written in the link after 127.0.0.0:8080/about
    #path('contact/', contact_us_view, name="contact_us"), # contact_us.html or contact_us/ can be write its just key
    #path('vision/', vision_view, name="vision"), 
    path('<slug:slug>/', page_view),
    #path('<int:id>/', page_slug_learn), #func under views
]

