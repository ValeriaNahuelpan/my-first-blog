from django.shortcuts import render

# Create your views here.ss
def post_list(request):
    return render(request, 'blog/post_list.html', {})