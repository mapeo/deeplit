from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from . import separator
from django.http import Http404
import os.path
from django.conf import settings

def upload(request):
    context = {}
    if not request.method == 'POST':
        return render(request, 'upload.html')
    if 'uploaded-file' not in request.FILES:
        return render(request, 'upload.html')
    uploaded_file = request.FILES['uploaded-file']
    data = request.POST.dict()
    algorithm = data['algorithm']
    fs = FileSystemStorage()
    filename = fs.save(uploaded_file.name, uploaded_file)
    zipfile = separator.separate(filename, data['algorithm'])
    return redirect(f'/downloads/{zipfile}')

def downloads(request, file):
    context = {}
    fs = FileSystemStorage()
    zipped = f'{file}.zip'
    if not os.path.exists(f'{settings.MEDIA_DOWNLOAD}{zipped}'):
        raise Http404("File not found")
    context['file'] = f'{fs.url(zipped)}'
    return render(request, 'downloads.html', context)

