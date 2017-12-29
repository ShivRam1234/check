from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from filmitouch.models import Blog


class BlogFeed(Feed):
    feed_type = Rss201rev2Feed
    title = "Latest Blog"
    link = "/BlogFeed"
    description = "Blog With Different Categories"

    @staticmethod
    def items():
        return Blog.objects.order_by('-datetime')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blog-detail', args=[item.slug])