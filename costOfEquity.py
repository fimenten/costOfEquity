import datetime,argparse
import pandas as pd
import pandas_datareader.stooq 
import yfinance

RF_url = "https://www.mof.go.jp/jgbs/reference/interest_rate/jgbcm.csv"
TOPIX_ticker = '^TPX'


def get_topix(days = 365):
    start =  datetime.datetime.now() - datetime.timedelta(days = days)
    end = datetime.datetime.now()
    df = pandas_datareader.stooq.StooqDailyReader(TOPIX_ticker,start,end).read()
    return ((df["Close"] - df["Close"].shift())/df["Close"].shift()).fillna(0)
def _get_ticker_df(ticker,days = 365):
    start =  datetime.datetime.now() - datetime.timedelta(days = days)
    end = datetime.datetime.now()
    df = yfinance.download(tickers=[ticker],start = start,progress=False)
    return ((df["Adj Close"] - df["Adj Close"].shift())/df["Adj Close"].shift()).fillna(0)

def get_ticker_df(ticker,days = 365):
    # start =  datetime.datetime.now() - datetime.timedelta(days = days)
    # end = datetime.datetime.now()
    # df = yfinance.download(tickers=[ticker],start = start,progress=False)
    ticker = yfinance.Ticker(ticker)
    ret = ticker.history("1y",back_adjust=True,)
    ret = ret.set_index(ret.index.values)
    return ((ret["Close"] - ret["Close"].shift())/ret["Close"].shift()).fillna(0)



def get_rate():
    df  = pd.read_csv(RF_url,encoding="Shift-JIS",header=1)
    # print(df)
    return df["10年"].iloc[-1]



"pip install pandas pandas-datareader yfinance"




def main():
    parser = argparse.ArgumentParser(description='calc cost_of_equity')

    parser.add_argument('ticker', type=str, help='the ticker symbol for the stock eg.. 4563.T')
    parser.add_argument('premium', type=float, help='the premium for the stock, percent')

    parser.add_argument('--yfinance', action='store_true',default=True, help='whether use the yfinance library to retrieve data')
    parser.add_argument('--beta', type=float, help='Specify if not yfinance. the beta value for the stock')
    parser.add_argument('--riskFreeRate', type=float, help='Specify if not yfinance the risk-free rate for the stock, percent')
    parser.add_argument('--freq', type=str, default="W",help='pandas format.freq to calc beta')
    parser.add_argument('--period', type=int, default=365,help='days to calc beta')
    

    args = parser.parse_args()

    # print(f'Ticker symbol: {args.ticker}')
    if args.yfinance:
        df_TOPIX = get_topix(days=args.period).resample(args.freq).sum()
        df_ticker = get_ticker_df(days=args.period,ticker=args.ticker).resample(args.freq).sum()
        df = pd.concat([df_TOPIX,df_ticker],axis=1).fillna(method="ffill")
        # print(df.cov())
        var,cov = list(df.cov().iloc[0])
        beta = cov/var

    else:
        beta = args.beta
    
    if args.riskFreeRate:    
        risk_free_rate = args.riskFreeRate
    else:
        risk_free_rate = get_rate()
        
    cost_of_equity = float(risk_free_rate) + float(beta) *  float(args.premium)
    
    print(cost_of_equity)
    
    
if __name__ =="__main__":
    main()