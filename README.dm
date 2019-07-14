Script save result of request from Homeaway. Available Query: owner, images, price(don`t work yet).
Results will save to json format.

The script runs through manage.py

                                                    Console Commands

To indicate the ID of hotel/house

    -You can manually enter ID:
        manage.py --id id1 id2 id3 ...
    - You can specify the ID through the csv file:
        manage.py -csv
    -You can combine these two options:
        manage.py -csv --id id1 id2 id3 ...

To specify which request you want:
    Query of owners:
        -owners
    Query of image:
        -image
    Query of price:
        -price
    All Available Query:
        -all

To set csv file path(default: input/input.csv):
    --csv_path input/input.csv

To set the path to save the result(default: results/owners.json):
    --result_path results/owners.json

To set semaphore(default: 100):
    --sem 100
