import pandas as pd
from os import system
from os import path as os_path
import tkinter as tk
system("clear")

if os_path.isfile('./supermarkets/supermarkets.csv'):
    bf1 = pd.read_csv('./supermarkets/supermarkets.csv')
    print(bf1)

w1 = tk.Canvas()
w1.mainloop()
