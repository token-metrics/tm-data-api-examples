import typing
from typing import Dict, List, Tuple, Union
def commands_transform_trade(exchange:str, commands:Dict[str, dict[str, str]]) -> dict[str, Union[str, int, float]]:
    """Differernt exchanges have different parameters for the trade. This function is to translate the commands to the parameters for the exchange

    Args:
        exchange (str): It is the name of the exchange, for example, 'binance', 'kraken', 'kucoin', 'gate', 'binanceus', 'bitmex', 'coinbasepro', 'bittrex', 'gemini'
        commands (Dict[str, dict[str, str]]): Dictionary of commands. The commands are the parameters for the trade. The commands are the same for all exchanges before the translation.

    Returns:
        dict[str, Union[str, int, float]]: After the translation, the parameters for the trade are returned. The parameters are different for different exchanges.
    """

    public_params: dict[str, Union[str, int, float]] = commands["public_params"]
    private_params:dict[str, Union[str, int, float]]= commands["private_params"]
    
    param = {}
    
    # todo: public params
    if exchange.lower() == 'binance':
        param['symbol'] = public_params['symbol']
        param['side'] = public_params['side']
        param['quantity'] = public_params['quantity']
        param['type'] = public_params['type']
        param['price'] = public_params['price']
        param['stopPrice'] = public_params['stopPrice']
        
    elif exchange.lower() == 'kraken':
        
        param['pair'] = public_params['symbol']
        param['type'] = public_params['side']
        param['volume'] = public_params['quantity']
        param['ordertype'] = public_params['type']
        param['price'] = public_params['price']
        param['price2'] = public_params['stopPrice']
        
    
    elif exchange.lower() == 'kucoin':
        # https://docs.kucoin.com/#place-a-new-order
        param['symbol'] = public_params['symbol']
        param['side'] = public_params['side']
        param['size'] = public_params['quantity']
        param['type'] = public_params['type']
        param['price'] = public_params['price']
        param['stopPrice'] = public_params['stopPrice']
        
    elif exchange.lower() == 'gate':
        
        param['currency_pair'] = public_params['symbol']
        param['side'] = public_params['side']
        param['amount'] = public_params['quantity']
        param['type'] = public_params['type']
        param['price'] = public_params['price']

    elif exchange.lower() == 'binanceus':
        param['symbol'] = public_params['symbol']
        param['side'] = public_params['side']
        param['quantity'] = public_params['quantity']
        param['type'] = public_params['type']
        param['price'] = public_params['price']
        param['stopPrice'] = public_params['stopPrice']

    elif exchange.lower() == 'bittrex':
        param['marketSymbol'] = public_params['symbol']
        param['direction'] = public_params['side']
        param['quantity'] = public_params['quantity']
        param['type'] = public_params['type']
        param['limit'] = public_params['price']
        param['ceiling'] = public_params['stopPrice']
        
    elif exchange.lower() == 'coinbasepro':
        param['product_id'] = public_params['symbol']
        param['side'] = public_params['side']
        param['size'] = public_params['quantity']
        param['type'] = public_params['type']
        param['price'] = public_params['price']
        param['stop_price'] = public_params['stopPrice']
        

    elif exchange.lower() == 'gemini':
        param['symbol'] = public_params['symbol']
        param['side'] = public_params['side']
        param['amount'] = public_params['quantity']
        param['type'] = public_params['type']
        param['price'] = public_params['price']
        param['stop_price'] = public_params['stopPrice']

    # Private params are unique for each exchange, where user needs to provide according to the exchange's requirement.
    if private_params:
        param.update(private_params) # combine the parameters
        
    # drop all "" param
    param = dict((k, v) for k, v in param.items() if v !='')
    return param
        
        
        
        
        
        
        
        
    