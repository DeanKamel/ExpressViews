from django.urls import path
from . import views

app_name = 'mysite'
urlpatterns = [
    #/home/mysite/
    # path('', views.politics_index, name='Politics_index'),                # Normal function view
    path('', views.PoliticsIndex.as_view(), name='Politics_index'),          # Class-based views
    path('order-by-likes/', views.Ordering.as_view(), name='order_likes'),
    path('<slug:article>/', views.politics_detail, name='Politics_detail'),
    path('post/new/', views.new_post, name='new_post'),
    path('like/<slug:article>/', views.like_view, name='like_article'),
    path('dislike/<slug:article>/', views.dislike_view, name='dislike_article'),
    path('post/report/', views.report_article, name='report'),
    path('post/edit/<int:pk>/', views.EditPost.as_view(), name='edit_post'),
    path('post/delete/<int:pk>/', views.DeletePost.as_view(), name='delete_post'),


    path('sports/page/', views.SportsIndex.as_view(), name='Sports_index'),
    path('sports/page/order-by-likes/', views.OrderingSports.as_view(), name='order_likes_sports'),

    path('food/page/', views.FoodIndex.as_view(), name='Food_index'),
    path('food/page/order-by-likes/', views.OrderingFood.as_view(), name='order_likes_food'),

    path('music/page/', views.MusicIndex.as_view(), name='Music_index'),
    path('music/page/order-by-likes/', views.OrderingMusic.as_view(), name='order_likes_music'),

    path('tech/page/', views.TechIndex.as_view(), name='Tech_index'),
    path('tech/page/order-by-likes/', views.OrderingTech.as_view(), name='order_likes_tech'),

    path('travel/page/', views.TravelIndex.as_view(), name='Travel_index'),
    path('travel/page/order-by-likes/', views.OrderingTravel.as_view(), name='order_likes_travel'),

    path('search/filtered/', views.search, name='searched_articles'),
    path('music/page/search/filtered/', views.search, name='searched_articles'),
    path('food/page/search/filtered/', views.search, name='searched_articles'),
    path('tech/page/search/filtered/', views.search, name='searched_articles'),
    path('travel/page/search/filtered/', views.search, name='searched_articles'),
    path('sports/page/search/filtered/', views.search, name='searched_articles'),

]
