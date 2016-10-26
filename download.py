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

## Imports ##
from datetime import datetime

## Functions ##

#construct Yahoo! Finance URL
def constructYFURL(ticker,start_date,end_date,freq):
    start_date = datetime.strptime(start_date,"%Y-%m-%d").date() #set start date in correct format
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date() #set end date in correct format
    
    s=ticker.replace("^","%5E") #replaces ^ in ticker with %5E notation
    
    #start date items
    #month always has 2 digits
    if start_date.month-1 < 10:
        a = "0" + str(start_date.month-1) #appends a 0
    else:
        a= str(start_date.month-1)#month of start date (index is from 0)
    b= str(start_date.day) #day of start date
    c= str(start_date.year) #year of start date
    
    #end date items
    #month always has 2 digits
    if end_date.month-1 <10:
        d = "0" + str(end_date.month-1) #appends a 0
    else:
        d= str(end_date.month-1) #month of end date
    e= str(end_date.day) #day of end date
    f= str(end_date.year) #year of end date
    g= freq #frequency d= daily, w= weekly, m= monthly
    
    #Setup the URL
    yfURL = "http://chart.finance.yahoo.com/table.csv?s="+s+"&a="+a+"&b="+b+"&c="+c+"&d="+d+"&e="+e+"&f="+f+"&g="+g+"&ignore=.csv"
    return yfURL

#Download file and save to local path
def download(file_Path,url_of_file):
    import urllib.request
    import urllib.error
    
    #Use a function from urllib to download a url and save to a local path
    webRequest = urllib.request.Request(url_of_file)
    
    #Rest of the code will be in try:/except: pair in case of failure
    
    try:
        page =  urllib.request.urlopen(webRequest)
        #save contents of web request to variable 'content'
        #file form of the URL
        
        content= page.read()
        
        with open(file_Path,'wb') as output:
            output.write(bytearray(content))
        #reads bytes in content and then writes to local file.
        #allows function to be filetype agnostic
        
    except urllib.error.HTTPError as err:
        #Print an error, if any resulted
        print (err.fp.read())
        

    