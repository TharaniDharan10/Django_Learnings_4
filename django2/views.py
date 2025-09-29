from django.shortcuts import render, redirect
from myapp.models import userModel


def view1(req):
    return render(req, 'thankyou.html')

def view2(req):
    return redirect("thankyou")

def contact(req):
    if(req.method=="POST"):
        return redirect("thankyou")
    
    return render(req, "contact.html")



# Create your views here.
def contactform(req):
    if req.method == "POST":
        try:
            n=req.POST.get("name")
            c=req.POST.get("city")
            p=req.POST.get("phone")
            s=req.POST.get("state")
            e=req.POST.get("email")

            fn=userModel(name=n, city=c, phone=p, state=s, email=e)
            fn.save()
            return redirect("thankyou")
        
        except Exception as ex:
            print("Error:", ex)
    
    return render(req, "contact2.html")
