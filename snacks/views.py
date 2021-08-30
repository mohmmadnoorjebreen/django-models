from django.views.generic import ListView, DetailView
from .models import snacks

# Create your views here.
class SnackListView(ListView):
    template_name = "snack_list.html"
    model = snacks
    
class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = snacks    