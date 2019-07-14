import argparse

import asyncio

from information_processing import load_data
from homeaway_requests import create_requests

parser = argparse.ArgumentParser(description='Help')
parser.add_argument('--id', type=str, nargs='+')
parser.add_argument('-csv', action='store_true')
parser.add_argument('-owner', action='store_true')
parser.add_argument('-images', action='store_true')
parser.add_argument('-price', action='store_true')
parser.add_argument('-all', action='store_true')
parser.add_argument('--csv_path', type=str, default='input/input.csv')
parser.add_argument('--result_path', type=str, default='results/owners.json')
parser.add_argument('--sem', type=int, default=100)

args = parser.parse_args()

query_type = {'owner': args.owner or args.all,
              'images': args.images or args.all,
              'price': args.price or args.all}
data = []

if args.csv:
    data = load_data(args.csv_path)

if args.id:
    data.extend(args.id)

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(create_requests(data, query_type,  args.result_path, args.sem))
loop.run_until_complete(future)
