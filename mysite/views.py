from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Report
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, UpdateView, DeleteView
from .forms import Form, CommentForm
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy


from django.db.models import Q
import operator
'''
def politics_index(request):
    articles = Article.objects.all()
    #Pagination
    paginator = Paginator(articles, 4)
    page = request.GET.get('page')
    try:
        articles_list = paginator.page(page)
    except PageNotAnInteger:
        articles_list = paginator.page(1)
    except EmptyPage:
        articles_list = paginator.page(paginator.num_pages)

    return render(request, 'mysite/article/list_articles.html', {'page': page, 'articles_list': articles_list})
'''


class PoliticsIndex(ListView):
    queryset = Article.objects.filter(topic='Politics')
    context_object_name = 'articles_list'
    paginate_by = 4
    template_name = 'mysite/article/list_articles.html'


class Ordering(ListView):
    queryset = Article.objects.filter(topic='Politics')
    context_object_name = 'order_likes'
    paginate_by = 4
    template_name = 'mysite/article/order-likes.html'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-likes')
        return ordering


def politics_detail(request, article):
    article = get_object_or_404(Article, slug=article)
    total_likes = article.total_likes()
    total_dislikes = article.total_dislikes()

    liked = False
    if article.likes.filter(id=request.user.id).exists():
        liked = True

    disliked = False
    if article.dislikes.filter(id=request.user.id).exists():
        disliked = True

    comments = article.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'mysite/article/detail.html', {'article': article,
                                                            'total_likes': total_likes,
                                                            'total_dislikes': total_dislikes,
                                                            'liked': liked,
                                                            'disliked': disliked,

                                                            'comments': comments,
                                                            'new_comment': new_comment,
                                                            'comment_form': comment_form,
                                                          })


def new_post(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.publish = timezone.now()
            article.slug = slugify(article)
            article.save()
            return redirect('mysite:Politics_detail', article.slug)
    else:
        form = Form(request.POST)
    return render(request, 'mysite/post_edit.html', {'form': form})


def like_view(request, article):
    article = get_object_or_404(Article, id=request.POST.get('article_id'))
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        article.dislikes.remove(request.user)
        liked = True
    return HttpResponseRedirect(reverse('mysite:Politics_detail', args=[article.slug]))


def dislike_view(request, article):
    article = get_object_or_404(Article, id=request.POST.get('article_id'))
    disliked = False
    if article.dislikes.filter(id=request.user.id).exists():
        article.dislikes.remove(request.user)
        disliked = False
    else:
        article.dislikes.add(request.user)
        article.likes.remove(request.user)
        disliked = True
    return HttpResponseRedirect(reverse('mysite:Politics_detail', args=[article.slug]))


def report_article(request):
    #report_form = Report()
    if request.method == "POST":
        report = Report()
        title = request.POST.get('title')
        email = request.POST.get('email')
        reason = request.POST.get('flexRadioDefault')
        report.title = title
        report.email = email
        report.reason = reason
        report.save()
        return render(request, 'mysite/article/thanks.html')
    return render(request, 'mysite/article/report.html')


class EditPost(UpdateView):
    model = Article
    form_class = Form
    template_name = 'mysite/article/edit_post.html'
    #fields = ['title', 'body']


class DeletePost(DeleteView):
    model = Article
    template_name = 'mysite/article/delete.html'
    success_url = reverse_lazy('home:index')









# def sports_index(request):
#     return render(request, 'mysite/sports.html')

class SportsIndex(ListView):
    queryset = Article.objects.filter(topic='Sports')
    context_object_name = 'articles_list'
    paginate_by = 4
    template_name = 'mysite/article/list_sports.html'


class OrderingSports(ListView):
    queryset = Article.objects.filter(topic='Sports')
    context_object_name = 'order_likes_sports'
    paginate_by = 4
    template_name = 'mysite/article/order-likes-sports.html'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-likes')
        return ordering






class FoodIndex(ListView):
    queryset = Article.objects.filter(topic='Food')
    context_object_name = 'articles_list'
    paginate_by = 4
    template_name = 'mysite/article/list_food.html'


class OrderingFood(ListView):
    queryset = Article.objects.filter(topic='Food')
    context_object_name = 'order_likes_food'
    paginate_by = 4
    template_name = 'mysite/article/order-likes-food.html'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-likes')
        return ordering



class MusicIndex(ListView):
    queryset = Article.objects.filter(topic='Music')
    context_object_name = 'articles_list'
    paginate_by = 4
    template_name = 'mysite/article/list_music.html'

class OrderingMusic(ListView):
    queryset = Article.objects.filter(topic='Music')
    context_object_name = 'order_likes_music'
    paginate_by = 4
    template_name = 'mysite/article/order-likes-music.html'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-likes')
        return ordering



class TechIndex(ListView):
    queryset = Article.objects.filter(topic='Tech')
    context_object_name = 'articles_list'
    paginate_by = 4
    template_name = 'mysite/article/list_tech.html'

class OrderingTech(ListView):
    queryset = Article.objects.filter(topic='Tech')
    context_object_name = 'order_likes_tech'
    paginate_by = 4
    template_name = 'mysite/article/order-likes-tech.html'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-likes')
        return ordering

class TravelIndex(ListView):
    queryset = Article.objects.filter(topic='Travel')
    context_object_name = 'articles_list'
    paginate_by = 4
    template_name = 'mysite/article/list_travel.html'

class OrderingTravel(ListView):
    queryset = Article.objects.filter(topic='Travel')
    context_object_name = 'order_likes_travel'
    paginate_by = 4
    template_name = 'mysite/article/order-likes-travel.html'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-likes')
        return ordering


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        search_title = Article.objects.filter(title__contains = q)
        return render(request, 'mysite/search.html', {'search_title': search_title, 'query': q})
    else:
        return render(request, 'home/index.html')


