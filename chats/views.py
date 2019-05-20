from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Chat


# Create your views here.
class ChatListView(ListView):
    model = Chat
    template_name = 'home.html'
    context_object_name = 'chat_list'


class ChatDetailView(DetailView):  # provides a context object called either object or the lowercased name of our model
    model = Chat                   # can override this by add context_object_name value
    template_name = 'chat_detail.html'


class ChatCreateView(CreateView):
    model = Chat
    template_name = 'chat_new.html'
    fields = ['title', 'text', 'author']


class ChatEditView(UpdateView):
    model = Chat
    template_name = 'chat_edit.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('home')


class ChatDeleteView(DeleteView):
    model = Chat
    template_name = 'chat_delete.html'
    success_url = reverse_lazy('home')  # reverse_lazy will wait until the deletion is complete
