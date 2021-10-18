import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def marksprediction(marks):
    
    data = pd.read_csv("student_scores.csv")

    X = data.iloc[:, :-1].values
    y = data.iloc[:, 1].values

    model = LinearRegression()
    model.fit(X,y)

    #print(model.intercept_)
    #print(model.coef_)

    Xtest = np.array(marks)
    Xtest = Xtest.reshape((1,-1))

    result = model.predict(Xtest)
    return result


