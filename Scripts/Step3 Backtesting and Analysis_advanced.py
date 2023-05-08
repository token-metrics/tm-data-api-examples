import backtrader as bt
import backtrader.feeds as btfeeds


class TM_API_data(btfeeds.GenericCSVData):
    # add only three columns called date, Bitcoin, Ethereum
    lines = ('ta_grade','quant_grade','trader_grade')

    params = (
        ('nullvalue', float('NaN')),
        ('dtformat', '%Y-%m-%d'),
        # ('tmformat', '%H:%M:%S'),

        ('datetime', 0),
        # ('time', 0),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', -1),
        ('ta_grade', 6),
        ('quant_grade', 7),
        ('trader_grade', 8),
    )

class EMACloseSignal(bt.Indicator):
    lines = ('trader_grade_A', 'trader_grade_B', 'signal')
    params = (('period_A', None),('period_B', None),)
    
    def __init__(self):
        self.lines.trader_grade_A = bt.talib.EMA(self.datas[0].trader_grade, timeperiod=self.p.period_A, subplot=True)
        self.lines.trader_grade_B = bt.talib.EMA(self.datas[0].trader_grade, timeperiod=self.p.period_B, subplot=True)
        self.lines.signal = self.lines.trader_grade_A > self.lines.trader_grade_B



class TMStrategy(bt.Strategy):
    params = (('period_A', None),('period_B', None),)

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        # print('%s, %s' % (dt, txt))

    def __init__(self):
        """Initialize the strategy"""
        self.dataclose = self.datas[0].close

        # for single strategy
        self.myindicator = EMACloseSignal(self.datas[0], period_A=self.p.period_A, period_B=self.p.period_B, plot=True)
        self.signal = self.myindicator.lines.signal
        

        # To keep track of pending orders
        self.order = None
        self.buyprice = None
        self.buycomm = None

    def calculate_size(self,slipage = 0.1):
        # full position
        cash = self.broker.get_cash()
        size = cash/(self.data.close[0] * (1+slipage))
        return size

    def next(self):
        """Run once per data bar"""
        size = self.calculate_size(slipage=0)
        self.log(f"Close, {self.dataclose[0]}, ta_grade, {self.datas[0].trader_grade[0]}, signal, {self.signal[0]}, tg_A, {self.myindicator.lines.trader_grade_A[0]}, tg_B, {self.myindicator.lines.trader_grade_B[0]}")

        # Check if an order is pending
        if self.order:
            return

        # We are not in the market
        if not self.position:
            if self.signal[0]: # Buy signal
                self.log(f"BUY CREATE, {self.dataclose[0]}")
                self.order = self.buy(size=size) # Long position

            else: # Sell signal
                self.log(f"SELL CREATE, {self.dataclose[0]}")
                self.order = self.sell(size=size) # Short position

        # We in a short position but given a Buy signal
        elif self.signal[0] and self.position.size < 0:

            self.log(f"SELL Close, {self.dataclose[0]}")
            self.order = self.close() # we close our current position

        # We in a long position but given a Sell signal
        elif not self.signal[0] and self.position.size > 0:
                
            self.log(f"BUY Close, {self.dataclose[0]}")
            self.order = self.close()


    def notify_order(self, order):
        
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))
                
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
                
            elif order.issell() : # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

            elif order.isclose():
                self.log('Order closed EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))  

def runstart():
    cerebro = bt.Cerebro(cheat_on_open=True)
    cerebro.addstrategy(TMStrategy, period_A=3, period_B=7)
    # cerebro.optstrategy(TMStrategy, period_A=range(2, 10), period_B=range(2, 10))

    cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='SharpeRatio')
    cerebro.addanalyzer(bt.analyzers.Returns, _name='Returns')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='DrawDown')

    cerebro.broker.setcash(100000.0)
    cerebro.adddata(TM_API_data(dataname='../Data/TMdata.csv'))
    cerebro.broker.setcommission(commission=0.0004)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    result = cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # # for optimization
    # for strat in result:
    #     print('Parameters:', strat[0].p.period_A, strat[0].p.period_B)
    #     print('Sharpe Ratio:', strat[0].analyzers.SharpeRatio.get_analysis()['sharperatio'])
    #     print('Returns:', strat[0].analyzers.Returns.get_analysis()['rtot'])

    # for single strategy
    strat = result[0]
    print('Sharpe Ratio:', strat.analyzers.SharpeRatio.get_analysis()['sharperatio'])
    print('DrawDown:', strat.analyzers.DrawDown.get_analysis()['max']['drawdown'])

    # pyfoliozer 
    # pyfoliozer = strat.analyzers.getbyname('pyfolio')
    # returns, positions, transactions, gross_lev = pyfoliozer.get_pf_items()
    # returns.to_csv('result/returns.csv')
    # positions.to_csv('result/positions.csv')
    # transactions.to_csv('result/transactions.csv')
    # gross_lev.to_csv('result/gross_lev.csv')

    cerebro.plot() 
    


if __name__ == '__main__':
    runstart()