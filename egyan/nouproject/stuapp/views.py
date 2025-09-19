from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from . models import Response
from nouapp.models import StudentInfo, LoginInfo
from adminapp.models import Material

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def stuhome(request):
    try:
        if request.session['userid']!=None:
            return render(request,"stuhome.html")
    except KeyError:
        return redirect("nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def logout(request):
        try:
             if request.session['userid']!=None:
                  del request.session['userid']
                  return redirect("nouapp:login")
        except KeyError:
             return redirect("nouapp:login")
        


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studymaterial(request):
       try:
         if request.session['userid']!=None:
            stu=StudentInfo.objects.get(rollno=request.session['userid'])
            smat=Material.objects.filter(program=stu.program,branch=stu.branch,year=stu.year,materialtype='smat')
            return render(request,"studymaterial.html",{"smat":smat})
       except KeyError:
             return redirect("nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def assignments(request):
       try:
         if request.session['userid']!=None:
            stu=StudentInfo.objects.get(rollno=request.session['userid'])
            assign=Material.objects.filter(program=stu.program,branch=stu.branch,year=stu.year,materialtype='assign')
            return render(request,"assignments.html",{"assign":assign})
       except KeyError:
             return redirect("nouapp:login")
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)  
def changepassword(request):
       try:
         if request.session['userid']!=None:
            if request.method=='POST':
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                confirmpassword=request.POST['confirmpassword']
                msg=''
                if newpassword!=confirmpassword:
                     msg="Password Not Match"
                     return render(request,"changepassword.html",{'msg':msg})
                else:
                    try:
                        obj=LoginInfo.objects.get(userid=request.session['userid'],password=oldpassword)
                        LoginInfo.objects.filter(userid=request.session['userid']).update(password=newpassword)
                        return redirect("stuapp:logout")
                    except:
                         msg='old Password not matched'
                         return render(request,"changepassword.html",{'msg':msg})
            return render(request,"changepassword.html")
       except KeyError:
             return redirect("nouapp:login")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def response(request):
       try:
           if request.session['userid']!=None:
               if request.method=='POST':
                    obj=StudentInfo.objects.get(rollno=request.session['userid'])
                    rollno=obj.rollno
                    name=obj.name
                    program=obj.program
                    branch=obj.branch
                    year=obj.year
                    responsetype=request.POST['responsetype']
                    responsetext=request.POST['responsetext']
                    res=Response(rollno=rollno,name=name,program=program, branch=branch,year=year, responsetype=responsetype, responsetext=responsetext)
                    res.save()
                    return render(request,"response.html",{"msg":"Respone is submited"})
               return render(request,"response.html")
       except KeyError:
             return redirect("nouapp:login")