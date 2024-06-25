from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# import necessary lib for data analysis
import csv
from .scripts import histo, cdf
from .scripts.data import Info


# figure processing
from io import StringIO, BytesIO
import base64

# Create your views here.
@login_required
def upload_file(request):
    if request.method == "POST":
        # get file and plot_title from form
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            info = Info(request)
            result = info.getResult()
            fig = result.get('figure')
            message = result.get('message')
            image_base64 = imgProcess(fig)
            context = {
                'image_base64': image_base64, 
                'message': message, 
                'plot_title': info.plot_title
            }
            return render(request, 'visual/plot.html', context)
    else:
        form = UploadFileForm()
    context = {'form': form}
    return render(request, 'visual/upload_file.html',context)


def imgProcess(fig):
    # initializes a bytes buffer to temporarily hold the generated image data
    buf = BytesIO()
    # saves the generated Matplotlib figure to the buffer in PNG format.
    fig.savefig(buf, format='png')
    # resets the buffer’s current position to the beginning
    buf.seek(0)
    # reads the image data from the buffer, encodes it in base64, and then 
    # decodes the base64 bytes to an ASCII string
    return base64.b64encode(buf.read()).decode('ascii')

