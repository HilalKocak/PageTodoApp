from django.urls import path
from todo.views import all_todos_view, tag_view, category_view, todo_detail_view


urlpatterns = [
    #All todos:
    path('', all_todos_view, name="all_todos_view"),
    path('category/<slug:category_slug>', category_view, name="category_view"),
    path('tag/<slug:tag_slug>/', tag_view, name="tag_view"),
    # Todo Detail
    path('category/<slug:category_slug>/todo/<int:id>/', todo_detail_view, name="todo_detail_view")
]

