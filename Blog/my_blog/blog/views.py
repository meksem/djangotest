from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def add(request):
    return render(request,'result.htm')
# Create your views here.
