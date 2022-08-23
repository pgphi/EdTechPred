import pandas as pd
from preprocessing import y
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def make_prediction(date, number, error):
    """

    :param date: date ('%Y/%m/%d') (str)
    :param number: kWh consumption (int or float)
    :param error: mean absolute error of price in euro/kWh
    :return: gas_costs in Euro based on kWh consumption i.E. 10000 Euros for 10000kWh
    """

    try:
        x1 = int(date.strftime("%s"))
        x2 = int(number) / 1000000000  # convert kWh to TWh
        y_pred = 5.014586015417417 + -6.691310239483297e-09 * x1 + 1.2486026421482226e-09 * x2 \
                 + 2.2363262130192694e-18 * x1 ** 2 + -7.831611461243813e-19 * x2 ** 2 \
                 + -3.191085831814934e-19 * x1 * x2
        x2 = x2 * 1000000000  # convert kWh to TWh for making suitable predictions for kWh
        gas_costs = round(y_pred * x2, 2)  # gas_costs in Euro = EUR/kWh * kWh
        cost_variance = round(x2 * error, 2)  # gas consumption in kWh * mae of model

    # Input is case sensitive
    except ValueError:
        print("Did you write the date right? For Example 01.01.2020 no '-' or shortcuts for the Year" + "\n" +
              "Please input whole numbers for your gas consumption i.e. 15000, 23543 etc. without points or comas"
              + "\n" + "Please right 'yes' or 'no'")

    return [gas_costs, cost_variance]


def mc_simulation(y, t_intervals, outcomes):
    """
    :param y: data for predictor i.e. price
    :param t_intervals: prediction time length into the future
    :param outcomes: no. of different randomized outcome possibilities
    :return: plot of monte carlo simulation
    """

    df = pd.DataFrame()
    df["Price"] = y.loc[::-1].reset_index(drop=True)  # reverse index for last to current (and not the other way around)
    df = df["Price"]
    # print(df)

    log_return = np.log(1 + df.pct_change())  # make price series continuous and numerical stable
    # print(log_return)

    mean = log_return.mean()
    # print(mean)
    var = log_return.var()
    # print(var)

    # plt.plot(df)  # plot price data points
    # plt.show()

    # plt.plot(log_return)  # plot log return data points
    # plt.show()

    drift = mean - 0.5 * var
    # print(drift)

    vol = log_return.std()  # volatility/variance of log return
    intervals = t_intervals  # generate data X time into future
    iterations = outcomes  # amount of randomized outcome possibilities

    r = np.exp(drift + vol * norm.ppf(np.random.rand(intervals, iterations)))
    # norm.ppf = # calculate distance from mean points
    # print(r)

    S0 = df[0]
    # print(S0)

    price_list = np.zeros_like(r)
    # print(price_list)

    price_list[0] = S0
    # print(price_list)

    for i in range(1, t_intervals):
        price_list[i] = price_list[i - 1] * r[i]

    # print(price_list)

    plt.figure(figsize=(15, 8), num="Monte Carlo Simulation for German Gas Prices")
    plt.plot(price_list)
    plt.xlabel("Time")
    plt.ylabel("Gas Price in Euro/kWh")
    plt.show()
    mc_plot = plt.savefig("Images/mc_prediction.png")

    return mc_plot


# mc_simulation(y, 200, 5)
