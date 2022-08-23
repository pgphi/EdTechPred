from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_absolute_error
import json


def reg_modeling(X, y):
    """
    :param X: 2D matrix with independend variables (Time and Storage)
    :param y: Price Prediction
    :return: intercepts, slopes or coefficients and performance of polynomial and linear function
    """

    # Create polynomial model: f(x1, x2) = y = ß0 + ß1x1 + ß2x2 + ß3x1^2 + ß4x2^2 + ß5x1x2
    poly = PolynomialFeatures(degree=2, include_bias=False)  # False, otherwise we assume a to be zero.
    poly_feautures = poly.fit_transform(X)  # X must be 2D
    poly_model = LinearRegression().fit(poly_feautures, y)
    poly_predicted = poly_model.predict(poly_feautures)

    """
    # Plot Polynomial Graph
    plt.figure(figsize=(10, 6))
    plt.title("Polynomial Graph", size=16)
    plt.scatter(time, y)
    plt.plot(time, poly_predicted, c="red")
    plt.show()
    """

    # Create linear model:  f(x1, x2) = y = ß0 + ß1x1 + ß2x2
    lin_model = LinearRegression().fit(X, y)
    lin_predicted = lin_model.predict(X)

    """
    # Plot Linear Graph
    plt.figure(figsize=(10, 6))
    plt.title("Linear Graph", size=16)
    plt.scatter(time, y)
    plt.plot(time, lin_predicted, c="red")
    plt.show()
    """

    # Get intercepts and slopes (coefficients of models)
    pols = poly_model.coef_
    poly_intercept = poly_model.intercept_
    lins = lin_model.coef_
    lin_intercept = lin_model.intercept_

    # Print functions
    """
    print(f"Polynomial function: \n f(x1, x2) = {poly_intercept} + {pols[0]} * x1 + {pols[1]} * x2 + "
          f"{pols[2]} * x1^2 + {pols[3]} * x2^2 + {pols[4]} *x1 * x2")
    print()
    print(f"Linear function: \n f(x1, x2) ={lin_intercept}  + {lins[0]} * x1 + {lins[1]} * x2")
    print()
    """

    # Evaluate Models
    poly_r2 = r2_score(y, poly_predicted)
    lin_r2 = r2_score(y, lin_predicted)
    poly_mae = mean_absolute_error(y, poly_predicted)
    lin_mae = mean_absolute_error(y, lin_predicted)

    # print(f"Polynomial Function MAE = {poly_mae}")
    # print(f"Linear Function MAE = {lin_mae}")
    # print(f"Polynomial Function R Squared = {poly_r2}")
    # print(f"Linear Function R Squared = {lin_r2}")

    return [pols, poly_intercept, lins, lin_intercept, poly_r2, poly_mae, lin_r2, lin_mae]


def model_to_json(coefficients, intercept):
    """
    :param coefficients: hyperparameters or slopes of model
    :param intercept: starting point when function is zero of model
    :return: model in JSON-format for contribution and production purposes
    """

    model_param = {'coefficients': list(coefficients), 'intercept': intercept.tolist()}

    # Convert Python Dictionary to JSON string
    json_txt = json.dumps(model_param, indent=4)  # indent specifies spaces at beginning of a line

    # Save Json String to a file
    with open('model.txt', 'w') as file:
        file.write(json_txt)

    # Load content of the file to a json string. Open file in read mode. Then load the json data in python object (DIC)
    with open('model.txt', 'r') as file:
        json_text = json.load(file)

    return json_text
