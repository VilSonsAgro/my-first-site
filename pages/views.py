from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views.generic import TemplateView
from .forms import HomeForm
from django.shortcuts import render, redirect


class HomePageView(TemplateView):
    template_name = 'homePage.html'


class AboutPageView(TemplateView):
    template_name = 'about_us.html'


class ProductsPageView(TemplateView):
    template_name = 'products.html'


class FoodSafetyPageView(TemplateView):
    template_name = 'food_safety.html'


class ContactUsPageView(TemplateView):
    template_name = 'contact_us.html'


class FeedBackPageView(TemplateView):
    template_name = 'feedback.html'

class HomeView(TemplateView):
    template_name = 'feedback.html'
    def get(self, request):
        form=HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form=HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('pages/feedback.html/')

        args={'form': form, 'text': text}




