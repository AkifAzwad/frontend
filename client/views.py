from django.shortcuts import render

import requests
# import json

# # Create your views here.

def index(request):
    r=requests.get('https://evening-badlands-91713.herokuapp.com/apis').json()

    if request.method == "POST":
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            email=request.POST.get('email')

            url = "https://evening-badlands-91713.herokuapp.com/apis/"
            next=requests.post(url, 
                        data={
                        "first_name" : fname,
                        "last_name" : lname,
                        "email" : email
                        }
                    )

            r=requests.get('https://evening-badlands-91713.herokuapp.com/apis').json()
            return render(request,'index.html',{
                        "response" : r,
                    })

    return render(request,'index.html',{
                "response" : r,
            }
            )    
            


  