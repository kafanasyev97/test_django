from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import UserBioForm, UploadFileForm


def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    result = a + b
    context = {
        'a': a,
        'b': b,
        'result': result,
    }
    return render(request, 'requestdataapp/request-query-params.html', context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    context = {
        'form': UserBioForm(),
    }
    return render(request, 'requestdataapp/user-bio-form.html', context=context)


MAX_UPLOAD_SIZE = "1000000"
def handle_file_upload(request: HttpRequest) -> HttpRequest:
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # myfile = request.FILES["myfile"]
            myfile = form.cleaned_data['file']
            if myfile.size < int(MAX_UPLOAD_SIZE):
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                print("saved file", filename)
            else:
                raise ValidationError('File too large. Size should not exceed 1 MiB.')
    else:
        form = UploadFileForm()
    context = {
        'form': form,
    }

    return render(request, "requestdataapp/file-upload.html", context=context)


# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760



