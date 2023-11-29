import pandas as pd
import pyodbc


def get_data():
    global map_dict, iris, iris_features, iris_label
    conn = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};Server=tcp:aidi1006.database.windows.net,1433;Database=aidi-1006-ass4;Uid=admi;Pwd=Ruba@1997;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    map_dict = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}

    iris = pd.read_sql('SELECT * FROM dbo.iris', conn)
    iris.Species = iris.Species.map(map_dict)

    iris_features = iris.values[:, 1:5].astype('f')
    iris_label = iris.values[:, 5]

    return iris_features, iris_label
