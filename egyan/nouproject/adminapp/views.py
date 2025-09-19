from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from nouapp.models import StudentInfo, Enquiry
from stuapp.models import Response
from . models import Material


# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    try:
        if request.session['adminid']!=None:
            return render(request,"adminhome.html")
    except KeyError:
        return redirect("nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminlogout(request):
        try:
             if request.session['adminid']!=None:
                  del request.session['adminid']
                  return redirect("nouapp:adminlogin")
        except KeyError:
             return redirect("nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def managecomplaint(request):
    try:
        if request.session['adminid']!=None:
            comp=Response.objects.filter(responsetype='complaint')
            return render(request,"managecomplaint.html",{'comp':comp})
    except KeyError:
        return redirect("nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def manageenquiry(request):
    try:
        if request.session['adminid']!=None:
            enq=Enquiry.objects.all()
            return render(request,"manageenquiry.html",{'enq':enq})
    except KeyError:
        return redirect("nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def managefeedback(request):
    try:
        if request.session['adminid']!=None:
            feed=Response.objects.filter(responsetype='feedback')
            return render(request,"managefeedback.html",{'feed':feed})
    except KeyError:
        return redirect("nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def managestudent(request):
    try:
        if request.session['adminid']!=None:
            stu=StudentInfo.objects.all()
            return render(request,"managestudent.html",{'stu':stu})
    except KeyError:
        return redirect("nouapp:login")
def managestudymaterial(request):
    try:
        if request.session['adminid']!=None:
            if request.method=='POST':
                program=request.POST['program']
                branch=request.POST['branch']
                year=request.POST['year']
                subject=request.POST['subject']
                materialtype=request.POST['materialtype']
                filename=request.POST['filename']
                myfile=request.FILES['myfile']
                mat=Material(program=program,branch=branch,year=year,subject=subject,materialtype=materialtype,filename=filename,myfile=myfile)
                mat.save()
                return render(request,"managestudymaterial.html",{"msg":"Uploaded"})


            return render(request,"managestudymaterial.html")
    except KeyError:
        return redirect("nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deleteenq(request, id):
    try:
        if request.session['adminid']!=None:
            enq=Enquiry.objects.get(id=id)
            enq.delete()
            return redirect("adminapp:manageenquiry")
    except KeyError:
        return redirect("nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletefeed(request, id):
    try:
        if request.session['adminid']!=None:
            feed=Response.objects.get(id=id)
            feed.delete()
            return redirect("adminapp:managefeedback")
    except KeyError:
        return redirect("nouapp:login")
def deletecomp(request, id):
    try:
        if request.session['adminid']!=None:
            comp=Response.objects.get(id=id)
            comp.delete()
            return redirect("adminapp:managecomplaint")
    except KeyError:
        return redirect("nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewmaterial(request):
    try:
        if request.session['adminid']!=None:
            smat=Material.objects.all()
            return render(request,"viewmaterial.html",{'smat':smat})
    except KeyError:
        return redirect("nouapp:login")
def deletesmat(request, mid):
    try:
        if request.session['adminid']!=None:
            smat=Material.objects.get(mid=mid)
            smat.delete()
            return redirect("adminapp:viewmaterial")
    except KeyError:
        return redirect("nouapp:login")