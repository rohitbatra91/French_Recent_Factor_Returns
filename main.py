# Analyzing the North American French Fama portfolios with Pandas
# By Rohit Batra

import pandas as pd
import numpy as np

# Files to be used
files = ["North_America_25_Portfolios_ME_Prior_12_2.csv",
         "North_America_32_Portfolios_ME_BE-ME_OP_2x4x4.csv"]


def portfolio_growth(monthly_portfolio_returns):
    number_of_months = len(monthly_portfolio_returns)
    # Initializing array, starting with 1
    portfolio_growth_arr = np.zeros(number_of_months)
    portfolio_growth_arr[0] = 1
    # Computing growth of portfolio value
    # current month value = last month value * (1 + monthly return / 100)
    for i in range(number_of_months - 1):
        portfolio_growth_arr[i+1] = portfolio_growth_arr[i] * (1 + monthly_portfolio_returns[i] / 100)
    return portfolio_growth_arr

# Function to calculate the geometric growth with from an array of returns
def geometric_mean_calc(returns_arr):
    n = len(returns_arr)
    product = 1
    for i in range(n - 1):
        product = product * (1 + returns_arr[i] / 100)
    geometric_mean = product ** (1/n * 12) - 1
    # Convert back to percent and return
    return geometric_mean * 100

# Finding the CAGR between points
def cagr_calc(beginning, end, time):
    return ((end / beginning) ** (1 / time) - 1) * 100


if __name__ == '__main__':
    # Looping over all the files we want to test out
    for file in files:
        # Creating the data frame from the file
        df = pd.read_csv(file, skiprows=1) # Skip the first row, just the weight of the portfolio
        dates = df.DATE.to_numpy()

        # Loop over all the portfolios constructed
        for i in df.columns[1:]:
            portfolio = df[i].to_numpy()
            # printing the geometric mean of the portfolio
            geometric_mean_portfolio = geometric_mean_calc((portfolio))
            if geometric_mean_portfolio > 18:
                print(i)
                print(geometric_mean_portfolio)