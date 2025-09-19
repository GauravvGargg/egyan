from django.shortcuts import render, redirect
from . models import Enquiry, StudentInfo,LoginInfo 

# Create your views here.
def index(request):
    return render(request,'index.html');
def aboutus(request):
    return render(request,'aboutus.html');
def login(request):
    if request.method=='POST':
        userid=request.POST['userid']
        password=request.POST['password']
        msg=''
        try:
            obj=LoginInfo.objects.get(userid=userid,password=password)
            if obj.usertype=='student':
                request.session['userid']=userid
                return redirect('stuapp:stuhome')
        except:
            msg='Invalid User'
        return render(request,"login.html",{"msg":msg})
    return render(request,'login.html');

    
def adminlogin(request):
    if request.method=='POST':
        userid=request.POST['userid']
        password=request.POST['password']
        msg=''
        try:
            obj=LoginInfo.objects.get(userid=userid,password=password)
            if obj.usertype=='admin':
                request.session['adminid']=userid
                return redirect('adminapp:adminhome')            
        except:
            msg='Invalid User'
        return render(request,"adminlogin.html",{"msg":msg})

    return render(request,'adminlogin.html');
def registration(request):
    if request.method=='POST':
        rollno=request.POST['rollno']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        address=request.POST['address']
        program=request.POST['program']
        branch=request.POST['branch']
        year=request.POST['year']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        password=request.POST['password']
        usertype='student'
        stu=StudentInfo(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender, address=address,program=program, branch=branch,year=year, contactno=contactno, emailaddress=emailaddress)
        log=LoginInfo(userid=rollno,password=password,usertype=usertype)
        stu.save()
        log.save()
        return render(request,"registration.html",{"msg":"Registration is Done"})
    return render(request,'registration.html');
def contactus(request):
    return render(request,'contactus.html');
def saveenq(request):
    name=request.POST['name']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    enq=Enquiry(name=name, address=address, contactno=contactno, emailaddress=emailaddress, enquirytext=enquirytext)
    enq.save()
    return render(request,"contactus.html",{"msg":"Enquiry is Saved"})


    