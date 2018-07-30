# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
@csrf_exempt
#def reg(request):
#	response1=render(request,'register.html',{})
#	return response1
def start(request):
	if 'username' in request.session:
		return redirect('/student')
	else:
		return redirect('/main')
def register(request):	
	context={}
	if request.method=='GET':
		return render(request,'register.html',{})
	elif request.method=='POST':
	#context['message']=message
		name=request.POST['name']
		username=request.POST['username']
		password=request.POST['password']
		contact=request.POST['contact']
		user_type=request.POST['user_type']
		rollno=request.POST['rollno']
		gender=request.POST.get('gender',Male)
		dept=request.POST.get('dept',EnTC)
		dob=request.POST['dob']
		passwordcheck=request.POST['passwordcheck']

		if user.objects.filter(username=username).exists():
			context['msg']='Username already exists'
			return render(request,'register.html',context)
		elif password!=passwordcheck: 
			context['msg']='Passwords did not match'
			return render(request,'register.html',context)

		else:
			aa=user(
			name=name,
			username=username,
			password=password,
			contact=contact,
			user_type=user_type,
			rollno=rollno,
			gender=gender,
			dept=dept,
			dob=dob
			)
			aa.save()

			context['name']=name
			context['password']=password
			context['username']=username
			context['contact']=contact
			context['user_type']=user_type
			context['dob']=dob
			context['gender']=gender
			context['dept']=dept
			context['rollno']=rollno
			return render(request,'main.html',context)
	#response1=render(request,'register.html',context)	
	#Sreturn response1
#@csrf_exempt
#def login_response(request):
#	response2=render(request,'login.html',{})
#	return response2
@csrf_exempt
def login(request):
	if "username" in request.session:
		if request.session['user_type']=='librarian':
			return redirect('/librarian')
		else:
			return redirect('/student')
	if request.method=='GET':
		response2=render(request,'login.html',{})
		return response2
	elif request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		context={}
		if user.objects.filter(username=username).exists():
			user_obj=user.objects.get(username=username)
			if user_obj.password==password:
				request.session['username']=user_obj.username
				request.session['user_type']=user_obj.user_type
				if user_obj.user_type == 'librarian':
					print 'Librarian'
					return redirect('/librarian')
				elif user_obj.user_type == 'student':
					print 'Student'
					return redirect('/student')
		
			else:
				msg='Password incorrect'
				context['msg']=msg			
				return render(request,'main.html',context)
		else:
			msg='User Not found'
			context['msg']=msg
			response2=render(request,'main.html',context)
			return response2
	
def librarian(request):
	if "username" in request.session:
		if request.session['user_type']=='student':
			return redirect('/login')
		else:
			context={}
			obj=books.objects.all()
			context['books']=obj
			return render(request,'librarian.html',context)
	else:
		return redirect('/login')
def student(request):
	if "username" in request.session:
		if request.session['user_type']=='librarian':
			return redirect('/login')
		else:
			context={}
			obj=books.objects.all()
			context['books']=obj
			return render(request,'student.html',context)
	else:
		return redirect('/login')
@csrf_exempt
def logout_user(request):
	if "username" in request.session:
		del request.session['username']
		del request.session['user_type']
		return redirect('/main')
	
	return redirect('/login')
def book_details(request):
	context={}
	id1=request.GET['book_id']
	user_obj=books.objects.get(id=id1)
	context['name']=user_obj.name	
	context['author']=user_obj.author
	context['summary']=user_obj.summary
	
	return render(request,'book_details.html',context)
def student_profile(request):
	if "username" in request.session:
		us1=request.session['username']
		context={}
		user_obj=user.objects.get(username=us1)
		context['username']=user_obj.username
		context['name']=user_obj.name		
		context['dept']=user_obj.dept
		context['gender']=user_obj.gender
		context['dob']=user_obj.dob
		context['rollno']=user_obj.rollno

		return render(request,'student_profile.html',context)
	else:
		return redirect('/login')
@csrf_exempt
def book_search(request):
	context={}
	name=request.POST['name']
	author=request.POST['author']
	genre=request.POST['genre']
	book_obj=books.objects.filter(Q(name=name)|Q(author=author)|Q(genre=genre))
	context['list']=book_obj
	return render (request,'book_search.html',context)
@csrf_exempt  	 
def main_page(request):
	
	return render(request,'main.html',{})

def book_list(request):
	context={}
	obj=books.objects.all()
	context['books']=obj
	return render(request,'book_list.html',context)

def home(request):
	return render(request, 'home.html')
		
	#return render (request,'book_search.html',context)
	
# Create your views here.
