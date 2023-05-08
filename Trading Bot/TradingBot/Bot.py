import TradingBot.BotTools as bot
import TradingBot.NewOrder as NewOrder
import TradingBot.ExchangeInfo as ExchangeInfo
import TradingBot.AccountInfo as AccountInfo
import TradingBot.OrderInfo as OrderInfo
import TradingBot.CancelOrder as CancelOrder
import TradingBot.TickerInfo as TickerInfo

from typing import Dict, List, Union, Optional, Any



class Bot(object):
    def __init__(self, exchange = None, api_keys = None):
        
        # API dictionary includes the api key and api secret and other essential information for authentication
        self.api_keys = api_keys 
        self.exchange = exchange
        
    def switch_exchange(self, exchange, api_keys = None):
        self.exchange = exchange
        self.api_keys = api_keys
    
    def load_key(self, api_keys):
        self.api_keys = api_keys 

    def bot_status(self):
        print("Current exchange: %s" % self.exchange)
        print("Current api_keys: %s" % self.api_keys)
    
    def new_Order(self, commands: Dict[str, Dict[str, str]]):
        
        # todo Step1: translate the commands to the parameters for the exchange
        params = bot.commands_transform_trade(self.exchange, commands)
        print(f'Commands: ', params)
        
        print("Execute the trade")
        response = NewOrder.execute(self.exchange, self.api_keys, params)
        print(response)
        return response
        
        
    def get_ExchangeInfo(self):
        response = ExchangeInfo.execute(exchange = self.exchange)
        return response
        
    def get_AccountInfo(self):
        response = AccountInfo.execute(exchange = self.exchange, api_keys = self.api_keys)
        return response
    
    def get_OpenOrderInfo(self):
        response = OrderInfo.execute(exchange = self.exchange, api_keys = self.api_keys)
        return response
    
    def make_CancelOrder(self, orderid: str, symbol: Optional[str] = '') -> Union[Dict, List]:
        response = CancelOrder.execute(exchange = self.exchange, api_keys = self.api_keys, orderid = orderid, symbol = symbol)
        return response
    
    def get_TickerInfo(self, symbol: str):
        response = TickerInfo.execute(exchange = self.exchange, symbol = symbol)
        return response
    
    
        
        
        

        
    
    
    