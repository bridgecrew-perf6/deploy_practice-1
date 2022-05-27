from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'basicapp/index.html')

# creating a new view for the form
def form_name_view(request):

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        # check if the data in the form is valid
        if form.is_valid():
            print('VALIDATION SUCCESS')
            print('NAME:' + form.cleaned_data['name'])
            print('EMAIL:' + form.cleaned_data['email'])
            print('TEXT:' + form.cleaned_data['text'])
    else:
        form = forms.FormName()

    return render(request, 'basicapp/form_page.html', {'form': form})