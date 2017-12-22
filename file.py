from pyramid.response import Response
from pyramid.view import view_defaults, view_config
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" Todo: class Visualizes multiple plots with the input of data by loading the file"""


class Visz(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name="line_chart", request_method='POST')
    def line_chart(self):
        """Todo: This method loads the given file and visualizes the given two attributes as a Line graph
         params: We get file_name,X,Y values in json_body of the request
         return  for now its just returning the type of the chart """

        # Extracting the json_body of te request to get our required parameters
        data = self.request.json_body
        file_name = data["file_name"]
        attr1 = data["X"]
        attr2 = data["Y"]
        # Loading CSV file using pandas
        df = pd.read_csv(file_name)
        # here X and Y pandas Series which contains the data for that particular columns
        X = df[attr1]
        Y = df[attr2]
        # Here we are plotting the X and Y using matplotlib plot command, label and title the graph
        plt.plot(X, Y, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue',
                 markersize=12)
        plt.xlabel(attr1)
        plt.ylabel(attr2)
        plt.title(file_name)
        plt.legend()
        plt.show()
        return Response("Line chart")

    @view_config(route_name="scatter_plot", request_method='POST')
    def scatter_plot(self):
        """Todo: This method loads the given file and visualizes the given two attributes as a Scatter plot
                 params: We get file_name,X,Y values in json_body of the request
                 return  for now its just returning the type of the chart that is scatter plot"""
        # Extracting the json_body of te request to get our required parameters
        data = self.request.json_body
        file_name = data["file_name"]
        attr1 = data["X"]
        attr2 = data["Y"]
        # Loading CSV file using pandas
        df = pd.read_csv(file_name)
        # here X and Y pandas Series which contains the data for that particular columns
        X = df[attr1]
        Y = df[attr2]
        # Here we are plotting the X and Y using matplotlib scatter command, label and title the graph
        plt.scatter(X, Y, label='Age-Salary', color='g', s=25, marker="*")
        plt.xlabel(attr1)
        plt.ylabel(attr2)
        plt.title(file_name)
        plt.legend()
        plt.show()
        return Response("scatter plot")

    @view_config(route_name="pie_chart", request_method='POST')
    def pie_chart(self):
        """Todo: This method loads the given file and visualizes the given two attributes as a Scatter plot
                         params: We get file_name,X values in json_body of the request
                         return  for now its just returning the type of the chart that is pie chart"""
        # Extracting the json_body of te request to get our required parameters
        data = self.request.json_body
        file_name = data["file_name"]
        attr1 = data["X"]
        df = pd.read_csv(file_name)
        X = pd.DataFrame()
        X = X.assign(new_col=df[attr1])
        arr = pd.unique(df[attr1]).tolist()
        pie_list = []
        expl = []
        colors = []
        for i in range(0, len(arr)):
            pie_list.append(X[X.new_col == arr[i]].size)
            expl.append(i / 100)
        plt.pie(pie_list, labels=arr, explode=expl, rotatelabels=True)
        plt.title(file_name + " " + attr1)
        plt.show()
        return Response("pie_chart")

    @view_config(route_name="bar_chart", request_method='POST')
    def bar_chart(self):
        data = self.request.json_body
        file_name = data["file_name"]
        attr1 = data["X"]
        attr2 = data["Y"]
        df = pd.read_csv(file_name)
        X = pd.unique(df[attr1]).tolist()
        Z = pd.DataFrame()
        Z = Z.assign(new_col1=df[attr1], new_col2=df[attr2])
        arr = pd.unique(df[attr2]).tolist()
        col = ['blue', 'yellow']
        colors = "bgrcmykw"
        color_index = 0
        index = np.arange(len(X))
        opacity = 0.8
        width = 0
        for i in range(0, len(arr)):
            Y = []
            for j in range(0, len(X)):
                Y.append(Z[(Z.new_col2 == arr[i]) & (Z.new_col1 == X[j])].size)
            plt.bar(index + width, Y, width=0.1, color=colors[color_index], label=arr[i], alpha=opacity)
            color_index = 1 + color_index
            width = width + 0.35
        plt.xlabel(attr1)
        plt.ylabel(attr2)
        plt.xticks(index, X)
        plt.title(file_name)
        plt.legend()
        plt.show()
        return Response("Multiple bar chart")

    @view_config(route_name="histogram", request_method='POST')
    def histogram(self):
        data = self.request.json_body
        file_name = data["file_name"]
        attr1 = data["X"]
        df = pd.read_csv(file_name)
        X = pd.DataFrame()
        X = X.assign(new_col=df[attr1])
        arr = pd.unique(df[attr1]).tolist()
        hist_list = []
        index = np.arange(len(arr))
        for i in range(0, len(arr)):
            hist_list.append(X[X.new_col == arr[i]].size)
        plt.hist(X, histtype='bar', rwidth=0.8)
        plt.xticks(index, arr)
        plt.title(file_name + " " + attr1)
        plt.show()
        return Response("histogram")

