from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# import necessary lib for data analysis
import matplotlib
matplotlib.use('Agg')
import csv
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# figure processing
from io import StringIO, BytesIO
import base64
import logging
import os
from django.conf import settings

# Create your views here.
@login_required
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # get file object from request
            uploaded_file = request.FILES["file"]
            # Read the file as text
            file_data = uploaded_file.read().decode('utf-8')
            # Create a reader object using StringIO
            reader = csv.reader(StringIO(file_data))
            # 'next()' gets a reader object and returns the next line of the file
            header_row = next(reader)
            # ========================================================
            dates, highs, lows = [], [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                try: 
                    high = int(row[5])
                    low = int(row[6])
                except ValueError:
                    print(f"Missing data for {current_date}")
                    return redirect('visual_logs:topics')
                else:     
                    dates.append(current_date)
                    highs.append(high)
                    lows.append(low)

            plt.style.use('seaborn-v0_8')
            fig, ax = plt.subplots()
            # param alpha set the transprancy of the line, decreasing from 0 to 1
            ax.plot(dates, highs, c = 'red', alpha = 0.5)
            ax.plot(dates, lows, c = 'blue', alpha = 0.5)
            # fill the area between the high and low
            ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
            # set the config of the figure
            ax.set_title("Title", fontsize = 24)
            ax.set_xlabel('', fontsize = 14)
            # use 'autofmt_xdate()' to draw inclined date to avoid overlapping
            fig.autofmt_xdate() 
            ax.set_ylabel("Temperature(F)", fontsize = 14)
            ax.tick_params(axis = 'both', which = 'major', labelsize = 14)
            
            # ========================================================

            # initializes a bytes buffer to temporarily hold the generated image data
            buf = BytesIO()
            # saves the generated Matplotlib figure to the buffer in PNG format.
            fig.savefig(buf, format='png')
            # resets the buffer’s current position to the beginning
            buf.seek(0)
            # reads the image data from the buffer, encodes it in base64, and then 
            # decodes the base64 bytes to an ASCII string
            image_base64 = base64.b64encode(buf.read()).decode('ascii')
            # display the image using this base64 string
            return render(request, 'visual/plot.html', {'image_base64': image_base64})
    else:
        form = UploadFileForm()
    context = {'form': form}
    return render(request, 'visual/upload_file.html',context)
