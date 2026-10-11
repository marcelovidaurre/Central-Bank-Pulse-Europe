Central Bank Pulse: Europe

How ECB and NBP interest rate decisions move Eurozone and Polish stocks, sectors and EUR/PLN.

Part 1 of the Central Bank Pulse series: Europe · United States (coming soon) · Peru (coming soon)

Overview

Central banks change interest rates to control inflation, and those decisions ripple through every financial market. Some sectors gain, others lose, and currencies shift as money flows toward higher returns.

This project measures those ripples in Europe. It tracks two central banks:

European Central Bank (ECB): sets rates for the 20 countries that use the euro.
National Bank of Poland (NBP): sets rates for the Polish złoty.

Using daily market data from January 2020 to today, the project covers three very different rate environments: the 2020 pandemic cuts, the 2022 to 2023 hiking cycle, and the easing period that followed.

Why this study matters

Rate decisions are among the most watched events in finance, yet their effect is uneven and often misunderstood. This study turns that into measurable evidence.

Who	How they can use it
Investors	See which sectors historically gained or lost after hikes and cuts, and set expectations before the next decision.
Companies trading between Poland and the Eurozone	Understand how the NBP and ECB rate gap moves EUR/PLN, which affects import costs, export revenue and currency hedging.
People earning or saving in two currencies	Judge when the złoty tends to strengthen or weaken against the euro.
Analysts and students	A transparent, reproducible example of an event study with public data and open code.
Research questions
Sector reaction: How do European banks, technology and utilities perform in the days around ECB rate hikes compared with cuts?
Polish market: Do Polish bank stocks (PKO BP, Pekao) react more to NBP decisions or to ECB decisions?
Currency: When the NBP and ECB move rates in different directions, how does EUR/PLN respond?
Risk: Does market volatility rise around decision dates?
Scope
Market	Instruments	Central bank
Eurozone	Euro Stoxx 50, DAX	ECB
European sectors	STOXX Europe 600 Banks, Technology and Utilities ETFs	ECB
Poland	PKO BP, Pekao, XTB (Warsaw Stock Exchange)	NBP
Currency	EUR/PLN	ECB and NBP

Period: January 2018 to today, daily data.

Data sources

All data is free and public.

Prices and FX: Yahoo Finance, via the yfinance Python library.
ECB deposit facility rate: FRED, Federal Reserve Bank of St. Louis (series ECBDFR).
NBP reference rate: National Bank of Poland, official rate archive.
Methodology
Collect daily prices, exchange rates and policy rate history.
Clean the data: align trading calendars across exchanges and handle holidays.
Measure daily returns and rolling volatility. Returns are used instead of prices so assets in different currencies can be compared.
Detect rate decision dates automatically from changes in the policy rate series.
Event study: measure cumulative returns from 5 trading days before to 5 trading days after each decision, then compare the average reaction to hikes against cuts.
Currency analysis: compare EUR/PLN with the rate gap between the NBP and the ECB.
Present the findings in an interactive dashboard.
Project roadmap
 Create repository
 1.1 Download European market prices
 1.2 Calculate returns and volatility
 1.3 Collect ECB and NBP rate history
 1.4 Store data in a SQLite database
 1.5 Event study on ECB and NBP decisions
 1.6 EUR/PLN vs. the NBP-ECB rate gap
 1.7 Interactive dashboard and key findings
How to run
bash
git clone https://github.com/marcelovidaurre/Central-Bank-Pulse-Europe.git
cd Central-Bank-Pulse-Europe
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python fetch_europe.py
Key findings

Coming soon, as each step is completed.

Limitations
Markets react to expected decisions before they happen, so part of the effect may appear before the decision date.
Other events (inflation data, earnings, geopolitics) can move prices in the same window.
Past reactions do not guarantee future ones.
Tech stack

Python · pandas · yfinance · SQLite · Streamlit · Plotly

Disclaimer

This project is for educational and research purposes only. It is not investment advice.

Author

Marcelo Vidaurre · GitHub
