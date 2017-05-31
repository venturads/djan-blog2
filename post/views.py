from django.shortcuts import render_to_response, render
from django import template
from django.http import HttpResponse
# Create your views here.

def home(request):
   # return HttpResponse('<h1>tes ven</h1>')
  return render(request, 'post/home.html',{
      'template_name': 'post/nav.html', 
      'template_footer': 'post/footer.html',
  })
