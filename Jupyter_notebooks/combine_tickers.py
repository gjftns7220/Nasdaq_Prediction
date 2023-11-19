import yfinance as yf
import os
import pandas as pd

us_tickers = [
    "AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "META", "BRK-B", "TSLA", "LLY", "V", 
    "UNH", "JPM", "XOM", "WMT", "AVGO", "MA", "JNJ", "PG", "ORCL", "HD", 
    "ADBE", "CVX", "ASML", "MRK", "COST", "KO", "ABBV", "BAC", "PEP", "SHEL", 
    "CRM", "BABA", "ACN", "NFLX", "MCD", "NVS", "AMD", "CSCO", "INTC", "TMO", 
    "SAP", "ABT", "TMUS", "CMCSA", "PFE", "DIS", "NKE", "WFC", "VZ", "QCOM", 
    "T", "UBER", "RTX", "ABNB", "SNPS", "CVS", "SHOP", "REGN", "C", "MU", 
    "GILD", "LRCX", "AMT", "SBUX", "AXP", "SNY", "NEE", "LOW", "AMAT", "BUD", 
    "SONY", "ISRG", "BLK", "PFE", "GS", "LMT", "TXN", "IBM", "COP", "NOW", 
    "UNP", "MS", "GE", "SPGI", "CAT", "SIE.DE", "UPS", "HON", "BA", "DE", 
    "BMY", "PFE", "AZN", "INTC", "CMCSA", "MRK", "WFC", "JNJ", "PG", "KO"
]

for ticker in us_tickers:
    data = yf.download(ticker)
    data.to_csv(f"ticker\{ticker}.csv")

directory = "ticker"
all_files = os.listdir(directory)

combined_data = pd.DataFrame()

for file in all_files:
    if file.endswith(".csv"):
        file_path = os.path.join(directory, file)
        df = pd.read_csv(file_path)
        combined_data = pd.concat([combined_data, df])

combined_data.reset_index(drop=True, inplace=True)
combined_data.to_csv("combined_tickers.csv", index=False)