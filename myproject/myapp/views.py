from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# def home(request):
#     return HttpResponse("Akansha's here...!!")

# def home1(request):
#     return render(request,'index.html')

# def home(request):
#     data={
#         'name':'Akansha',
#         'age':23,
#         'qualifi':'Btech'
#     }
#     data1={
#         'name':'Aastha',
#         'age':21,
#         'qualifi':'Bcom'
#     }
#     data2={
#         'name':'shristy',
#         'age':20,
#         'qualifi':'Bca'
#     }
#     # return render(request,'index.html',data)
#     return render(request,'index.html',{'key1':data,'key2':data1,'key3':data2})

# def collection(request):
#     data=[{'name':'Akansha','age':23,'city':'Pune'},
#           {'name':'Aastha','age':21,'city':'Delhi'},
#           {'name':'Shristy','age':20,'city':'Indore'},
#           {'name':'Rohan','age':22,'city':'Bhopal'}]
#     return render(request,'collection.html',{'data':data})

# def filter(request):
# #     return render(request,'filter.html',{'value':10})
#     return render(request,'filter.html',{'value':"my name is akansha bagde"})

def form(request):
    return render(request,'form.html')

def register(request):
    return render(request,'register.html')

# def login(request):
#     if request.method=='POST':
#         name=request.POST.get('nm')
#         password=request.POST.get('ps')
#         # print(name,password)
#         name1=request.COOKIES['name']
#         contact=request.COOKIES['contact']
#         email=request.COOKIES['email']
#         password1=request.COOKIES['password']
#         # print(name1,contact,email,password1)
#         if name1==name:
#             if password1==password:
#                 data={'name1':name,
#                       'contact1':contact,
#                       'email1':email,
#                       'password1':password
                     
#                 }
#                 return render(request,'dashboard.html',data)
#             else:
#                 msg="name and password not matched"
#                 return render(request,'login.html',{'msg':msg})
#         else:
#             msg="name not registered"
#             return render(request,'login.html',{'msg':msg})

        
#     else:
#         return render(request,'login.html')

    

# def rdata(request):
#     print(request.method)
#     print(request.POST)
#     cstoken=request.POST.get('csrfmiddlewaretoken')
#     name=request.POST.get('nm')
#     contact=request.POST.get('ct')
#     email=request.POST.get('em')
#     password=request.POST.get('ps')
#     print(cstoken)
#     print(name)
#     print(contact)
#     print(email)
#     print(password)
#     response=render(request,'login.html')
#     response.set_cookie('name',name,max_age=60*60*24,)
#     response.set_cookie('contact',contact)
#     response.set_cookie('email',email)
#     response.set_cookie('password',password)
#     return response

def logout(request):
    response=render(request,'register.html')
    response.delete_cookie('name')
    response.delete_cookie('contact')
    response.delete_cookie('email')
    response.delete_cookie('password')
    return response

# def userlogin(request):
#     if request.method=='POST':
#         name=request.POST.get('nm')
#         password=request.POST.get('ps')
#         print(name,password)

def rdata(request):
    if request.method=='POST':
        name=request.POST.get('nm'),
        email=request.POST.get('em'),
        contact=request.POST.get('ct'),
        password=request.POST.get('ps')
        data={
            'name':name,
            'email1':email,
            'contact':contact,
            'password1':password
        }
        request.session['data']=data
        return render(request,'login.html')
    else:
        return render(request,'form.html')
    
def login(request):  
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        # password=request.POST['password']
        data1=request.session.get('data')
        # print(data1)
        # print(data1["name"],data1["email1"],data1["contact"],data1["password1"])
        if data1['name']==name:
            
            if data1['password1']==password:
                my_data={
                    'nm':data1['name'],
                    'em':data1['email1'],
                    'con':data1['contact'],
                    'pas':data1['password1']
                }
                return render(request,'dashboard.html',my_data)
            else:
                msg="Password is inccorrect"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Name is incorrect"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
        


    