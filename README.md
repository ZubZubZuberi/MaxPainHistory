# MaxPainHistory

## Description

The Max Pain Tracker is a Python-based code that helps you track the "max pain" of a stock over time and analyze whether there are any noticeable patterns. Max pain refers to the point where the option buyers (calls and puts) will experience the most financial loss. This code calculates the max pain using the Open Interest (OI) data of call and put options, and then visualizes it on a graph for easier analysis (TBD). 

## Features

- Fetches up-to-date Open Interest (OI) data from reliable financial data sources.
- Calculates the max pain level for specific stocks using the collected OI data.
- Plots the historical max pain levels on an interactive graph for easy visualization.

## How It Works

1. The code retrieves Open Interest (OI) data for call and put options from the chosen data source.
2. It analyzes the data to calculate the max pain level, considering both the number of contracts (volume) and their strike prices.
3. The code then generates a graph showing both the stock price and the max pain levels over time.
4. You can observe the graph and look for any interesting patterns or trends in the maximum pain levels.
5. Based on the analysis, you may gain insights into how option buyers are impacted and evaluate potential trading strategies.

## Requirements

- Python 3.x
- Any necessary dependencies specified in the `requirements.txt` file.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` in your preferred command-line tool.
3. Modify the code as needed (e.g., data source, stock ticker, time interval, graphs, SQL edits, etc).

## Example Data + Graph (Fake Info Used)
## ![image](https://github.com/ZubZubZuberi/MaxPainHistory/assets/156230012/c6240bc0-e90b-49bf-93e3-d64e653c0faf)
| Ticker | Price | MaxPain |      Date      |
| ------ |-------| --------| -------------- |
|  GME   | $14.93| $15.10  | 1/10/2023 8:00 AM |
|  GME   | $14.98| $14.90  | 1/10/2023 8:15 AM |
|  GME   | $15.05| $14.97  | 1/10/2023 8:30 AM |
|  GME   | $15.10| $14.94  | 1/10/2023 8:45 AM |
|  GME   | $15.02| $14.98  | 1/10/2023 9:00 AM |
|  GME   | $15.07| $14.92  | 1/10/2023 9:15 AM |
|  GME   | $14.92| $15.05  | 1/10/2023 9:30 AM |
|  GME   | $15.15| $15.08  | 1/10/2023 9:45 AM |
|  GME   | $14.97| $15.10  | 1/10/2023 10:00 AM |
|  GME   | $15.10| $15.03  | 1/10/2023 10:15 AM |
|  GME   | $14.93| $14.99  | 1/10/2023 10:30 AM |
|  GME   | $15.05| $14.95  | 1/10/2023 10:45 AM |
|  GME   | $14.99| $15.08  | 1/10/2023 11:00 AM |
|  GME   | $15.02| $14.93  | 1/10/2023 11:15 AM |
|  GME   | $15.07| $14.98  | 1/10/2023 11:30 AM |
|  GME   | $15.10| $15.04  | 1/10/2023 11:45 AM |
|  GME   | $14.92| $15.07  | 1/10/2023 12:00 PM |
|  GME   | $15.15| $14.94  | 1/10/2023 12:15 PM |
|  GME   | $14.97| $15.03  | 1/10/2023 12:30 PM |
|  GME   | $15.08| $15.05  | 1/10/2023 12:45 PM |
|  GME   | $15.10| $14.99  | 1/10/2023 1:00 PM  |
|  GME   | $14.93| $14.96  | 1/10/2023 1:15 PM  |
|  GME   | $15.05| $15.10  | 1/10/2023 1:30 PM  |
|  GME   | $14.99| $15.02  | 1/10/2023 1:45 PM  |
|  GME   | $15.02| $14.93  | 1/10/2023 2:00 PM  |
|  GME   | $15.07| $14.95  | 1/10/2023 2:15 PM  |
|  GME   | $15.10| $15.08  | 1/10/2023 2:30 PM  |
|  GME   | $14.92| $14.97  | 1/10/2023 2:45 PM  |
|  GME   | $15.15| $14.92  | 1/10/2023 3:00 PM  |

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
