from django.shortcuts import redirect

def index(request):
	"""
	Redirect to admin 
	"""
	return redirect('admin:index')
