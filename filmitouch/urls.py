from django.conf.urls import url, include
from filmitouch.feeds import BlogFeed
from filmitouch.views import ContactView1, HealthView, SportView, TechnologyView, HolView, BolView, CarView, TravelView, \
    FashionView, NatureView

urlpatterns = [
    url(r'^health/$', HealthView.as_view(), name='health'),
    url(r'^sport/$', SportView.as_view(), name='sport'),
    url(r'^technology/$', TechnologyView.as_view(), name='technology'),
    url(r'^bollywood/$', BolView.as_view(), name='bollywood'),
    url(r'^hollywood/$', HolView.as_view(), name='hollywood'),
    url(r'^car/$', CarView.as_view(), name='cars'),
    url(r'^travel/$', TravelView.as_view(), name='travel'),
    url(r'^fashion/$', FashionView.as_view(), name='fashion'),
    url(r'^nature/$', NatureView.as_view(), name='nature'),
    url(r'^BlogFeed/$', BlogFeed(), name='blogfeed'),
    url(r'^contact/$', ContactView1.as_view(), name='contact1'),
]
