from urllib import response
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse,JsonResponse
from api.models import cars

          # create function #

def index(request):
    if request.method == "POST":
        
        cars_name   = request.POST.get('cars_name')
        cars_colour = request.POST.get('cars_colour')  
        cars_price  = request.POST.get('cars_price') 
        cars_models = request.POST.get('cars_models')
        
        data = {
            
            'cars_name':cars_name,
            'cars_colour':cars_colour,
            'cars_price':cars_price,
            'cars_models':cars_models
        }
            
        response = requests.post('http://127.0.0.1:8000/cars/',json=data)
        return redirect('retrieve')
        
    return render(request,'index.html')
    

               # read function #  
     
def retrieve(request):
    response = requests.get('http://127.0.0.1:8000/cars/').json()
    return render(request,'retrieve.html',{'response':response})


               # update function #

def update(request,id):
    
    if request.method=="POST":
        cars_name=request.POST['cars_name']
        cars_colour=request.POST['cars_colour']
        cars_price=request.POST['cars_price']
        cars_models=request.POST['cars_models']
        
        data={
            
            'cars_name': cars_name,
            'cars_colour':cars_colour,
            'cars_price':cars_price,
            'cars_models':cars_models
        }
        
        response =  requests.put('http://127.0.0.1:8000/cars/{pk}/'.format(pk=id),json=data) 
        return redirect('retrieve')
    
    return render(request,'update.html')



           # delete function #

def delete(request,id):
    response = requests.delete('http://127.0.0.1:8000/cars/{pk}/'.format(pk=id))
    print(response)
    return redirect('retrieve')

           # popup function #

def popup(request):
    return render(request,'popup.html')   