from django.shortcuts import render

from myapp.models import userModel

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
        
        except Exception as ex:
            print("Error:", ex)
    
    return render(req, "contact2.html")


