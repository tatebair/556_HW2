Welcome to the S&P500 vs Vix Comparison project.

This is a homework for STA556 in which the objective is as follows:
"Build a small, readable data-analysis pipeline that obtains data, cleans it with reusable functions, and
communicates one clear finding visually."

The purpose of this project is to analyze the relationship between the VIX and S&P500 data sets. We will look at differences S&P500 daily returns among different segments of volitility.

This data is retreived from the yFinance API for the 2020 - 2026 period. For future users, this should allow different time periods to be selected, and less data needing to be stored on their device with larger csv files.

Please use the Analysis.ipynb file to run this project. You will notice that you must first install the following packages: yFinance, Pandas, Numpy, Matplotlib, Seaborn, and Pathlib. If you hit run all, it should allow these to download onto your device and then it will execute the subsequent code.

---- For Copy into the Terminal----
pip install yfinance
pip install matplotlib
pip install seaborn
---- ----

----- Results: ------
 It appears daily VIX volume closing levels exhibit a strong right-skewed distribution. The majority of trading days between tend to stay between 15 and 25 points with an extended tail above 30 during market turmoil.

 The percentage of negative S&P 500 trading days increases across volatility brackets, rising from 35.9% in the Low regime (0–15) to 61.7% in the Extreme regime (30+).

 VIX daily point changes and S&P 500 percentage returns display a medium strength negative correlation, r = -0.782, with the largest downward equity swings occurring during X-Treme volatility spikes.
 
 Please note that if used for different time periods, results may vary.
 ---- ----