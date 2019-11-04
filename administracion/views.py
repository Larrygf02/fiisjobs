#from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from administracion.forms import UploadForm
from administracion.models import Document

#from somewhere import handle_uploaded_file

def upload_file(request):
	if request.method == 'POST':
		form = UploadForm(request.POST,request.FILES)
		if form.is_valid():
			newdoc = Document(filename = request.POST['filename'],docfile = request.FILES['docfile'])
			newdoc.save(form)
			return redirect("uploads")
	else:
		form = UploadForm()
	return render(request,'administracion/upload.html',{'form':form})

def my_view(request):
	return render(request,'administracion/my_template.html',{"usuario":"administrador"})

