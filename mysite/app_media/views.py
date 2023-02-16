from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm, DocumentForm, MultiFileForm
from .models import File


def upload_file(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=file.name, status=200)

    else:
        upload_file_form = UploadFileForm()
        context = {
            'form': upload_file_form
        }
        return render(request, 'app_media/upload_file.html', context=context)


def model_form_upload(request: HttpRequest):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/files/upload_file')
    else:
        form = DocumentForm()
    return render(request, 'app_media/file_form_upload.html', {'form': form})


def upload_files(request: HttpRequest):
    if request.method == 'POST':
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)
                instance.save()
            return redirect('/files/upload_file')
    else:
        form = MultiFileForm()
    return render(request, 'app_media/create_post.html', {'form': form})
