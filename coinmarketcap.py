#!/usr/bin/python3

from pymongo import MongoClient
import requests
import datetime
import os


if __name__ == '__main__':
    # MLab credentials
    user = os.getenv('MLABUSER')
    password = os.getenv('MLABPASS')

    # Connect to MLab Mongo Instance
    uri = 'mongodb://' + user + ':' + password + '@ds241885-a0.mlab.com:41885/coinmarketcap'
    client = MongoClient(uri)
    db = client.get_default_database()
    col = db['coinmarketcap']

    # Request from Coinmarket Cap the top 100 coin data
    req = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=100')
    coin_data = req.json()

    # Update each coin with API request time
    call_time = datetime.datetime.now().isoformat()
    for coin in coin_data:
        coin['time'] = call_time

    # Insert data into 'coinmarketcap' collection
    col.insert_many(coin_data)

    # Close the connection
    client.close()



