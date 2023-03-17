import datetime
from django.shortcuts import render, redirect
from farmland.settings import *
from django.core.files.storage import FileSystemStorage
from . models import *
from django.contrib.auth.models import User, auth
import requests
from django.contrib import messages


from django.http import HttpResponse


def home(request):
    mkm = STATIC_DIR
    return render(request,'home.html',{'mkm':mkm})


def about(request):
    return render(request,'about.html')


def blog(request):
    return render(request,'blog.html')


def contact(request):
    return render(request,'contact.html')


def detail(request):
    return render(request,'detail.html')


def feature(request):
    return render(request,'feature.html')


def product(request):
    return render(request,'product.html')


def services(request):
    return render(request,'services.html')


def team(request):
    return render(request,'team.html')


def testimonial(request):
    return render(request,'testimonial.html')


def admin(request):
    return render(request,'admin_register.html')


def worker(request):
    return render(request,'worker_register.html')


def blogcarousel(request):
    return render(request,'blog-carousel.html')


def testimonials(request):
    return render(request,'testimonials.html')


def agricultureprd(request):
    return render(request,'agriculture-products.html')


def blogdetails(request):
    return render(request,'blog-details.html')


def blogsidebar(request):
    return render(request,'blog-sidebar.html')


def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')


def diaryproducts(request):
    return render(request,'dairy-products.html')


def faq(request):
    return render(request,'faq.html')


def farmers(request):
    return render(request,'farmers.html')


def farmerscarousel(request):
    return render(request,'farmers-carousel.html')


def freshvegetables(request):
    return render(request,'fresh-vegetables.html')


def organicproducts(request):
    return render(request,'organic-products.html')


def productdetails(request):
    return render(request,'product-details.html')


def products(request):
    return render(request,'products.html')


def project1(request):
    return render(request,'project-01.html')


def project2(request):
    return render(request,'project-02.html')


def projectcarousel(request):
    return render(request,'project-carousel.html')


def projectdetails(request):
    return render(request,'project-details.html')


def servicescarousel(request):
    return render(request,'services-carousel.html')


def testimonialscarousel(request):
    return render(request,'testimonials-carousel.html')


def registration(request):
    if request.method == 'POST':
        x = datetime.datetime.now()
        y = x.strftime("%Y-%m-%d")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(photo.name, photo)
        reg1 = Registration.objects.all()
        for i in reg1:
            if i.Email == email:
                messages.success(request, 'User already exists')
                return render(request, 'registration.html')

        user_name = request.POST.get('user_name')
        for t in User.objects.all():
            if t.username == user_name:
                messages.success(request, 'Username taken. Please try another')
                return render(request, 'registration.html')

        user = User.objects.create_user(username=user_name, email=email, password=psw)
        user.save()

        t = Registration()
        t.First_name = first_name
        t.Last_name = last_name
        t.Email = email
        t.Password = psw
        t.Registration_date = y
        t.Image = photo
        t.About_website = 'Nil'
        t.User_role = 'admin'
        t.user = user
        t.save()
        messages.success(request, 'You have successfully registered as admin')
        return redirect('home')
    else:
        return render(request, 'registration.html')


def registrationworker(request):
    if request.method == 'POST':
        x = datetime.datetime.now()
        y = x.strftime("%Y-%m-%d")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(photo.name, photo)
        reg1 = Registration.objects.all()
        for i in reg1:
            if i.Email == email:
                messages.success(request, 'User already exists')
                return render(request, 'registration-worker.html')

        user_name = request.POST.get('user_name')
        for t in User.objects.all():
            if t.username == user_name:
                messages.success(request, 'Username taken. Please try another')
                return render(request, 'registration-worker.html')

        user = User.objects.create_user(username=user_name, email=email, password=psw)
        user.save()
        t = Registration()
        t.First_name = first_name
        t.Last_name = last_name
        t.Email = email
        t.Password = psw
        t.Registration_date = y
        t.Image = photo
        t.About_website = 'Nil'
        t.User_role = 'worker'
        t.user = user
        t.save()
        messages.success(request, 'You have successfully registered')
        return redirect('home')
    else:
        return render(request, 'registration-worker.html')


def registrationstaff(request):
    return render(request,'registration-staff.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Invalid credentials')
            return render(request, 'login.html')
        auth.login(request, user)
        if Registration.objects.filter(Password=password).exists():
            logs = Registration.objects.filter(Password=password)
            for value in logs:
                user_id = value.id
                usertype = value.User_role
                if usertype == 'admin':
                    request.session['logg'] = user_id
                    return redirect("adminhome")

                elif usertype == 'worker':
                    request.session['logg'] = user_id
                    return redirect('workerhome')

                elif usertype == 'student':
                    request.session['logg'] = user_id
                    return redirect('staffhome')
                else:
                    messages.success(request, 'Your access to the website is blocked. Please contact admin')
                    return render(request, 'login.html')
        else:
            messages.success(request, 'Username or password entered is incorrect')
            return render(request, 'login.html')
    return render(request, 'login.html')

def userhome(request):
    return render(request, 'userhome.html')



def staffhome(request):
    return render(request,'staff-home.html')


def adminhome(request):
    return render(request,'admin-home.html')


def workerhome(request):
    return render(request,'worker-home.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def schedule_work(request):
    fd = Registration.objects.filter(User_role = 'worker')
    if request.method == 'POST':
        scd = request.POST.get('scd')
        worker = request.POST.get('worker')
        worker = int(worker)
        k = Registration.objects.get(id = worker)
        mv = Schedule_worker()
        mv.work = scd
        mv.work_reg = k
        mv.save()
        messages.success(request,'Scheduled successfully')
        return redirect('adminhome')
    return render(request,'schedule_work.html',{'fd':fd})


def work_schedule(request):
    m = Registration.objects.get(id = request.session['logg'])
    hgh = Schedule_worker.objects.filter(work_reg = m)
    return render(request,'work_schedule.html',{'hgh':hgh})
