from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadFileForm
import csv
import io
import matplotlib.pyplot as plt
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES["file"]
            file_data = uploaded_file.read().decode('utf-8')
            data = pd.read_csv(io.StringIO(file_data))
            # add data analysis function here
            # test case
            # auto fill to test - need to update
            return redirect('visual_logs:topics')
    else:
        form = UploadFileForm()
    context = {'form': form}
    return render(request, 'visual/upload_file.html',context)


    