__author__ = 'mike-bowles'

import numpy
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.externals.six import StringIO
from math import sqrt
import csv
from sklearn import preprocessing


# read data into iterable

class datapredict:
    def predict(self, pm25data):

        xList = []
        labels = []
        names = []
        firstLine = True
        with open('pm25data.csv', 'rb') as csvfile:
            data = csv.reader(csvfile)
            for line in data:
                if firstLine:
                    names = line
                    firstLine = False
                else:
                    # split on semi-colon
                    row = line
                    # put labels in separate array
                    labels.append(float(row[-1]))
                    # remove label from row
                    row.pop()
                    # convert row to floats
                    floatRow = [float(num) for num in row]
                    xList.append(floatRow)

        #xList = preprocessing.scale(xList)
        nrows = len(xList)
        ncols = len(xList[0])

        wineTree = DecisionTreeRegressor(max_depth=4)

        wineTree.fit(xList, labels)

        return wineTree.predict([pm25data])

        # with open("pm25Tree2.dot", 'w') as f:
        #    f = tree.export_graphviz(wineTree, out_file=f)
        # Note: The code above exports the trained tree info to a
        # Graphviz "dot" file.
        # Drawing the graph requires installing GraphViz and the running the
        # following on the command line
        # dot -Tpng wineTree.dot -o wineTree.png
        # In Windows, you can also open the .dot file in the GraphViz
        # gui (GVedit.exe)]
