import matplotlib.pyplot as plt
import csv
import numpy
from pyramid.response import Response
from pyramid.view import view_config
x = []
y = []


@view_config(route_name="load_file_matplotlib", request_method='POST')
def load_file_matplotlib(request):
    data=request.json_body
    file_name=data["file_name"]
    attr1=data["X"]
    attr2=data["Y"]
    with open(file_name, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        rownum=0
        xnum=0
        ynum=0
        for row in plots:
            if(rownum==0):
                header = row
                colnum=0
                for col in row:
                    if col==attr1:
                        xnum=colnum
                    elif col==attr2:
                        ynum=colnum
                    colnum=colnum+1
            rownum = rownum+1
            if(rownum>1):
                x.append(row[xnum])
                y.append(row[ynum])
    plt.scatter(x, y, label='Age-Salary', color='g', s=25, marker="*")
    plt.xlabel(attr1)
    plt.ylabel(attr2)
    plt.xticks(numpy.arange(3))
    plt.yticks(numpy.arange(3))
    plt.title('Interesting Graph Check it out')
    plt.legend()
    plt.show()
    return Response("Matplot lib loading file and visualizing it")

