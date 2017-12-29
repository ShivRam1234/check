from tastypie.resources import ModelResource
from tastypie.constants import ALL
from filmitouch.models import Categories,Subcategories,Language1,Newsletter,Advertisement1,Blog,ContactForm1


class BlogResources(ModelResource):
    class Meta:
        queryset = Blog.objects.all()
        resource_name = 'article'