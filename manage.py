import argparse
import asyncio

from information_processing import load_data
from homeaway_requests import create_requests

parser = argparse.ArgumentParser(description='Help')
parser.add_argument('--id', type=str, nargs='+')
parser.add_argument('-csv', action='store_true')
parser.add_argument('--csv_path', type=str, default='input/input.csv')
parser.add_argument('--result_path', type=str, default='results/owners.json')
parser.add_argument('--sem', type=int, default=100)

args = parser.parse_args()

data = []

if args.id:
    data += args.id

if args.csv:
    data += load_data(args.csv_path)

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(create_requests(data, args.result_path, args.sem))
loop.run_until_complete(future)
