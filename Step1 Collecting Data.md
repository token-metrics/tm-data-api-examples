# Obatin data from Data API

From this tutorial, we will go through the data collection phase and give you a guidebook about obtaining our TM data as well as the market data.

## Table of Content

- [Obatin data from Data API](#obatin-data-from-data-api)
  * [Preparation before the action](#preparation-before-the-action)
  * [Obtain the coins index from the `Tokens` endpoint](#obtain-the-coins-index-from-the--tokens--endpoint)
  * [Obtain the Market price from the exchange](#obtain-the-market-price-from-the-exchange)
  * [Obtain the features from `Trader Grades` endpoint](#obtain-the-features-from--trader-grades--endpoint)
- [Appendix](#appendix)

## Preparation before the action

Here are the packages we needed.

```python
import requests
from pandas import json_normalize
from urllib.parse import urlencode

from typing import Dict, List, Union, Optional, Any
import warnings

warnings.filterwarnings("ignore")
```

Here is a useful function built to help connect to our platform. Just put your API key in `<your API key>` and explore endpoints as you wished.


```python
API_key = '<your API key>'

def tm_API(endpoint: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
	"""Obtain data from the Token Metrics Data API

	Args:
		endpoint (str): The endpoint of the API
		payload (Optional[Dict[str, Any]], optional): The parameters to send to the API. Defaults to None.

	Returns:
		Dict[str, Any]: The response from the API
	"""

	if payload:
		url = 'https://alpha.data-api.tokenmetrics.com/v1/' + endpoint + '?' + urlencode(payload)
	else:
		url = 'https://alpha.data-api.tokenmetrics.com/v1/' + endpoint 
	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'api_key': API_key}
	response = requests.get(url, headers=headers)
	return response.json()
```

## Obtain the coins index from the `Tokens` endpoint

Now, once we have all the tools ready, what do we need first? It is the **Tokens** or **Symbol** absolutely! As shown in our `Guide`, all the tokens or symbol information were stored in the `tokens` endpoint. So we can extract the token information with the following code:

```python
endpoint = 'tokens'
params = {}
response = tm_API(endpoint,params)
coins = json_normalize(response['data'])
coins = coins.sort_values(by = 'TOKEN_ID').reset_index(drop = True)
coins[coins.NAME.isin(['Bitcoin','Ethereum','Litecoin'])].reset_index(drop = True)
```

| Index | TOKEN_ID | SYMBOL |     NAME |
| ----: | -------: | -----: | -------: |
|     0 |     3306 |    ETH | Ethereum |
|     1 |     3375 |    BTC |  Bitcoin |
|     2 |     3377 |    LTC | Litecoin |

> We filtered the table with three coins: `Bitcoin`, `Ethereum`, and `Litecoin` for the demo show.

Before going next steps, we want to claim that since this tutorial is aimed to show the whole process from a professional trader's thinking way, we will not consider complicated or complex strategies but focus on a simple one:`Long-Short Single asset trading strategy`.

Here is how we defined the `Long-Short Single asset trading strategy`: 

* We will focus on the `Bitcoin` asset only
* Three are only two statuses of the position: `Long`, `Short`, where we will only be in `Long position` or `Short position` at a time.

## Obtain the Market price from the exchange

```python
import pandas as pd
import datetime as dt
import requests
```



Next, we need to collect the market quotes for `Bitcoin`.

```python
# Obtain data from the Binance US API
params = {'symbol': 'BTCUSDT', 
       'interval': '1d', 
       'startTime': int(dt.datetime(2020,5,2).timestamp())*1000,
       'endTime': int(dt.datetime(2023,1,28).timestamp())*1000,
       'limit': 1000}
r = requests.get('https://api.binance.us/api/v3/klines', params = params).json()

# Convert to pandas dataframe
col = ['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades',
       'Taker buy volume','Taker buy quote asset volume','Ignore']
btcusdt = pd.DataFrame(r, columns = col)

btcusdt['Open time'] = btcusdt['Open time'].apply(lambda x: dt.datetime.fromtimestamp(x/1000)).dt.strftime('%Y-%m-%d')
btcusdt['Close time'] = btcusdt['Close time'].apply(lambda x: dt.datetime.fromtimestamp(x/1000)).dt.strftime('%Y-%m-%d')

# Clean up the data
btcusdt.rename(columns = {'Close time': 'Date'}, inplace = True)
btcusdt[['Open', 'High', 'Low', 'Close', 'Volume']] = btcusdt[['Open', 'High', 'Low', 'Close', 'Volume']].astype(float)
btcusdt = btcusdt[['Date','Open', 'High', 'Low', 'Close', 'Volume']]
btcusdt
```

We obtain the historical price of `BTCUSDT` from the `Binance US`. After some data-cleaning steps, we get the following table:

| Date |       Open |    High |     Low |   Close |  Volume |            |
| ---: | ---------: | ------: | ------: | ------: | ------: | ---------- |
|    0 | 2020-05-10 | 9531.93 | 9569.31 | 8127.14 | 8726.30 | 600.659830 |
|    1 | 2020-05-11 | 8730.15 | 9162.08 | 8200.00 | 8561.03 | 399.574609 |
|    2 | 2020-05-12 | 8560.18 | 8973.14 | 8533.72 | 8810.00 | 153.606379 |
|    3 | 2020-05-13 | 8808.62 | 9398.12 | 8800.91 | 9295.00 | 167.297195 |

And here is the plot of the data:

<div align="center"> <iframe src="Plots/btcusdt.html" width="90%" height="400"> </iframe> <p align = "right"> Sources: Binance US  </p> <p align = "left"> Figure 2 - BTCUSDT. </p>


## Obtain the features from `Trader Grades` endpoint

Our `Trader Grades` endpoint provides a comprehensive overview of price movements. Amplify information was hidden from this table where we will start exploring our trading idea from this endpoint. 

```python
endpoint = 'trader-grades'
params = {
	'tokens': '3375',
	'startDate': '2020-05-03T00:00:00.000Z',
	'endDate': '2023-01-27T00:00:00.000Z',
	'limit': 1000

}
r = tm_API(endpoint,params)
trader_grades = json_normalize(r['data'])
```

Once we extract the data from our API, we will only select `[['DATE','TA_GRADE','QUANT_GRADE','TM_TRADER_GRADE',]]` those most important features. Then do a simple transformation on those data.

```python
# select the columns we want
btc_tg = trader_grades[['DATE','TA_GRADE','QUANT_GRADE','TM_TRADER_GRADE',]]

# merge the data
data = pd.merge(btc_tg, btcusdt, left_on='DATE', right_on='Date', how='left').drop('Date', axis=1)

# do some transformations
data['DayReturnPCT'] = (data.Close/data.Close.shift(-1) - 1)*100
data['ta_gradePCT'] = (data['TA_GRADE']/data['TA_GRADE'].shift(-1) - 1)*100
data['quant_gradePCT'] = (data['QUANT_GRADE']/data['QUANT_GRADE'].shift(-1) - 1)*100
data['tm_trader_gradePCT'] = (data['TM_TRADER_GRADE']/data['TM_TRADER_GRADE'].shift(-1) - 1)*100
data['DailyReturnPCT'] = (data.Close/data.Open - 1)*100
```

Till now, we have collected all the data we need, please refer to the `btc_tg.csv`

```python
<class 'pandas.core.frame.DataFrame'>
Int64Index: 748 entries, 0 to 747
Data columns (total 14 columns):
 #   Column              Non-Null Count  Dtype         
---  ------              --------------  -----         
 0   DATE                748 non-null    datetime64[ns]
 1   TA_GRADE            747 non-null    float64       
 2   QUANT_GRADE         747 non-null    float64       
 3   TM_TRADER_GRADE     746 non-null    float64       
 4   Open                748 non-null    float64       
 5   High                748 non-null    float64       
 6   Low                 748 non-null    float64       
 7   Close               748 non-null    float64       
 8   Volume              748 non-null    float64       
 9   DayReturnPCT        747 non-null    float64       
 10  ta_gradePCT         745 non-null    float64       
 11  quant_gradePCT      745 non-null    float64       
 12  tm_trader_gradePCT  743 non-null    float64       
 13  DailyReturnPCT      748 non-null    float64       
dtypes: datetime64[ns](1), float64(13)
memory usage: 87.7 KB
```

# Appendix

[Code](https://github.com/token-metrics/tm-data-api-examples/blob/master/Scripts/Step1%20Collecting%20data.ipynb)



