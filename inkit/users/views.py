from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,Skill , Message
from django.db.models import Q 
from django.contrib import messages
from .forms import CustomUserCreationForm,MessageForm
from .utils import searchProfiles,paginateProfiles

# Create your views here.

def loginUser(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"user does not exist")
            
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'profiles' )
        else:
            messages.error(request,'username or password incorrect')

    return render(request,'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request,'Successfully logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
 
    if request.method == 'POST':
        
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            
            
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request,'User registered successfully')
            
            login(request,user)
            return redirect('profiles')
        else:
            messages.success(request,'An error occured')
    
        
    context = { 'page':page , 'form':form}
    
    return render(request,'users/login_register.html',context)


def profiles(request):      

    search_query = ''
    profiles,search_query = searchProfiles(request)
    custom_range,profiles = paginateProfiles(request,profiles,3)

    context = {'profiles':profiles , 'search_query':search_query, 'custom_range':custom_range}
    return render(request,'users/profiles.html',context)

def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile':profile,'topSkills':topSkills,'otherSkills':otherSkills}
    return render(request,'users/user-profile.html',context)



@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.Messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {
        'messageRequests':messageRequests,
        'unreadCount':unreadCount,
    }
    return render(request,'users/inbox.html',context)

@login_required(login_url='login')
def viewMessage(request,pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context= {
        
        'message':message,

    }
    return render(request,'users/message.html',context)

def createMessage(request,pk):

    recipient = Profile.objects.get(id=pk) 
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            
            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request,'Message sent')
            return redirect('user-profile',pk=recipient.id)




    context = {
        'recipient':recipient,
        'form':form,
    }
    return render(request,'users/message_form.html',context)
