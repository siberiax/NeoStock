import re

def parseData(data):
    goodStocks = []
    toSell = []

    whatwewant1 = data.split("marquee")

    whatwewant2 = whatwewant1[1].split("<b>")

    stocks = []
    for i in range(len(whatwewant2)):
        whatwewant3 = whatwewant2[i].split("</b>")
        stocks.append(whatwewant3[0])

    for stock in stocks:
        fields = stock.split()
        if ("href" in fields[1]):
            continue
        value = int(fields[1])
        if (value == 15):
            if (fields[0] not in goodStocks):
                goodStocks.append(fields[0])
        if (value > 59):
            if (fields[0] not in toSell):
                toSell.append(fields[0])
    if (len(goodStocks) == 0):
        print ("Nothing to buy right now")
    if (len(goodStocks) == 1):
        print ("Buy: " + goodStocks[1])
    parseData2(data, goodStocks, toSell)

def parseData2(data, goodStocks, toSell):
    bestValue = 999
    bestStock = ""
    for stock in goodStocks:
        firstSplit = stock + "\">"
        if (firstSplit not in data):
            bestStock = stock
            break
        whatwewant1 = data.split(firstSplit)
        whatwewant2 = whatwewant1[1].split("<td align=\"center\"><b>Shares</b></td>")

        whatwewant3 = whatwewant2[0].split("<td align=\"center\">")
        whatwewant4 = whatwewant3[4].split()
        whatwewant5 = whatwewant4[0].split(",")
        stockVal = int(whatwewant5[0])
        if (stockVal < bestValue):
            bestValue = stockVal
            bestStock = stock
    print ("Buy: " + bestStock)
    sellIt = []
    for stock in toSell:
        ownIt = stock + "\">"
        if (ownIt in data):
            sellIt.append(stock)
    for stock in sellIt:
        print ("Sell: " + stock)
