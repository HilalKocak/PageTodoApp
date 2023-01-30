from todo.models import Todo
todos=Todo.objects.all()

for item in todos:
    if not "Django" in item.title:
        item.title=f"{item.title} -Django"
        item.save()

for item in todos:
    print(item)

Todo.objects.exclude(title__icontains="Django").count()

for item in todos:
    item.title=f"{item.title} -Django"
    item.save()