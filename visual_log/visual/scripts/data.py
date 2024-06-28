## create a result class to encapsulate the component of result
import csv
from io import StringIO, BytesIO
from . import cdf, histo, line, confidece_ellipse
import pandas as pd

class Info:
    def __init__(self, request):

        self.request = request
        self.plot_title = request.POST.get('title')
        self.plot_title_font = int(request.POST.get('tfont'))
        self.x_title = request.POST.get('xtitle')
        self.x_font = int(request.POST.get('xfont'))
        self.y_title = request.POST.get('ytitle')
        self.y_font = int(request.POST.get('yfont'))
        self.style = request.POST.get('style')
        self.type = int(request.POST.get('type'))
        self.legend = int(request.POST.get('legend'))
        self.bin = int(request.POST.get('bin', 10))

        # generate file reader and header_row
        self.file = request.FILES["file"]
        reader = readFile(self.file)
        # 'next()' gets a reader object and returns the next line of the file
        self.header_row = next(reader)
        self.file_reader = reader
        
        # generate header dictionary
        self.header_dic = headerToDic(self.header_row)

        # decomposite input parameter
        self.parameter = request.POST.get('parameter').split('#')
        if len(self.parameter) == 1:
            self.para = self.parameter[0].split('/')
            self.para_pos = generatePosList(self.para, self.header_dic)
            self.para_data = getXDataList(self.para_pos, self.file_reader)
            
        elif len(self.parameter) == 2:
            self.paraX = self.parameter[0].split('/')
            self.paraX_pos = generatePosList(self.paraX, self.header_dic)
            self.paraY = self.parameter[1].split('/')
            self.paraY_pos = generatePosList(self.paraY, self.header_dic)
            # self.para_data is a dictionary of both independent and dependent variable data 
            # and missing message.
            self.para_data = getXYDataList(self.paraX_pos, self.paraY_pos, self.file_reader)
            

    def getResult(self):
        if self.type == 1:
            return histo.histogram(self)
        elif self.type == 2:
            return histo.bihistogram(self)
        elif self.type == 3:    
            return cdf.cumulative_distributions(self)
        elif self.type == 4:
            return line.line_chart(self)
        elif self.type == 5:
            return confidece_ellipse.confidence_ellipse_gram(self)



# helper function

def readFile(file):
    # Create a reader object using StringIO
    file_data = file.read().decode('utf-8')
    if file.name.endswith('.tsv'):
        return csv.reader(StringIO(file_data), delimiter="\t")
    elif file.name.endswith('.csv'):
        return csv.reader(StringIO(file_data))
    elif file.name.endswith('.json'):
        df = pd.read_json(StringIO(file_data))
        csv_output = StringIO()
        df.to_csv(csv_output, sep='\t', index=False)
        csv_output.seek(0)
        return csv.reader(csv_output, delimiter="\t")
    else:
        raise FileExpection("Invalid File Format!")

def headerToDic(header_row):
        index = 0
        header = {}
        for para in header_row:
            header[para] = index
            index += 1
        return header

def generatePosList(list, dict):
    pos_list = []
    for para in list:
        pos = dict.get(para)
        pos_list.append(pos)
    return pos_list

def getXDataList(pos_list, reader):
    # Initialize the list of data and the missing message list
    datas = [[] for _ in pos_list]
    missing_msg = []

    for row in reader:
        id = str(row[0])
        try:
            isValidRow(row, pos_list)
        except ValueError:
            missing_msg.append(f"Missing or invalid data in line {reader.line_num} for {id}")
            continue
        for index, pos in enumerate(pos_list):
            datas[index].append(row[pos])
    result = {'datas': datas, 'message': missing_msg}
    return result

def getXYDataList(paraX_pos_list, paraY_pos_list, reader):
    # Initialize the list of data and the missing message list
    paraX_datas = [[] for _ in paraX_pos_list]
    paraY_datas = [[] for _ in paraY_pos_list]
    missing_msg = []

    for row in reader:
        id = str(row[0])
        try:
            isValidRow(row, paraX_pos_list)
            isValidRow(row, paraY_pos_list)
        except ValueError:
            missing_msg.append(f"Missing or invalid data in line {reader.line_num} for {id}")
            continue
        for index, pos in enumerate(paraX_pos_list):
            paraX_datas[index].append(row[pos])
        for index, pos in enumerate(paraY_pos_list):
            paraY_datas[index].append(row[pos])
    result = {'paraX_datas': paraX_datas, 'paraY_datas': paraY_datas, 'message': missing_msg}
    return result

def isValidRow(row, pos_list):
    data = 0
    for pos in pos_list:
        data = int(row[pos])
        
    
# exception class inheritent from basic exception

class FileExpection(Exception):
    def __init__(self, message):
        self.msg = message
    def __str__(self):
        return repr(self.msg)    