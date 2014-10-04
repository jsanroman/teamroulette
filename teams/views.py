from django.shortcuts import render
from . import forms

def main(request):
    if request.method == 'GET':
        form = forms.TeamForm()
        dictionary = {'name': 'Miguel',
                      'form': form}
        return render(request,
                      'teams/index.html',
                      dictionary=dictionary)
    elif request.method == 'POST':
        form = forms.TeamForm(data=request.POST)
        if form.is_valid():
            assert False
        else:
            dictionary = {'name': 'Miguel',
                          'form': form}
            return render(request,
                          'teams/index.html',
                          dictionary=dictionary)

