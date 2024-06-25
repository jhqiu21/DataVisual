## create a result class to encapsulate the component of result
import csv
from io import StringIO, BytesIO
from . import cdf, histo


class Info:

    def __init__(self, request):
        self.request = request
        self.plot_title = request.POST.get('title')
        self.type = int(request.POST.get('type'))
        self.file = request.FILES["file"]
        
    
    def getFileReader(self):
        # Read the file as text
        file_data = self.file.read().decode('utf-8')
        # Create a reader object using StringIO
        reader = csv.reader(StringIO(file_data), delimiter="\t")
        return reader
    
    def getResult(self):
        if self.type == 1:
            return histo.histogram(self)
        elif self.type == 2:
            return cdf.cumulative_distributions(self)
        elif self.type == 3:
            return 

    



