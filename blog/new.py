#Python shell commands
from .models import Post
Post.objects.exclude(id__in=[1,2,]) # There is one =
Post.objects.exclude(id__in=[1,2,]).delete()
items= Post.objects.all()
for id in range(21):
    if not id%2==0:
        obj=items[0]
    else:
        obj=items[1]
    obj.pk=None
    obj.title = f"{obj.title} - {id}" #we changed title info
    #we forgot slug info
    obj.save()

    i=Post.objects.last()

    
# add slug via shell
for item in items:
    item.slug=f"{slugify(item.title)}-{item.pk}"
    item.save()


for item in items:
    print(item.slug)