from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserInput
from .utils import calculate, generate_table_html, generate_graph_html

def index_view(request):
    """takes user input and renders the results page

    Args:
        request (POST): form data

    Returns:
        object: Render
    """
    if request.method == 'POST':
        form = UserInput(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('results/')

    else:
        form = UserInput()
                
    return render(request, 'index.html', {'form': form})
    

def results_view(request):
    """renders the results page

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'GET':
        data_file = request.GET.get('upload_file', None)
        email = request.GET.get('email')

        
        benford_table = calculate(data_file)

        # Generate HTML for the table and graph
        table_html = generate_table_html(benford_table)
        graph_html = generate_graph_html(benford_table)
    
    return render(request, 'results.html', {'table_html': table_html, 'graph_html': graph_html})


    
    
def about(request): 
    """renders the about page

    Args:
        request (_type_): _description_
        
    Returns:
        _type_: _description_
    """

    about_dict = {"about":"The story behind Flexie"}

    return render(request, "about.html", context = about_dict)

