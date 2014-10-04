from django.shortcuts import render, redirect
from . import forms

def main(request):
    dictionary = {'name': 'Miguel'}
    if request.method == 'GET':
        form = forms.TeamForm()
        dictionary['form'] = form
        return render(request,
                      'teams/index.html',
                      dictionary=dictionary)
    elif request.method == 'POST':
        form = forms.TeamForm(data=request.POST)
        if form.is_valid():
            return redirect('/')
        else:
            dictionary['form'] = form
            return render(request,
                          'teams/index.html',
                          dictionary=dictionary)
