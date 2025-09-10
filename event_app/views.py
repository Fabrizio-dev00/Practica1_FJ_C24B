from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Eventos
from .forms import EventForm
from django.urls import reverse_lazy

class EventListView(ListView):
    model = Eventos
    template_name = 'event_app/even'