from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blog.models import Blog

# Create your views here.


class BlogCreatedViev(CreateView):
    model = Blog
    fields = ("heading", "content", "preview", "created_at", "sign_of_publication", "views_count")
    success_url = reverse_lazy("blog:blog_list")


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(sign_of_publication=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("heading", "content", "preview", "created_at", "sign_of_publication", "views_count")

    def get_success_url(self):
        return reverse_lazy("blog:blog_detail", kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
