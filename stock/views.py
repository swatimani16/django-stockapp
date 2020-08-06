from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup
import plotly.graph_objects as go



# Create your views here.


def home(requests):
    url = 'https://www.cnn.com/business/media/'
    html = urlopen(url)
    soup3 = BeautifulSoup(html,'lxml')
    #HEADLINES OF THE DAY
    r4 = soup3.find_all('h3',{'class':'cd__headline'})[0].find_all('a')[0].find_all('span',{'class':'cd__headline-text'})[0].getText()
    # print(r4)
    ##LINK TO THE HEADLINES
    r5 = soup3.find_all('h3',{'class':'cd__headline'})[0].find_all('a')[0]['href']
    # print(r5)


    url = 'https://money.cnn.com/data/hotstocks/'
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    #DAY, DATE-TIME
    data_day = soup.find_all('div',{'class':'wsod_fRight'})[0].find_all('div',{'class':'wsod_mrktmsg'})[0].getText()
    from datetime import datetime
    date = str(datetime.now())

    # print(data_day)
    # print(date)
    # print(data_time)
    # print('\n')


    url = 'https://money.cnn.com/data/hotstocks/'
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    r = soup.find_all('tr')


    #DATA TIME-DOW, NASDAQ, S&P VALUES
    d = {}

    def getdata():
        url = 'https://money.cnn.com/data/hotstocks/'
        html1 = urlopen(url)
        soup1 = BeautifulSoup(html1, 'lxml')
        data_time = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('span',{'stream':'time_599362|579435|575769'})[0].getText()
        dow = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[0].find_all('a',{'class':'wsod_symbol'})[0].getText()
        dow_v1 = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[0].find_all('span',{'class','quoteChange'})[0].getText()
        dow_v2 = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[0].find_all('div',{'class':'bannerQuote'})[0].getText()
        dow_v3 = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[0].find_all('span',{'class':'quotePctChange'})[0].getText()
        
        nas = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[1].find_all('a',{'class':'wsod_symbol'})[0].getText()
        nas_v1 = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[1].find_all('span',{'class','quoteChange'})[0].getText()
        nas_v2 = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[1].find_all('div',{'class':'bannerQuote'})[0].getText()
        nas_v3 = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[1].find_all('span',{'class':'quotePctChange'})[0].getText()
        
        snp = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[2].find_all('a',{'class':'wsod_symbol'})[0].getText()
        snp_v1 = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[2].find_all('span',{'class','quoteChange'})[0].getText()
        snp_v2 = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[2].find_all('div',{'class':'bannerQuote'})[0].getText()
        snp_v3 = soup1.find_all('div',{'class':'wsod_fRight'})[0].find_all('ul')[0].find_all('li')[2].find_all('span',{'class':'quotePctChange'})[0].getText()
        
        
    #     print(data_time)
    #     print(dow)
    #     print(dow_v1)
    #     print(dow_v2)
    #     print(dow_v3)
        
    #     print(nas)
    #     print(nas_v1)
    #     print(nas_v2)
    #     print(nas_v3)
        
    #     print(snp)
    #     print(snp_v1)
    #     print(snp_v2)
    #     print(snp_v3)
        
        d['dow'] = dow
        d['dow_v1'] = dow_v1
        d['dow_v2'] = dow_v2
        d['dow_v3'] = dow_v3
        d['nas'] = nas
        d['nas_v1'] = nas_v1
        d['nas_v2'] = nas_v2
        d['nas_v3'] = nas_v3
        d['snp'] = snp
        d['snp_v1'] = snp_v1
        d['snp_v2'] = snp_v2
        d['snp_v3'] = snp_v3
        d['data_time'] = data_time
        # d['dow'] = dow
        # d['dow_v1'] = dow_v1
        return d





    d = getdata()
    l=[]
    l1=[]
    x = []
    price = []
    change = []
    changeper = []
    for rows in r:
    #     print("rows: ",rows)
    #     print(rows)
        if rows.find_all('a') != []:
            l.append(rows.find_all('a')[0].getText()) 
            x.append(rows.find_all('a')[0]['href']) 
    #         print("x:",x)
        if rows.find_all('span') != []:
            l1.append(rows.find_all('span')[0].getText())
        if rows.find_all('td',{'class':'wsod_aRight'})!=[]:
            price.append(rows.find_all('span')[1].getText())
            change.append(rows.find_all('span')[2].getText())
            changeper.append(rows.find_all('span')[4].getText())

    # print(d)
    # print(l)
    # print('\n')
    # print(l1)
    # print('\n')
    print(x)
    print('\n')
    # print(price)
    # print('\n')
    # print(change)
    # print('\n')
    # print(changeper)
    
    context = {
        'headline': r4,
        'url' : r5,
        'data_day' : data_day,
        'date' : date,
        'data_time' : d['data_time'],
        'dow' : d['dow'],
        'dow_1' : d['dow_v1'],
        'dow_2' : d['dow_v2'],
        'dow_3' : d['dow_v3'],
        'nas' : d['nas'],
        'nas_1' : d['nas_v1'],
        'nas_2' : d['nas_v2'],
        'nas_3' : d['nas_v3'],
        'snp' : d['snp'],
        'snp_1' : d['snp_v1'],
        'snp_2' : d['snp_v2'],
        'snp_3' : d['snp_v3'],
        'most_active' : l[0:10],
        'gainers' : l[10:20],
        'losers' : l[20:30],
        'ma_price' : price[0:10],
        'ma_change' : change[0:10],
        'ma_cper' : changeper[0:10],
        'g_price' : price[10:20],
        'g_change' : change[10:20],
        'g_cper' : changeper[10:20],
        'l_price' : price[20:30],
        'l_change' : change[20:31],
        'l_cper' : changeper[20:31]
        
    }
    return render(requests, 'index.html',context)


