import yfinance as yf
import wikipedia


org = "Tesla"

# WIKIPEDIA DATA #

wikipedia.search(org)
wiki_name = "Tesla, Inc."
wikipedia.summary(wiki_name)
page = wikipedia.page(wiki_name)
print(page)

# FINANCIAL DATA #

ticker = "TSLA"
ydata = yf.Ticker(ticker)

# number of shares in millions
shares = ydata.shares.values[-1][0]/1000000

# major holders
investors = ydata.major_holders
investors_institutional = ydata.institutional_holders
print(investors)
print(investors_institutional)


# SUSTAINABILITY DATA #

# sustainability data as pd dataframe: 2 col
susty_yahoo = ydata.sustainability

# NEWS #

# news
news_yahoo = ydata.news


# GENERAL DATA #

# Wikipedia #


"""

NOTES:

How to correctly read the the multi-level columns after saving the dataframe to a csv with pandas.DataFrame.to_csv

"""