from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Repository
import requests

def home(request):
    return render(request, 'home.html')

def search_repositories(request):
    query = request.GET.get('q')  
    order = 'desc'
    if query:
        url = f"https://api.github.com/search/repositories?q={query}&order={order}in:name"
        response = requests.get(url)
        if response:
            data = response.json()
            repositories = data.get('items', []) 
            if repositories== []: 
               return render(request, 'error.html', {'error_message': 'Failed to fetch data from GitHub API.'})
            for repo_data in repositories:
                Repository.objects.create(
                    name=repo_data['name'],
                    owner=repo_data['owner']['login'],
                    description=repo_data['description'],
                    stars=repo_data['stargazers_count'],
                    forks=repo_data['forks_count'], 
                )
                if request.GET:
                  page_number = request.GET.get('page', 1)
                paginator = Paginator(repositories, 10)
                page_obj = paginator.get_page(page_number)
                return render(request, 'results.html', {'page_obj': page_obj})
       
           
                
    return render(request, 'home.html')

def error(request):
    return render(request, 'error.html')




    
    

