import matplotlib.pyplot as plt
import pandas as pd


def extract_data(csv_dataset):
    """
    :param csv_dataset: csv_dataset (relative path)
    :return: list of arrays [dataset-, training- and test-array].
    """

    df = pd.read_csv(csv_dataset, sep=";")  # "DataSets/NASDQ_Price_Data.csv"

    training_data = df.sample(frac=0.8, random_state=25)
    testing_data = df.drop(training_data.index)

    # print(f"No. of training examples: {training_data.shape[0]}")
    # print(f"No. of testing examples: {testing_data.shape[0]}")

    return [df, training_data, testing_data]


def create_scatter_plot(title, x1label, x2label, ylabel,
                        x1, x2, y):
    """
    :param title: Title of scatter plot
    :param x1label: Name of first regressor
    :param x2label: Name of second regressor
    :param x3label: Name of third regressor
    :param ylabel: Name of predictor
    :param x1: Values for first regressor
    :param x2: Values for second regressor
    :param x3: Values for third regressor
    :param y: Values for predictor
    :return: scatter plot
    """

    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111, projection="3d")

    ax.set_title(title)
    ax.set_xlabel(x1label, labelpad=15)
    ax.set_ylabel(ylabel, labelpad=15)

    img = ax.scatter(x1, y, c=x2, cmap=plt.hot())  # takes x, y and z
    clb = fig.colorbar(img)
    clb.set_label(x2label, labelpad=15)
    plt.show()
    scatter_plot = fig.savefig(title + ".png", dpi=1000)

    return scatter_plot


def check_for_equal_len(X, y):
    """
    :param X: N-D matrix or array (regressors)
    :param y: 1-D matrix or array (predictor)
    :return: True (False) if length of X and y are (not) equal
    """

    if len(X) == len(y):
        return True

    else:
        print(f"X length := {len(X)}")
        print(f"y length := {len(y)}")
        return False


def date_to_timestamps(dates):
    """
    :param dates: column of dates i.e. 23-95-2025 with string type
    :return: list of timestamps with float type (for modeling)
    """
    timestamps = []
    for i in dates:
        timestamps.append(i.timestamp())

    return timestamps


# Extract dataset, X and y
DF = extract_data("Dataset/Gas_Dataset.csv")[0]
# print("Dataset:")
# print(DF)
# print()

x1 = pd.to_datetime(DF["Date"], format="%d.%m.%y")
x1 = date_to_timestamps(x1)
x1 = pd.DataFrame(x1)
# print("Time data:")
# print(x1)
# print()

x2 = DF["Storage (TWh)"].apply(lambda x: float(x.split()[0].replace(',', '')))
x2 = pd.DataFrame(x2)
# print("Gas Storage Data:")
# print(x2)
# print()

X = x1.assign(Gas_Storage=x2)
# print("Regressor Data (X):")
# print(X)
# print()

y = DF["Price (EUR/kWh)"].apply(lambda x: float(x.split()[0].replace(',', '')) / 10000)
# print("Price Data (y):")
# print(y)
# print()

# Check for X and y length
if not check_for_equal_len(X, y):
    print("Please check your X and y data. Rows have to be equal in length.")

# Plot Data
# scat_plot = create_scatter_plot("Gas Price Prediction",
# "Time(-stamps) (from 01-10-15 to 01-09-22)",
# "Gas Storage in TWh (from dark (low) to bright (high))",
# "Gas Price in Euro/kWh",
# x1, x2, y)
