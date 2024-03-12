#import requests;

# coin_id = 'bitcoin';
# currency = 'usd';

# url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}'

# data = requests.get(url).json()

# coin_price = data[coin_id][currency]

# print(coin_price)

##########

#This code initializes a SQLite database named 'portfolio.db'.
#This code sets up a table named 'investments' with columns for coin ID, currency, amount, sale status, and date, ensuring the table exists if it hasn't been created yet.

#creating a command line application

import sqlite3
import datetime
import csv
from dataclasses import dataclass

import requests
import click

database = sqlite3.connect('portfolio.db');
cursor = database.cursor()

CREATE_INVESTMENTS_SQL = """
CREATE TABLE IF NOT EXISTS investments (
    coin_id TEXT,
    currency TEXT,
    amount REAL,
    sell INT, 
    date TIMESTAMP
);
"""

######################

#This code defines a command-line interface using the click library for managing cryptocurrency investments. 
#It includes commands to display the current price of a specified cryptocurrency, as well as to add a new investment record with details like coin ID, currency, amount, and whether it's a sale or purchase. 
#The show_coin_price command retrieves and prints the current price of a specified cryptocurrency.
#The add_investment command inserts a new investment record into a SQLite database, with an option to specify a sale.


def get_coin_price(coin_id, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    data = requests.get(url).json()
    coin_price = data[coin_id][currency]
    return coin_price

@click.group()
def cli():
    pass

@click.command()
@click.option("--coin_id", default="bitcoin")
@click.option("--currency", default="usd")
def show_coin_price(coin_id, currency):
    coin_price = get_coin_price(coin_id, currency)
    print(f"The price of {coin_id} is {coin_price:.2f} {currency.upper()}")

@click.command()
@click.option("--coin_id")
@click.option("--currency")
@click.option("--amount", type=float)
@click.option("--sell", is_flag=True)
def add_investment(coin_id, currency, amount, sell):
    sql = "INSERT INTO investments VALUES (?, ?, ?, ?, ?);"
    values = (coin_id, currency, amount, sell, datetime.datetime.now())
    cursor.execute(sql, values)
    database.commit()

    if sell:
        print(f"Added sell of {amount} {coin_id}")
    else:
        print(f"Added buy of {amount} {coin_id}")

#####################

#This code extends a command-line interface built with click, introducing commands to calculate the total value of investments in a specified cryptocurrency 
#Also imports investment data from a CSV file into a SQLite database. 
#It integrates these new functionalities into the existing CLI alongside commands for displaying coin prices and adding new investments, utilizing a SQLite database for data storage.

@click.command()
@click.option("--coin_id")
@click.option("--currency")
def get_investment_value(coin_id, currency):
    coin_price = get_coin_price(coin_id, currency)
    sql = """SELECT amount
    FROM investments
    WHERE coin_id=?
    AND currency=?
    AND sell=?;"""
    buy_result = cursor.execute(sql, (coin_id, currency, False)).fetchall()
    sell_result = cursor.execute(sql, (coin_id, currency, True)).fetchall()
    buy_amount = sum([row[0] for row in buy_result])
    sell_amount = sum([row[0] for row in sell_result])

    total = buy_amount - sell_amount

    print(f"You own a total of {total} {coin_id} worth {total * coin_price} {currency.upper()}")

@click.command()
@click.option("--csv_file")
def import_investments(csv_file):
    with open(csv_file, "r") as f:
        rdr = csv.reader(f, delimiter=",")
        rows = list(rdr)
        sql = "INSERT INTO investments VALUES (?, ?, ?, ?, ?);"
        cursor.executemany(sql, rows)
        database.commit()

        print(f"Imported {len(rows)} investments from {csv_file}")

cli.add_command(show_coin_price)
cli.add_command(add_investment)
cli.add_command(get_investment_value)
cli.add_command(import_investments)

if __name__ == "__main__":
    database = sqlite3.connect("portfolio.db")
    cursor = database.cursor()
    cursor.execute(CREATE_INVESTMENTS_SQL)
    cli()
