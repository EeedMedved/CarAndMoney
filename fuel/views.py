from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Refill
from .forms import RefillForm


def refill_list(request):
    refills = Refill.objects.all()
    return render(request, 'fuel/list.html', {'refill_list': refills})


class CreateRefillView(CreateView):
    form_class = RefillForm
    template_name = 'fuel/refill_add.html'
    success_url = reverse_lazy('refill_list')
