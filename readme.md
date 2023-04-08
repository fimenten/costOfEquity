# Cost of Equity Calculator

This is a simple command-line tool that calculates the cost of equity for a given stock, based on its beta, risk-free rate, and premium.

## Requirements

This tool requires the following Python packages to be installed:

- pandas
- pandas-datareader
- yfinance

You can install them using the following command:

`pip install pandas pandas-datareader yfinance`


## Usage

To use this tool, run the `costOfEquity.py` script with the following command:


Where:
- `<ticker>` is the ticker symbol for the stock you want to calculate the cost of equity for. For example, `4563.T` for アンジェス.
- `<premium>` is the premium for the stock, in percent.
- `--yfinance` is an optional flag that tells the script to use the `yfinance` library to retrieve the data. It is set to `True` by default.
- `--beta <beta_value>` is an optional argument that specifies the beta value for the stock, if you don't want to use the default value retrieved from `yfinance`.
- `--riskFreeRate <risk_free_rate_value>` is an optional argument that specifies the risk-free rate for the stock, if you don't want to use the default value retrieved from the Japanese Ministry of Finance website.
- `--freq <resampling_frequency>` is an optional argument that specifies the frequency to resample the data to. It is set to "W" (weekly) by default.

## Example

`python costOfEquity.py 4563.T 0.1`


This command calculates the cost of equity for 4563.T. and RiskPremium 0.1

## License

This tool is licensed under the MIT License. Feel free to use and modify it as you wish.
