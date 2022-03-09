from tkinter import *
from tkinter import ttk
from datetime import date

import bs4
import requests


def start_scrapping():
    base_url = "https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut"

    result = requests.get(base_url)

    soup = bs4.BeautifulSoup(result.text, "lxml")

    currency_rate = soup.find('td', string='GBP / KZT')
    value.set(currency_rate.find_next_sibling().string)

root = Tk()
root.title("Currency rates")

mainframe = ttk.Frame(root)
mainframe.grid(column =0, row= 0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

value = StringVar()
ttk.Label(mainframe, textvariable=value).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Расчет", command=start_scrapping).grid(column=2, row=1, sticky=W)

ttk.Label(mainframe, text="Валюта").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="GBP/KZT").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Дата").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text=f"{date.today()}").grid(column=2, row=3, sticky=W)


root.mainloop()