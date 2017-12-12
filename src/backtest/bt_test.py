import bt
import matplotlib.pyplot as plt
data = bt.get('spy,agg', start='2010-01-01')
s = bt.Strategy('s1', [bt.algos.RunMonthly(),
                       bt.algos.SelectAll(),
                       bt.algos.WeighEqually(),
                       bt.algos.Rebalance()])
test = bt.Backtest(s, data)
res = bt.run(test)
res.plot()
plt.show()
