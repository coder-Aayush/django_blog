from django.shortcuts import render,get_object_or_404
from .models import Blog,Contact,NewsSubscriber
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    query = request.GET.get('q', None)
    if query is not None:
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(slug__icontains=query)
        )
    else:
        result = Blog.objects.all()

    paginator = Paginator(blogs, 9)
    page = request.GET.get('page')

    blogs = paginator.get_page(page)

    context = {
        'blogs':blogs,
        'query':query
               }

    return render(request, 'index.html', context)

def post(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    return render(request,'blog.html',{'blog':blog})



def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        body = request.POST.get('body')
        date = timezone.now()
        form = Contact(name=name,subject=subject,email=email,body=body,date=date)
        form.save()
        send_mail(
            'New Message From Blog',
            'Subject = {} \n {} \n email is {}\n question is {}\n \n email on {}'.format(subject,name,email,body,date),
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )
    else:
        return render(request,'contact.html')
    return render(request,'contact.html')


def news(request):
    if request.method == 'POST':
        email = request.POST['email']
        sub = NewsSubscriber(email=email)
        sub.save()

    return render(request,'news.html')

def support(request):
    return render(request,'support.html')

def handler404(request):
    return render(request,'404.html')

def handler500(request):
    return render(request,'404.html')