def search_stock(request):
    x = []   #Getting the urls of the stocks
    url = 'https://money.cnn.com/quote/quote.html?symb='+str(request.GET['search'])
    print(url)
    html = urlopen(url)
    soup = BeautifulSoup(html,'lxml')
    r1 = soup.find_all('div',{'class':'clearfix wsod_pgHeader'})[0].find_all('h1',{'class':'wsod_fLeft'})[0].getText()
    r2 = soup.find_all('tr')[0].find_all('td',{'class':'wsod_last'})[0].getText()
    r3 = soup.find_all('tr')[0].find_all('td',{'class':'wsod_change'})[0].getText()
    print(r3)
    v1 = 0
    for i in r2:
        if i.isnumeric():
            v1+=1 
    v2 = 0
    for j in r3:
        if j == '%':
            break
        else:
            v2+=1
    indexes = [0,1,2,3,4,5]
    indexes1 = [0,1]
    r = []
    for j in indexes:
        for k in indexes1:
            r.append(soup.find_all('div',{'class':'clearfix wsod_DataColumnLeft'})[0].find_all('tr')[j].find_all('td')[k].getText())
            print(r)
    from datetime import datetime
    date = str(datetime.now())

    # fig = go.Figure(data=[go.Candlestick(x=df['Date'],
    #             open=r[3], high=df['AAPL.High'],
    #             low=df['AAPL.Low'], close=df['AAPL.Close']
    #                  ])
    # graph = fig1.to_html(full_html=False, default_height=500, default_width=300)
    context = {
        'stock_name': r1,
        'v1': r2[0:v1-2],
        'p' : r3[0:v2],
        'p_close' : r[0],
        'p_close_v' : r[1],
        'to' : r[2],
        'to_v' : r[3],
        'dr' : r[4],
        'dr_v' : r[5],
        'v' : r[6],
        'v_v' : r[7],
        'av' : r[8],
        'av_v' : r[9],
        'mc' : r[10],
        'mc_v' : r[11],
        'date' : date
        # 'graph' : graph
    }
    return render(request, 'search.html',context) 