from django.shortcuts import render
from django.views.generic import  TemplateView,DetailView
from django.db.models import Q #malumotlar bazasidan malumotlarni qidirsh uchun Q obyektidan foydalanamiz

from .models.articles import Post
from .models.category import Category

# Create your views here.

def index(request):
  posts = None
  cat_menu = Category.objects.all()
  categoryID = request.GET.get('category') # request(so'rov) boyicha ichidagi malumotni yuklaydi 
  if categoryID:
    posts = Post.get_all_products_by_categoryid(categoryID) 
  else: 
    posts = Post.objects.all();
  if categoryID:
    post_header = Post.get_all_products_by_categoryid(categoryID).order_by("?")[:1]
  else:
    post_header = Post.objects.all().order_by("?")[:1]
  context = {}
  context['cat_menu'] = cat_menu
  context['posts'] = posts
  context['post_header'] = post_header
  return render(request, 'home.html', context)


def Serachbar(request):
  search = request.GET.get("search") #request ichidagi qiymatni olish 
  if search:
    postssearch = Post.objects.all().filter(Q(title__icontains = search) | Q(body__icontains=search))
    return render(request,'searchbar.html',{'postssearch':postssearch})

# Q obyektidan quydagicha foydalanamiz Q(title__icontains = search)

class AboutPage(TemplateView):
  template_name = 'about.html'

class ArticlePage(DetailView):
  model = Post
  template_name = 'article.html'

