from download import constructYFURL

ticker= "^GSPC"

start_date="2015-01-01"

end_date="2016-01-01"

freq = "d"

yfURL = constructYFURL(ticker,start_date,end_date,freq)

print (yfURL)