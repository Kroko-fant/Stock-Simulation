from simulation import stock, szenario
import threading
import time as t
from pylab import *

stock1 = stock.Stock("???", 57.6, 10, 1)
szenario = szenario.Szenario(0)
end = []


def ticker(stockobj, intervall=1, length=100):
    for x in range(0, length):
        stockobj.update(szenario)
        szenario.updateszenario()
        t.sleep(intervall)
        if x % 1_000 == 0:
            end.append(stock1.last_price)
    minmax = arange(0, len(end), 1)
    plot(minmax, end)
    xlabel('Zeiteinheiten')
    ylabel('Price')
    title(f'Chart von {stock1.name}')
    grid(True)
    show()


thread = threading.Thread(target=ticker, args=(stock1, 0, 500_000))
thread.start()
