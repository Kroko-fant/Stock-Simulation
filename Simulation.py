import stock
import threading
import szenario
import time as t

stock1 = stock.Stock("Test Company", 100, 1)
szenario = szenario.Szenario(0)


def ticker(stockobj, intervall=1, length=100):
    for _ in range(0, length):
        stockobj.update_price(szenario)
        print(str(stockobj))
        szenario.updateszenario(1)
        t.sleep(intervall)


thread = threading.Thread(target=ticker, args=(stock1, 1, 100))
thread.start()
