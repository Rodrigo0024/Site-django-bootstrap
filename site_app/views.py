from django.shortcuts import render, redirect
from .models import Anime

# Create your views here.
def index(request):
    template_name = 'index.html' # template
    
   
    return render(request, template_name) # render



def anime(request):
    template_name = 'anime.html' # template
    
   
    return render(request, template_name) # render




    
   
    return render(request, template_name) # render


def listaanimes(request):
    template_name = 'lisanimes.html' # template
    
   
    return render(request, template_name) # render


# views.py



def lista_animes(request):
    animes = Anime.objects.all()
    return render(request, 'lista-animes.html', {'animes': animes})

def detalhe_anime(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    return render(request, 'detalhe-anime.html', {'anime': anime})




from .forms import  AnimeForm







def adicione(request):
    if request.method == "POST":
        form = AnimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Redireciona para uma página de sucesso
    else:
        form = AnimeForm()
    return render(request, 'adicione-anime.html', {'form': form})


def sucesso(request):
    return render(request, 'sucesso.html')