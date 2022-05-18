from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from.models import*
from django.db.models import Q
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
#<<<<<<<<<<<<<<<<<<<<<<<< Admin >>>>>>>>>>>>>>>>>>>>>>#

@login_required(login_url='/login/')
def indexx(request):
    return render(request,'index.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.user.roles == 'admin':
              return render(request,'index.html')

        elif request.user.roles == 'doctor':
               return render(request,'index-doctor.html')

        else:
             return render(request,'index-patience.html')



    
@login_required(login_url='/login/')
def signupp(request):
    return render(request,'sign-up.html')

def logoutt(request):
     logout(request)
     messages.info(request,'Logout SuccessFully!!')
     return redirect('login')



@login_required(login_url='/login/')
def index_patiences(request):
        return render(request,'index-patience.html')


def logins(request):
    if not request.user.is_authenticated:
        form1=LoginForm()
        if request.method == 'POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                print(user)
                if user is not None:
                   print('hello')
                   login(request,user)
           
                   return redirect ('dashboard')
                else:
                    print(user.errors)
                    messages.info(request,'Enter correct username or password')
                    return render(request,'login.html',{'form':form1})
 
            else:
                print(form.errors)
                messages.info(request,'Enter correct username')
                return render(request,'login.html',{'form':form1})  

        return render(request,'login.html',{'form':form1}) 
    else:
       return redirect ('dashboard')

               
            


                

     

                   
@login_required(login_url='/login/')
def doctor_create(request):
    form1=SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Created !!')
  
            return redirect('index')
        else:
            messages.error(request,'inavlid data')
            return redirect('create_doctor')
    else:
        return render(request,'create_doctor.html',{'form':form1})   

    
             
@login_required(login_url='/login/')
def view_doctor(request):
    a=User.objects.filter(roles='doctor')
    return render(request,'list_doctor.html',{'a':a})

@login_required(login_url='/login/')
def updates_doctor(request,pk):
        uid = User.objects.get(id=pk)
        post =EditProfile(instance = uid)
        if request.method == 'POST':
            post1=EditProfile(request.POST,instance=uid)
            if post1.is_valid():
             post1.save()
             messages.success(request,'Edit Detail successfully!!')
             return redirect('list_doctor')
            
            else:
                return redirect('update_doctor')
        else:
            return render(request,'update_doctor.html',{'post':post})
   


@login_required(login_url='/login/')
def deletes_doctor(request,pk):
        uid = User.objects.get(id=pk)
        uid.delete()
        return redirect('list_doctor')




@login_required(login_url='/login/')   
def patiences_create(request):
    form1 = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Create SuccessFully!!')
            return redirect('index_patience')
        else:
            messages.error(request,'Invalid Data!!')
            return redirect('patience_create')
    else:
        return render(request,'create_patience.html',{'form':form1})


@login_required(login_url='/login/')
def view_patience(request):
        many=User.objects.all().filter(roles='patiences')
        return render(request,'list_patience.html',{'many':many})

@login_required(login_url='/login/')
def deletes_patience(request,pk):
        uid=User.objects.get(id=pk)
        uid.delete()
        return redirect('list_patience')

@login_required(login_url='/login/')
def updates_patience(request,pk):
        uid = User.objects.get(id=pk)
        post = EditProfile1(instance = uid)
        if request.method == 'POST':
            post1 = EditProfile1(request.POST,instance = uid)
            if post1.is_valid():
                post1.save()
                messages.success(request,'EDIT Profile Successfully!!')
                return redirect('list_patience')
            else:
                return redirect('index_patience')
        else:
            return render(request,'update_patience.html',{'post':post})

#<<<<<<<<<<<<<<<<<<<<<< Admin End >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

#<<<<<<<<<<<<<<<<<<<<<<< Doctor View  Start >>>>>>>>>>>>>>>>>>>>>>>>>#
@login_required(login_url='/login/')
def index_doc(request):
     return render(request,'index-doctor.html') 

@login_required(login_url='/login/')
def updates_profile(request):
        post =EditProfile(instance = request.user)
        if request.method == 'POST':
            post1=EditProfile(request.POST,instance = request.user)
            if post1.is_valid():
             post1.save()
             messages.success(request,'Edit Detail successfully!!')
             return redirect('index_doc')
            
            else:
                return redirect('update_profiles')
        else:
            return render(request,'update_doctor.html',{'post':post})

@login_required(login_url='/login/')
def appointment_views(request):
        #many=Appointment.objects.filter(slot = uid) 
        many=Appointment.objects.all()
        return render(request,'appointment-view.html',{'many':many})

@login_required(login_url='/login/')
def appointment_status(request):
        many = Appointment.objects.filter(user=request.user)
        print(many)
        return render(request,'appointment-status.html',{'many':many})



@login_required(login_url='/login/')
def slot_add(request):
        form1 = SlotForm()
        if request.method=='POST':
            form = SlotForm(request.POST)
            print(form)
            if form.is_valid():
                print(form)
                f=form.save(commit=False)
                f.doctor_id = request.user
                f.save()
                messages.info(request,'Slot Addded SuccessFully!!')
                return redirect('slots')
            else:
                print(form.errors)
                messages.error(request,'ERROR!!')

                return redirect('slots')
           
        else:
            return render(request,'slot.html',{'form':form1})

@login_required(login_url='/login/')
def view_slots(request):
        many = Slot.objects.all().order_by('weeks')
        return render(request,'view-slot.html',{'many':many})

        
@login_required(login_url='/login/')
def update_slots(request,pk):
       uid=Slot.objects.get(id=pk)
       form1=Slotupdate(instance = uid)
       if request.method == 'POST':
           form = Slotupdate(request.POST,instance = uid)
           if form.is_valid():
               form.save()
               return redirect('view-slot')
           else:
               return redirect('update-views')
       else:
            return render(request,'update-slot.html',{'form':form1})
    
           
        
@login_required(login_url='/login/')      
def delete_slots(request,pk):
        id=Slot.objects.get(id=pk)
        id.delete()
        return redirect('view-slot')


#<<<<<<<<<< patience >>>>>>>>>>>>>>>>>>>>>>>>>>>>#

@login_required(login_url='/login/')
def profile_patience(request):
        form1=Profile(instance=request.user)
        if request.method == 'POST':
           form=Profile(request.POST,request.FILES,instance = request.user) 
           if form.is_valid():
               form.save()
               return redirect('index_patience')
           else:
                return redirect('patience-edit')
        else:
            return render(request,'patience-edit.html',{'form':form1})

@login_required(login_url='/login/')
def doctor_view(request):
    user=User.objects.filter(roles='doctor')
    return render(request,'doctor-view.html',{'user':user})

@login_required(login_url='/login/')    
def available_slot(request,pk):
    user=User.objects.get(id=pk)
    slot=Slot.objects.filter(doctor_id = user)
    return render(request,'slot-detail.html',{'user':user,'slot':slot})

@login_required(login_url='/login/')
def appointments_form(request,pk):
        user=User.objects.get(email=request.user.email)
        data=Slot.objects.get(id=pk)
        print(data)
       
        if request.method =='POST':
            data.slotsize -= 1
            data.save()

            Appointment.objects.create(
            name=request.POST['name'],
            user=user,
            slot=data,
            description = request.POST['description'],
            )
            return render(request,'appointment-form.html',{'msg':'Appointment Send To Doctor Successfully!!','user':user,'data':data})
        else:
            return render(request,'appointment-form.html',{'user':user,'data':data})



#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< status >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

def complete_status(request,pk):
    uid = Appointment.objects.get(id=pk)
    uid.status = 1
    uid.save()
    return redirect('appointment-views')

def absent_status(request,pk):
    uid = Appointment.objects.get(id=pk)
    uid.status = 2
    uid.save()
    return redirect('appointment-views')

def cancel_status(request,pk):
    uid = Appointment.objects.get(id=pk)
    uid.status = 3
    uid.save()
    return redirect('appointment-views')


