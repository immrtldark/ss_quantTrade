from download import constructYFURL
from download import download
ticker= "^GSPC"

start_date="2015-01-01"

end_date="2016-01-01"

freq = "d"

yfURL = constructYFURL(ticker,start_date,end_date,freq)

print (yfURL)


#Testing the download function

localFilePath = "tmp/pytest/gspc.csv"

download(localFilePath,yfURL)