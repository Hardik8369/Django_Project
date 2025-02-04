from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def aboutus(request):
    return render(request,'aboutus.html')
@login_required(login_url='login')
def index(request):
 
    return render(request,'index.html')
@login_required(login_url='login')
def predict(request):
   if(request.method=="POST"):
      data=request.POST
      hours=float(data.get('texthours'))
      age=int(data.get('textage'))
      internet=bool(data.get('textinternet'))
      if('buttonadd' in request.POST):
         import pandas as pd
         path="C:\\Users\\gowda\\OneDrive\\Desktop\\Data\\Data\\Exammarks.csv"
         data=pd.read_csv(path)
         medianvalue=data.hours.median()
         data.hours=data.hours.fillna(medianvalue)
         inputs=data.drop('marks','columns')
         output=data.drop(['hours','age','internet'],'columns')
         import sklearn
         from sklearn import linear_model
         model=linear_model.LinearRegression()
         model.fit(inputs,output)
         result=model.predict([[hours,age,internet]])
         return render(request,'predict.html',context={'result':"Marks="+str(result)})
   return render(request,'predict.html')

@login_required(login_url='login')
def counter(request):
    if(request.method=="POST"):
        data=request.POST
        result=data.get('textresult')
        if result=="":
            result=0
        else:
            result=int(data.get('textresult'))
        if('buttonincrement' in request.POST):
            result=result+1
            return render(request,'counter.html',context={'result':result})
        if('buttondecrement' in request.POST):
            result=result-1
            return render(request,'counter.html',context={'result':result})
        if('buttonreset' in request.POST):
            result=0
            return render(request,'counter.html',context={'result':result})

    return render(request,'counter.html')

@login_required(login_url='login')
def register(request):
    if(request.method=="POST"):
        data=request.POST
        firstname=data.get('textfirstname')
        lastname=data.get('textlastname')
        if('buttonsubmit' in request.POST):
            result=firstname+" "+lastname
            return render(request,'register.html',context={'result':result})

    return render(request,'register.html')
@login_required(login_url='login')
def calci(request):
    if(request.method=="POST"):
        data=request.POST
        firstnumber=int(data.get('textfirstnumber'))
        secondnumber=int(data.get('textsecondnumber'))
        print(firstnumber)
        print(secondnumber)
        if('buttonadd' in request.POST):
            result=firstnumber+secondnumber
            return render(request,'calci.html',context={'result':"Sum="+str(result)})
        if('buttonsub' in request.POST):
            result=firstnumber-secondnumber
            return render(request,'calci.html',context={'result':"Sub="+str(result)})
        if('buttonmul' in request.POST):
            result=firstnumber*secondnumber
            return render(request,'calci.html',context={'result':"Mul="+str(result)})
        if('buttondiv' in request.POST):
            result=firstnumber/secondnumber
            return render(request,'calci.html',context={'result':"Div="+str(result)})
        

    return render(request,'calci.html')
@login_required(login_url='login')
def department(request):
    if(request.method=="POST"):
        data=request.POST
        deptname=data.get('textdepartmentname')
        deptdesc=data.get('textdepartmentdesc')
        StudentDepartment.objects.create(DEPT_NAME=deptname,DEPT_DESC=deptdesc)
        result="Department Details saved Succefully"
        return render(request,'department.html',context={'result':result})


    return render(request,'department.html')
@login_required(login_url='login')
def departmentview(request):
    getdepartment=StudentDepartment.objects.all()
    return render(request,'departmentview.html',context={'getdepartment':getdepartment})
@login_required(login_url='login')
def departmentupdate(request,id):
  getdepartments=StudentDepartment.objects.get(id=id)
  if(request.method=="POST"):
    data=request.POST
    deptname=data.get('textdepartmentname')
    deptdesc=data.get('textdepartmentdesc')
    getdepartments.DEPT_NAME=deptname
    getdepartments.DEPT_DESC=deptdesc
    getdepartments.save()
    return redirect('/departmentview/')
  return render(request,'departmentupdate.html',context={'getdepartments':getdepartments})
@login_required(login_url='login')
def departmentdelete(request,id):
  getdepartments=StudentDepartment.objects.get(id=id)
  if(request.method=="POST"):
    data=request.POST
    getdepartments.delete()
    return redirect('/departmentview/')
  return render(request,'departmentdelete.html',context={'getdepartments':getdepartments})
@login_required(login_url='login')
def Employee(request):
  if(request.method=="POST"):
    data=request.POST
    empname=data.get('textdepartmentname')
    empdes=data.get('textdepartmentdesc')
    empplace=data.get('textdepartmentplace')
    Employee_Table.objects.create(EMP_NAME=empname,EMP_DESI=empdes,EMP_PLACE=empplace)
    result="Employee Details saved Succefully"
    return render(request,'Employee.html',context={'result':result})
  return render(request,'Employee.html')
@login_required(login_url='login')
def Employee_details(request):
  getEmployee=Employee_Table.objects.all()
  return render(request,'Employee_details.html',context={'getEmployee':getEmployee})

@login_required(login_url='login')
def Employee_update(request,id):
  getEmployee=Employee_Table.objects.get(id=id)
  if(request.method=="POST"):
    data=request.POST
    empname=data.get('textdepartmentname')
    empdes=data.get('textdepartmentdesc')
    empplace=data.get('textdepartmentplace')
    getEmployee.EMP_NAME=empname
    getEmployee.EMP_DESI=empdes
    getEmployee.EMP_PLACE=empplace
    getEmployee.save()
    return redirect('/Employee_details/')
  return render(request,'Employee_update.html',context={'getEmployee':getEmployee})

@login_required(login_url='login')
def Employee_delete(request, pk):
    employee = Employee_Table.objects.get(id=pk)
    if request.method == "POST":
       employee.delete()
       return redirect("Employee_details")
    
    context = {
        "employee":employee,
    }

    return render(request, "Employee_delete.html", context)

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=User.objects.filter(username=username)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
          login(request,user)
          return redirect('index')
        else:
            result="Password Entered is wrong"
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')