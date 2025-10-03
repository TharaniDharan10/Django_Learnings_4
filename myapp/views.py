from django.shortcuts import render, redirect, get_object_or_404
from .forms import userforms
from myapp.models import userModel
from . import views
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


def display(req):
    fm=userforms()
    data={"user":fm}
    try:
        a=req.POST["name"]
        b=req.POST['phone']
        c=req.POST['city']
        d=req.POST.get('state')
        e=req.POST.get('email')
        f=req.POST.get('message')
        print(a,b,c,d,e,f)
        obj=userModel(name=a,phone=b,city=c,state=d,email=e,message=f)
        obj.save()

    except:
        pass
    return render(req,"display.html",data)

def select(req):
    obj=userModel.objects.all()
    return render(req,"displaydata.html",{'data':obj})


def update(req, id):
    obj = get_object_or_404(userModel, id=id)

    if req.method == "POST":
        fm = userforms(req.POST)
        if fm.is_valid():
            # Manually assign cleaned data back to model fields
            obj.name = fm.cleaned_data['name']
            obj.phone = fm.cleaned_data['phone']
            obj.city = fm.cleaned_data['city']
            obj.state = fm.cleaned_data['state']
            obj.email = fm.cleaned_data['email']
            obj.message = fm.cleaned_data['message']
            obj.save()
            return redirect("select")   # after update, go back to list
    else:
        # Pre-fill the form with existing object data
        fm = userforms(initial={
            'name': obj.name,
            'phone': obj.phone,
            'city': obj.city,
            'state': obj.state,
            'email': obj.email,
            'message': obj.message
        })

    return render(req, 'update.html', {'user': fm})

