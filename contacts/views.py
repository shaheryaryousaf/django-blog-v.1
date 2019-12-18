from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']

		contact = Contact(name=name, email=email, phone=phone, message=message)
		contact.save()
		return redirect('/contact_us')
