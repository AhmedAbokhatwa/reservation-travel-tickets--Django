from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from products.models import Product
from django.contrib import auth
from .models import UserProfile
import re

# Create your views here.


def signin(request):
    if request.method =='POST' and 'signinbtn' in request.POST:
        username = request.POST['username']
        password =request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if 'rememberme' not in request.POST:
                request.session.set_expiry(0)
            auth.login(request,user)
            #messages.success(request,'you are login')
        else:
            messages.error(request,'you username or password is not correct')
        messages.info(request,'this is post')
        return redirect('signin')
    else:
         return render(request,'accounts/signin.html')
    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('index') 

def signup(request):
    if request.method =='POST' and 'signupbtn' in request.POST:
        #variables
        fname = None
        lname = None
        address = None
        address2 = None
        city = None
        state = None
        zip_number = None
        email = None
        username = None
        password = None
        terms = None
        is_added = None
        # get value from the form 'fname'is variable
        if 'fname' in request.POST: 
            fname = request.POST['fname']
        else: 
            messages.error(request,'error in first name')
        if 'lname' in request.POST: 
            lname = request.POST['lname']
        else: 
            messages.error(request,'error in last name')
        if 'address' in request.POST: 
            address = request.POST['address']
        else: 
            messages.error(request,'error address')
        if 'address2' in request.POST: 
            address2 = request.POST['address2']
        else: 
            messages.error(request,'error address2')
        if  'state' in request.POST: 
            state = request.POST['state']
        else: 
            messages.error(request,'error state')
        if 'city' in request.POST: 
            city = request.POST['city']
        else: 
            messages.error(request,'error city')
        if 'email' in request.POST: 
            email = request.POST['email']
        else: 
            messages.error(request,'error email')
        if 'zip' in request.POST: 
            zip_number= request.POST['zip']
        else: 
            messages.ERROR(request,'error zip')
        if 'username' in request.POST: 
            username = request.POST['username']
        else: 
            messages.error(request,'error username')
        if 'password' in request.POST: 
            password = request.POST['password']
        else: 
            messages.error(request,'error password')
        if 'terms' in request.POST: 
            terms = request.POST['terms']
            #check the valye
        if fname and lname and address and address2 and state and city and zip_number and username and email and password:
            if terms == 'on':
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'user is exist')
                    #email
                else:
                     if User.objects.filter(email=email).exists():
                        messages.error(request, 'email is exist')
                     else:   
                        patt="\w+(-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*"
                        if re.match(patt,email):
                            user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                            user.save()
                            userprofile = UserProfile(user=user,address=address,address2=address2,city=city,state=state,zip_number=zip)
                            userprofile.save()
                            #CLEAR FILEDS 
                            fname = None
                            lname = None
                            address = None
                            address2 = None
                            city = None
                            state = None
                            zip_number = None
                            email = None
                            username = None
                            password = None
                            terms = None
                            messages.success(request,'your account is added')
                            is_added = True
                            messages.success(request,'account is created')
                        else:
                            messages.error(request, 'email is invaild') 
            else: 
                 messages.error(request, 'you must agree the terms')
        else:        
            messages.error(request, 'check empty filed')
          
        return render(request,'accounts/signup.html',{  
            'fname':fname,
            'lname':lname,
            'address':address,
            'address2':address2,
            'city':city,
            'state':state,
            'email':email,
            'password':password,
            'zip':zip_number,
            'username':username,
            'is_added':is_added

            
        })
    else:
        return render(request,'accounts/signup.html')


def profile(request):
    if request.method == 'POST' and 'savebtn'in request.POST:
        if request.user is not None and request.user.id != None:
            userprofile = UserProfile.objects.get(user=request.user)
            if request.POST['fname'] and request.POST['lname'] and request.POST['address'] and request.POST['address2'] and request.POST['city'] and request.POST['state'] and request.POST['zip'] and request.POST['email'] and request.POST['password'] and request.POST['username']:
                request.user.first_name = request.POST['fname']
                request.user.last_name = request.POST['lname']
                userprofile.address = request.POST['address']
                userprofile.address2 = request.POST['adress2']
                userprofile.city = request.POST['city']
                userprofile.state = request.POST['state']
                userprofile.zip = request.POST['zip']
                request.user.email = request.POST['email']
                #request.user.password = request.POST['password']
                if not request.POST['password'].startwith('pbkdf2_sha256$'):
                   request.user.set_password(request.user.POST['pass'])
                request.user.username = request.POST['username']


            else:
                messages.error(request,'errror in elements')    
        return redirect('profile')
    
    else:   
        if request.user is not None:
            if request.user.id != None:   
                userprofile = UserProfile.objects.get(user=request.user)

                context = {
                            'fname':request.user.first_name,
                            'lname':request.user.first_name,
                            'address':userprofile.address,
                            'address2':userprofile.address2,
                            'city':userprofile.city,
                            'state':userprofile.state,
                            'zip':userprofile.zip_number,
                            'user':request.user.username,
                            'email':request.user.email,
                            'password':request.user.password,
                }
                return render(request,'accounts/profile.html',context)       
        else:
           return render(request,'accounts/profile.html')
        
def product_favorite(request,pro_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        pro_fav = Product.objects.get(pk=pro_id)
        if UserProfile.objects.filter(user=request.user,product_favorites=pro_fav).exists:
            messages.success(request,'already product in favorite list')
        else:
            userprofile=UserProfile.objects.get(user=request.user)
            userprofile.product_favorites.add(pro_fav)    
            messages.success(request,' product has been in favorite ')
            return redirect('/products/'+str(pro_id))
    
def show_product_favorite(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        context=None
        userinfo=UserProfile.objects.get(user=request.user)
        pro=userinfo.product_favorites.all()
        context={
            'products':pro
        }
        return render(request,'products/products.html',context)