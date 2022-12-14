from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..forms import *
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.models import User
from ..models import *
from django.urls import reverse

def index(request):
	if request.method == 'POST':
		form = CustomAuthForm(data=request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
			print(user)
			if user is not None:
				login(request,user)
				if user.es_estudiante:
					return redirect('AMCE:vistaAlumno')
				elif user.es_profesor:
					return redirect('AMCE:ProfMisGrupos')
	else:
		form = CustomAuthForm()
	return render(request,'index.html',{"form": form})

def signup(request):
	return render(request,"registration/signup.html")

def password_validation(request):
	return render(request,"registration/test_pass_validation.html")

"""
@csrf_exempt
def password_validation(request):
 
    valid = False
    min_strength = settings.PASSWORD_MINIMUM_ENTROPY
 
    if request.method == 'GET':
        password = request.GET["password"]
        results = password_strength(password)
 
        if results['entropy'] > min_strength:
            valid = True
 
        return JsonResponse({
            'valid': valid,
            'min_strength': min_strength,
            'results': results}
            )
"""
	