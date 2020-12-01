import backtrader
import datetime
from strategies import TestStrategy

cerebro = backtrader.Cerebro()

cerebro.broker.set_cash(1000000)

 # Create a Data Feed
data = backtrader.feeds.YahooFinanceCSVData(
    dataname='oracle.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(2000, 1, 1),
    # Do not pass values before this date
    todate=datetime.datetime(2000, 12, 31),
    # Do not pass values after this date
    reverse=False)

# add Strategy
cerebro.addstrategy(TestStrategy)

# add data
cerebro.adddata(data)

print('starting portfoilio value: ' + str(cerebro.broker.getvalue()))

cerebro.run()

print('starting portfoilio value: ' + str(cerebro.broker.getvalue()))
