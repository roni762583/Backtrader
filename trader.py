import backtrader

cerebro = backtrader.Cerebro()

print('starting portfoilio value: ' + str(cerebro.broker.getvalue()))

cerebro.run()

print('starting portfoilio value: ' + str(cerebro.broker.getvalue()))
