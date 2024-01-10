import pandas as pd
import yfinance as yf
import datetime

def options_chain(tk):
    # Builds the Options chain of tk
    opt = pd.DataFrame()
    opt_calls = tk.option_chain().calls
    opt_puts = tk.option_chain().puts
    opt = pd.concat([opt_calls, opt_puts])

    # Boolean column if the option is a CALL
    opt['CALL'] = opt['contractSymbol'].str[4:].apply(lambda x: "C" in x)

    opt[['bid', 'ask', 'strike','openInterest']] = opt[['bid', 'ask', 'strike', 'openInterest']].apply(pd.to_numeric)

    # Drop unnecessary and/or meaningless columns
    opt = opt.drop(columns = ['contractSize', 'currency', 'change', 'percentChange', 
                              'lastTradeDate', 'lastPrice', 'contractSymbol', 'bid', 'ask', 'impliedVolatility', 
                              'inTheMoney'])

    return opt

def total_loss_on_strike(chain, strike):
    callChain = chain[chain['CALL'] == True]
    callChain = callChain.dropna()       
    in_money_calls = callChain[callChain['strike'] < strike][["openInterest", "strike"]]
    in_money_calls["CLoss"] = (strike - in_money_calls['strike']) * in_money_calls["openInterest"]

    putChain = chain[chain['CALL'] != True]
    putChain = putChain.dropna()    
    
    in_money_puts = putChain[putChain['strike'] > strike][["openInterest", "strike"]]
    in_money_puts["PLoss"] = (in_money_puts['strike'] - strike) * in_money_puts["openInterest"]
    
    total_loss = in_money_calls["CLoss"].sum() + in_money_puts["PLoss"].sum()

    return total_loss

# YFinance Object of the Ticker
ticker = "GME"
tk = yf.Ticker(ticker)

# Export all Strikes
chain = options_chain(yf.Ticker(ticker))

# Create a list of the Strikes to Itterate over
strikes = chain['strike'].values.tolist()

# Remove Duplicates (eg. A Call and A Put at $10 is only used once), Arrange by Value
strikes = sorted(list(dict.fromkeys(strikes))) 

# Initialize an Array for the Losses at Each Strike
losses = []
for expiry_strike in strikes:
    losses.append([total_loss_on_strike(chain, expiry_strike)])
    # Un-comment below to audit the losses at each strike price
    #print("Losses at the expirary price of: " + str(expiry_strike) + " were: " + str(losses[-1]))

# Max pain is the minimum loss to option writers
max_pain = strikes[losses.index(min(losses))]
print(f"Max Pain: {max_pain}")
print(f"Price of {ticker}: {round(tk.history()['Close'].iloc[-1], 4)}")

#####
# Add the Values into a SQL Database at current date/time
# Either use multiple tables (ie. use maxpain.Connor, maxpain.Chives, etc.)
# or use a "personalID" number to differentiate which theory is recorded in that value
#
# CREATE TABLE maxPain.ConnorMethod (
#	personalID int,
#	date DATE,
#   maxPain FLOAT,
#   price FLOAT,
#   );
#
# After some time of regular capture, use the database to pull up graphs of the max pain of the ticker over time
#
#
#####