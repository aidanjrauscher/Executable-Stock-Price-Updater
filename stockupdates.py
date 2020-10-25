import tkinter as tk
import yfinance as yf

###############################################################################

window = tk.Tk()
window.title("My Quotes")
window.configure(bg="dark slate blue")
window.geometry("400x400")
window.grid_rowconfigure(12, weight=1)
window.grid_columnconfigure(0, weight=1)

###############################################################################

frameName = tk.Label(window, text="Quotes")
frameName.grid(row = 2, column = 0, padx =8, pady=8)
frameName.configure(font = ("",24), fg="white", bg="dark slate blue")

stock1 = tk.Label(window, text="MRNA: ")
stock1.grid(row = 4,  column = 0, padx =4, pady=4)
stock1.configure(font = 12, fg="white", bg="dark slate blue")

stock2 = tk.Label(window, text="AMZN: ")
stock2.grid(row = 5,  column = 0, padx =4, pady=4)
stock2.configure(font = 12, fg="white", bg="dark slate blue")

stock3 = tk.Label(window, text="MDB: ")
stock3.grid(row = 6,  column = 0, padx =4, pady=4)
stock3.configure(font = 12, fg="white", bg="dark slate blue")

stock4 = tk.Label(window, text="NAK: ")
stock4.grid(row = 7,  column = 0, padx =4, pady=4)
stock4.configure(font = 12, fg="white", bg="dark slate blue")

userStock = tk.Entry(window)
userStock.grid(row = 10, column = 0, padx =12, pady =12)

newStock = tk.Label(window, text="No Ticker Entered")
newStock.grid(row = 11,  column = 0, padx =4, pady=4)
newStock.configure(font = 12, fg="white", bg="dark slate blue")

###############################################################################

def getMyQuotes():
    tickers = ["MRNA", "AMZN", "MDB", "NAK"]
    labels = [stock1, stock2, stock3, stock4]
    for i in tickers:
        ticker = yf.Ticker(i)
        tickerHistory = ticker.history()
        lastQuote = (tickerHistory.tail(1)['Close'].iloc[0])

        if (float(lastQuote) > 5.0):
            lastQuote = round(lastQuote, 3)
        else: 
            lastQuote = round(lastQuote, 4)
        labelText = i + ": " + str(lastQuote)
        labels[tickers.index(i)].config(text=labelText)
    return 
 
###############################################################################
        
def lookupQuote():
        userTicker = userStock.get()
        newTicker = (str(userTicker)).upper()
        tickerLookup = yf.Ticker(newTicker)
        try: 
            tickerHistory = tickerLookup.history()
            lastQuote = (tickerHistory.tail(1)['Close'].iloc[0])
        except IndexError: 
            tickerLookup = None
        
        if tickerLookup is None:
            newStock.config(text="Not a Valid Ticker")
            return
        else:
            tickerHistory = tickerLookup.history()
            lastQuote = (tickerHistory.tail(1)['Close'].iloc[0])
            if (float(lastQuote) > 5.0):
                lastQuote = round(lastQuote, 3)
            else: 
                lastQuote = round(lastQuote, 4)
            newlabelText = newTicker + ": " + str(lastQuote)
            newStock.config(text=newlabelText)
            return 
            
###############################################################################               
              
updateButton = tk.Button( text = "Updates Quotes", 
                      fg = "white", bg = "black", 
                      command = getMyQuotes)
updateButton.grid(row=8, column = 0, padx=12, pady =12)

searchButton = tk.Button( text = "Lookup Stock", 
                      fg = "white", bg = "black", 
                      command = lookupQuote)
searchButton.grid(row=12, column = 0, padx=12, pady =12)

###############################################################################

window.mainloop()
