

import requests as rq
import pandas as pd

stocks=pd.read_csv('D:/stocks.csv',encoding='ISO-8859-1')

slist=stocks.to_dict(orient='records')

currencyurl =f'https://api.coinbase.com/v2/exchange-rates'
currencyheader={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'

}
currencyparams={'currency': 'USD'}
cresp=rq.get(url=currencyurl,headers=currencyheader,params=currencyparams)

if cresp.status_code==200:
    cdata=cresp.json()
    Inr_usd_rate=float(cdata['data']['rates']['INR'])
else:
    print(f'failed to fetch :{cresp.status_code}')
    exit()

for st  in slist:
    if st['currency']=='USD':
        st['INR']=(float(st['price'])* Inr_usd_rate)
    elif st['currency'] =='SGD':
        sgdrate= float(cdata['data']['rates']['SGD'])
        st['INR']=(float(st['price'])* sgdrate* Inr_usd_rate)
    else:
        st['INR']=None


updtate_stock=pd.DataFrame(slist)
output='update_stock.csv'
updtate_stock.to_csv(output,index=False)



        




