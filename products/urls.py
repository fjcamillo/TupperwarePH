from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stock/(?P<id>\d+)/$', views.specificproductview, name='SpecificProductView'),
    # url(r'^', views.specificproductview, name='SpecificProductView')
    url(r'^category/men$', views.men, name='men'),
    url(r'^category/women$', views.women, name='women'),
    url(r'^category/kids$', views.kids, name='kids'),
    url(r'^category/tupperware$', views.tupperware, name='tupperware'),


    #--------------> Sub categories
    url(r'^category/kids/1$', views.kidone, name='kidone'),
    url(r'^category/kids/2$', views.kidtwo, name='kidtwo'),
    url(r'^category/kids/3$', views.kidThree, name='kidthree'),
    url(r'^category/kids/4$', views.kidFour, name='kidfour'),
    url(r'^category/kids/5$', views.kidFive, name='kidfive'),

    #------------------------>

    url(r'^category/men/1$', views.menone, name='menone'),
    url(r'^category/men/2$', views.mentwo, name='mentwo'),
    url(r'^category/men/3$', views.menthree, name='menthree'),
    url(r'^category/men/4$', views.menfour, name='menfour'),

    url(r'^category/men/body/1$', views.menbodyone, name='menbodyone'),
    url(r'^category/men/body/2$', views.menbodytwo, name='menbodytwo'),
    url(r'^category/men/body/3$', views.menbodythree, name='menbodythree'),
    url(r'^category/men/deo/1$', views.mendeoone, name='mendeoone'),
    url(r'^category/men/deo/2$', views.mendeotwo, name='mendeotwo'),

    #----------------------------------->

    url(r'^category/tupperware/1$', views.tupperwareone, name='tupperwareone'),
    url(r'^category/tupperware/2$', views.tupperwaretwo, name='tupperwaretwo'),
    url(r'^category/tupperware/3$', views.tupperwarethree, name='tupperwarethree'),

    #------------------------------------->

    url(r'^category/women/1$', views.womenone, name='womenone'),
    url(r'^category/women/2$', views.womentwo, name='womentwo'),
    url(r'^category/women/3$', views.womenthree, name='womenthree'),
    url(r'^category/women/4$', views.womenfour, name='womenfour'),
    url(r'^category/women/5$', views.womenfive, name='womenfive'),
    url(r'^category/women/6$', views.womensix, name='womensix'),
    url(r'^category/women/7$', views.womenseven, name='womenseven'),
    url(r'^category/women/8$', views.womeneight, name='womeneight'),
    url(r'^category/women/9$', views.womennine, name='womennine'),
    url(r'^category/women/10$', views.womenten, name='womenten'),
    url(r'^category/women/11$', views.womeneleven, name='womeneleven'),
    url(r'^category/women/12$', views.womentwelve, name='womentwelve'),


    url(r'^category/women/deo/1$', views.womendeoone, name='womenone'),
    url(r'^category/women/deo/2$', views.womendeotwo, name='womentwo'),
    url(r'^category/women/deo/3$', views.womendeothree, name='womenthree'),
    url(r'^category/women/fragrance/1$', views.womenfragranceone, name='womenfour'),
    url(r'^category/women/fragrance/2$', views.womenfragrancetwo, name='womenfive'),
    url(r'^category/women/fragrance/3$', views.womenfragrancethree, name='womensix'),
    url(r'^category/women/fragrance/4$', views.womenfragrancefour, name='womenseven'),
    url(r'^category/women/fragrance/5$', views.womenfragrancefive, name='womeneight'),
    url(r'^category/women/lotion/1$', views.womenlotionone, name='womennine'),
    url(r'^category/women/lotion/2$', views.womenlotiontwo, name='womenten'),
    url(r'^category/women/lotion/3$', views.womenlotionthree, name='womeneleven'),
    url(r'^category/women/lotion/4$', views.womenlotionfour, name='womentwelve'),
    url(r'^category/women/lotion/5$', views.womenlotionfive, name='womentwelve'),
]


