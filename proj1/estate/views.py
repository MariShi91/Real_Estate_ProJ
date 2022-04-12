from django.shortcuts import render
from .models import Ad
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class AdListView(ListView):
    model = Ad
    template_name = 'estate/home.html'
    context_object_name = 'ads'
    ordering = ['-date_posted']

class AdDetailView(DetailView):
    model = Ad
    context_object_name = 'ad'

class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    fields = ['ad_type','accomodation_type','address', 'rooms', 'area', 'price', 'phone', 'desc', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AdUpdateView(LoginRequiredMixin, UserPassesTestMixin, CreateView, UpdateView):
    model = Ad
    fields = ['address', 'rooms', 'area', 'price', 'phone', 'desc', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.author:
            return True
        return False

class AdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ad
    success_url = '/'
    
    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.author:
            return True
        return False

