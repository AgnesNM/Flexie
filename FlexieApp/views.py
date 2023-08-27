from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

#from FlexieApp import forms

from . forms import UserInput
from . models import FlexieUsers

# Create your views here.  

def form_view(request):

    # if this is a POST request we need to process the form data

    if request.method == "POST":

        # create a form instance and populate it with data from the request:        

        form = UserInput(request.POST)     
         

        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            # print(form.cleaned_data["username"])
            # print(form.cleaned_data["email"])       

            data = form.cleaned_data

            #create a new instance of the model

            user_info = FlexieUsers(email = data["email"], username = data["username"])
            
            #save the instance to the database

            user_info.save()

            HttpResponseRedirect("/thanks/") 
            

    # if a GET (or any other method) we'll create a blank form
    
    else:

        form = UserInput()
        

    return render(request, "FlexieApp/index.html", {"form": form})
   

def flexie(request):
    return HttpResponse("Hey, this is another view in the Flexie App.")


def about(request): 

    about_dict = {"about":"The story behind Flexie"}

    return render(request, "FlexieApp/about.html", context = about_dict)











