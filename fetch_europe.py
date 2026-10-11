import yfinance as yf
# Display name -> Yahoo Finance ticker
EUROPE = {
    "Euro Stoxx 50": "^STOXX50E",
    "DAX": "^GDAXI",
    "EU Banks": "EXV1.DE",
    "EU Technology": "EXV3.DE",
    "EU Utilities": "EXH9.DE",
    "PKO BP": "PKO.WA",
    "Pekao": "PEO.WA",
    "XTB": "XTB.WA",
    "EUR/PLN": "EURPLN=X",
}
# Download daily closing prices, adjusted for dividends and splits
prices = yf.download(list(EUROPE.values()), start="2020-01-01", end = "2026-01-01",
                     auto_adjust=True, progress=False)["Close"]

# Replace tickers with readable names
prices = prices.rename(columns={v: k for k, v in EUROPE.items()})

# Save to CSV
prices.to_csv("data/europe_prices.csv")

print(prices.tail())
print(prices.isna().sum())
print(f"Period: {prices.index.min().date()} to {prices.index.max().date()}")
print(f"Trading days: {len(prices)}")