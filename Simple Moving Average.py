# Put any initialization logic here.  The context object will be passed to
# the other methods in your algorithm.
def initialize(context):
    context.security = symbol('SPY')

# Will be called on every trade event for the securities you specify. 
def handle_data(context, data):
   print(data)
   MA1 = data[context.security].mavg(50)
   MA2 = data[context.security].mavg(200)
#these are just two moving averages, one for 50 days the other for 200 days to see if the stock is trending up or down
              
   current_price = data[context.security].price
   current_positions = context.portfolio.positions[symbol('SPY')].amount
   cash = context.portfolio.cash
   
              
   if (MA1 > MA2) and current_positions == 0:
       number_ofshares = int(cash/current_price)
       order(context.security, number_ofshares)
       log.info('Buying Shares')
   
   elif (MA1 < MA2) and current_positions != 0:
       order_target(context.security, 0)
       log.info('Selling Shares')
              
   record(MA1 = MA1, MA2 = MA2, Price = current_price)
              
 