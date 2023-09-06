from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . forms import *
from . models import *


def index_view(request):
    """takes user input and renders the results page

    Args:
        request (POST): form data

    Returns:
        object: Render
    """
    if request.method == "POST":      
        form = UserInput(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            HttpResponseRedirect("/thanks/") 

    else:
        form = UserInput()
        
    return render(request, "FlexieApp/index.html", {"form": form})
   

def analysis_results_view(request):
    """renders the results page

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Get the uploaded file
    user_info = FlexieUsers.objects.last()
    data = user_info.file

    # Calculate Benford's Law results
    benford_table = calculate(data)

    # Generate HTML for the table and graph
    table_html = generate_table_html(benford_table)
    graph_html = generate_graph_html(benford_table)

    # Render a template with the results
    return render(request, 'FlexieApp/results.html', {'table_html': table_html, 'graph_html': graph_html})


def about(request): 

    about_dict = {"about":"The story behind Flexie"}

    return render(request, "FlexieApp/about.html", context = about_dict)











