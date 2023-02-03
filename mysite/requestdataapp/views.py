from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


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
    return render(request, 'requestdataapp/user-bio-form.html')


MAX_UPLOAD_SIZE = "1000000"
def handle_file_upload(request: HttpRequest) -> HttpRequest:
    if request.method == "POST" and request.FILES.get("myfile"):
        myfile = request.FILES["myfile"]
        if myfile.size < int(MAX_UPLOAD_SIZE):
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            print("saved file", filename)
        else:
            raise ValidationError('File too large. Size should not exceed 1 MiB.')

    return render(request, "requestdataapp/file-upload.html")


# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760



