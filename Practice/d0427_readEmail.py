import sys
from collections import Counter
import csv

#EmailCount

def get_domain(email_address):
    """split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]

with open('data/email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
    for line in f
    if "@" in line)
    print(domain_counts)


#Delimited Files

def process(*args):
    print('c={}, d={}'.format(len(args),args))

with open('data/tab_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)

with open('data/colon_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        process(date, symbol, closing_price)

today_prices = {'Chinese': 90.91, 'English': 41.68, 'Math': 64.5 }
with open('data/score.txt','wb') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])