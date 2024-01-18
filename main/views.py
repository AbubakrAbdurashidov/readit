from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from article.models import Article
from .models import Feedback, Contact
from .forms import ContactForm


def home_view(request):
    articles = Article.objects.order_by('-id')
    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    ctx = {
        'articles': page_obj,
    }
    return render(request, 'main/index.html', ctx)

def about_view(request):
    feedbacks = Feedback.objects.all()
    ctx = {
        'object_list': feedbacks
    }
    return render(request, 'main/about.html', ctx)


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message successfully sent')
            return redirect('.#django-messages')
    ctx = {
        'form': form
    }
    return render(request, 'main/contact.html', ctx)