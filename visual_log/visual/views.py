from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadForm
import csv
import matplotlib.pyplot as plt
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.owner = request.user
            uploaded_file.save()
            file_path = uploaded_file.file.path

            # gain data from upload file
            data = pd.read_csv(file_path)

            # perform data analysis
            plt.figure(figsize=(10, 6))
            data.plot(kind='bar')
            plt.title('Data Analysis')
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.grid(True)

            # save figure
            plot_path = f'media/uploads/plot_{uploaded_file.id}.png'
            plt.savefig(plot_path)
            plt.close()

            return redirect('visual_logs:view_plot', plot_id=uploaded_file.id)
    else:
        form = UploadForm()

    context = {'form': form}    
    return render(request, context)

@login_required
def view_plot(request, plot_id):
    uploaded_file = get_object_or_404(UploadedFile, id=plot_id, owner=request.user)
    plot_path = f'uploads/plot_{uploaded_file.id}.png'
    return render(request, 'visual_logs/view_plot.html', {'plot_path': plot_path})

    