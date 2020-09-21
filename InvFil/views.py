from django.shortcuts import render
#from django.http import HttpResponse
from .forms import UploadFileForm
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			filter(request.FILES['file'])
	return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the index.")
