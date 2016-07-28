prices = {}
stock = {}
revenue = {}

def make_dat_money(prices,stock):
    """ creates dictionary of item and predicted revenue"""
    a = 0
    for i in prices:
       revenue[i] = int(prices[i]) * int(stock[i])
    for b in revenue:
        a += int(revenue[b])
    return a

def Add_item(item,price,stocks):
    """adds item to stock and price dictionaries"""

    prices[item] = price
    stock[item] = stocks
    
#Asks number of items being added
items = int(raw_input("How many items are you adding?"))
#asks 'items' number of times
for i in xrange(0, items):
    Add_item(
    raw_input("What have we added to the stock Manager?"), 
    raw_input("How much does it cost?"),
    raw_input("How many do we have?")
    )
    print #keeping that style

make_dat_money(prices,stock)
print #blank lines make it pretty
print "We will make %s dollars" % (make_dat_money(prices,stock))
print #blank lines make it pretty
print "The individual prices related to each item are as follows"
print revenue