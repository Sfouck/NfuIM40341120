# -*- coding:utf8 -*-
# Attribute Information:
#
# No: row number
# year: year of data in this row
# month: month of data in this row
# day: day of data in this row
# hour: hour of data in this row
# pm2.5: PM2.5 concentration (ug/m^3)
# DEWP: Dew Point (â„ƒ)
# TEMP: Temperature (â„ƒ)
# PRES: Pressure (hPa)
# cbwd: Combined wind direction
# Iws: Cumulated wind speed (m/s)
# Is: Cumulated hours of snow
# Ir: Cumulated hours of rain

import pandas as pd
import numpy as np
from sklearn import linear_model
import warnings


def warn(*args, **kwargs):
    pass


warnings.warn = warn
if __name__ == '__main__':
    train_percent = 95

    load_data = pd.read_csv("Beijing_pm2.5.csv")
    load_data = load_data[(load_data["pm2.5"] >= 0)]
    cbwd = {"cv": 0.21,
            "NE": 0.11,
            "NW": 0.33,
            "SE": 0.35}
    # cbwd = {"cv": 1,
    #         "NE": 2,
    #         "NW": 4,
    #         "SE": 5}
    load_data["cbwd"] = [cbwd[wind] for wind in load_data["cbwd"]]

    # print load_data

    count = len(load_data)
    train_count = train_percent * count / 100

    train_data = load_data[:train_count]
    test_data = load_data[train_count:].reset_index(drop=True)

    # print train_data
    # print test_data

    select_row = "year,month,day,hour,DEWP,TEMP,PRES,cbwd,Iws,Is,Ir".split(",")
    print select_row
    # print train_data[select_row]

    regr = linear_model.LinearRegression(n_jobs=-1)
    regr.fit(train_data[select_row], train_data["pm2.5"])

    print(regr.coef_)
    # The coefficients
    # print('Coefficients: \n{}'.format(np.array(zip(select_row, regr.coef_))))
    # The mean squared error
    print("Mean squared error: {:.2f}".format(
        np.mean((regr.predict(test_data[select_row]) - test_data["pm2.5"]) ** 2)))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: {:.2f}'.format(regr.score(test_data[select_row], test_data["pm2.5"])))
