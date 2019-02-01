from django.shortcuts import render

def home(request):
	return render(request,"home.html",{})

def about(request):
	my_name = "I am Jahanzeb Khurshid"
	return render(request,"about.html",{"my_name":my_name})

def contact(request):
	return render(request,"contact.html",{})

def product(request):
	return render(request,"product.html",{})
