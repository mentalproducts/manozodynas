from django.shortcuts import render
from forms import WordWithoutTranslationForm
from django.http import HttpResponseRedirect
from manozodynas.models import WordWithoutTranslation
def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def words_view(request):
    return render(request, 'manozodynas/words.html', {'zodziai' : WordWithoutTranslation.objects.all()})


def post_word(request):
    if request.method == 'POST':
        form = WordWithoutTranslationForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            context = form.cleaned_data['context']
            form.save()
            return HttpResponseRedirect('/zodziai/')
    else:
        form = WordWithoutTranslationForm()
    return render(request, 'manozodynas/post_word.html', {'form': form,
    })


