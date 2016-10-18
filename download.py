#Author: Scott Chilton

#This script will download data files from Yahoo Finance for specific tickers

#SPY Max Daily
#http://chart.finance.yahoo.com/table.csv?s=SPY&a=0&b=29&c=1993&d=9&e=17&f=2016&g=d&ignore=.csv

#SPY Max Weekly
#http://chart.finance.yahoo.com/table.csv?s=SPY&a=0&b=29&c=1993&d=9&e=17&f=2016&g=w&ignore=.csv

#SPY Max Monthly
#http://chart.finance.yahoo.com/table.csv?s=SPY&a=0&b=29&c=1993&d=9&e=17&f=2016&g=m&ignore=.csv

#AMZN Max Daily
#http://chart.finance.yahoo.com/table.csv?s=AMZN&a=4&b=16&c=1997&d=9&e=17&f=2016&g=d&ignore=.csv

#a,b,c = month, day, year for start date
#month indexing starts at 0
#d,e,f = month, day, year for end date
#month indexing starts at 0
#g = frequency d,w,m (daily, weekly, monthly)