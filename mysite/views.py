from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Event
from .forms import AddForm
from django.contrib import messages

def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'mysite/home.html', context)

def join_event(request, pk):
    current_event = Event.objects.get(id=pk)
    current_event.players.add(request.user)
    messages.success(request, 'User added to the event!')
    
    url = '/event/{}'.format(pk)

    return redirect(url)


class EventListView(ListView):
    model = Event
    template_name = 'mysite/home.html'
    context_object_name = 'events'
    ordering = ['-datetime_created']

class EventDetailView(DetailView):
    model = Event

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = AddForm

    def form_valid(self, form):
        form.save()
        form.instance.players.add(self.request.user)
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['sport', 'arena', 'date']

    def form_valid(self, form):
        form.save()
        form.instance.players.add(self.request.user)
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if event.players.filter(id=self.request.user.id).exists():
            return True

        return False
