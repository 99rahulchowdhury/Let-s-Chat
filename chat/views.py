from django.shortcuts import render as re
from django.shortcuts import redirect as rd
from django.http import HttpResponse, JsonResponse
from chat.models import Users,Message
from datetime import datetime
import random as r
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Create your views here.
ottt=0
new_password=0
new_usersss=0
def otp():
    return int(r.uniform(1000,4444))
def send_email(email,ot):
            try:
                msg = MIMEMultipart()
                print("[+] Message Object Created")
            except:
                print("[-] Error in Creating Message Object")
                return
            fromaddr='monsterrazzy@gmail.com'
            toaddr=email

            msg['From'] = fromaddr

            msg['To'] = toaddr

            msg['Subject'] = 'Reset Password'
            # ot=color.BOLD + str(ot) + color.END
            print(ot)
            body = 'Your OTP is:'+str(ot)

            msg.attach(MIMEText(body, 'plain'))

          

          

            

            try:
                s = smtplib.SMTP('smtp.gmail.com', 587) 
                # s = smtplib.SMTP('stud.iitp.ac.in', 587)
                print("[+] SMTP Session Created")
            except:
                print("[-] Error in creating SMTP session")
                return

            s.starttls()

            try:
                s.login(fromaddr, 'qekborrfsfieqpsh')
                print("[+] Login Successful")
            except:
            
                print("[-] Login Failed")

            text = msg.as_string()

            try:
                s.sendmail(fromaddr, toaddr, text)
                print("[+] Mail Sent successfully")
            except:
                print('[-] Mail not sent')

            s.quit()

def home(request):
    return re(request,'home.html')



def room(request,room):
    username = request.GET.get('username')
    
   
    a=Users.objects.filter(name=username)
    
    # return re(request,'room.html')
    return re(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room,
      
        
    })
    
    




def checkrecipent(request):
    room=request.POST['rn']
    ff=request.POST['sg']
   
    # if(Message.objects.filter(user=ff,recipent=room).exists()):
    #     return rd('/'+room+'/?userame='+ff)
    # else:
    #     ss=Message.objects.create(user=)
    #     ss.save()
    return rd('/'+room+'/?username='+ff)

    # if(Users.objects.filter(name=recipent_name).exists()):
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    # print(message)
    # print(username,'->',room_id)

    
    new_message = Message.objects.create(value=message, user=username,recipent=room_id,xx=str(datetime.now()))
    new_message.save()
    return HttpResponse('Message sent successfully')   

def getMessages(request, room,username):
    room_details = Users.objects.get(name=room)
    # print(username+'->'+room)
    messages1= Message.objects.filter(user=room,recipent=username)
    messages2=Message.objects.filter(user=username,recipent=room)
    a1=[]
 
    for i in (list(messages1.values())):
        a1.append([i['xx'],i,0])
    for i in (list(messages2.values())):
        a1.append([i['xx'],i,1])
    a1.sort()
    # print(a1)
    ans=[]
    for i in a1:
        ans.append(i[1])
    value=[]
    for i in a1:
        value.append(i[2])
    a=Users.objects.filter(name=room);
    b=Users.objects.filter(name=username);
    a=list(a.values())
    b=list(b.values())
    
    meimg=a[0]['image']
    reimg=b[0]['image']
    nickname=b[0]['nickname']
    

 


    return JsonResponse({"messages":ans,'value':value,'nickname':nickname,'meimg':meimg,'reimg':reimg})
 
def data(request):
    nic=request.GET.get('ni')
    

    u=request.GET.get('Choose')
    print(u)
    usrname,img=u.split(' ')
    a= Users.objects.get(name=usrname)
    
    a.nickname=nic
    a.image=img

    a.save()
  
 
    return re(request,'recipent.html',{'usern':usrname})


def check(request):
    user_name=request.GET.get('em',0)
    user_password=request.GET.get('ps',0)
    user_signup=request.GET.get('sb',0)
    user_login=request.GET.get('lb',0)
    user_log=request.GET.get('submit2',0)
    print(user_signup)
    print(user_login)
    if(user_log):
        
        if(Users.objects.filter(name=user_name).exists()):
            if(Users.objects.filter(name=user_name,password=user_password).exists()):

                return re(request,'recipent.html',{'usern':user_name})
            else:
                return re(request,'back.html')
    if(user_signup):
        if(Users.objects.filter(name=user_name).exists()):
            return re(request,'back.html')
        
        else:
            new_username=Users.objects.create(name=user_name,password=user_password)
            new_username.save()
            
            return re(request,'data.html',{'usern':user_name})
    elif(user_login):

        if(Users.objects.filter(name=user_name).exists()):
            if(Users.objects.filter(name=user_name,password=user_password).exists()):

                return re(request,'recipent.html',{'usern':user_name})
            else:
                return re(request,'back.html')

        else:
    
            
            return re(request,'Login.html')
    else:
        return re(request,'forgot.html')    
def forgot(request):
    global ottt
    global new_password
    global new_usersss
    username=request.POST['nm']
    email=request.POST['em']
    password=request.POST['pss']
    
    submit=request.POST['sl']

    if(submit):
        new_usersss=username
        new_password=password
        ot=otp()
        ottt=ot
        send_email(email,ot)
        return re(request,'otp.html',{'email':email})
def otpp(request):
    
    f=request.POST['first']
    s=request.POST['second']
    t=request.POST['third']
    fo=request.POST['fourth']
    sp=request.POST['sp']
    
    if(sp):
        x=f+s+t+fo
        print(x)
        if(str(ottt)==x):
            a= Users.objects.get(name=new_usersss)
    
            a.password=new_password
        

            a.save()
            
            return re(request,'pass.html')
    
        

