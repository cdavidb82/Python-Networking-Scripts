# HTTP Services written in Python


import urllib.request
import pprint
import csv

pp = pprint.PrettyPrinter(indent=4)

goog_url = 'http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv'

def download(csv_url):
    try:
        with urllib.request.urlopen(csv_url) as response:
            reader = csv.reader(response)
            for row in reader:
                pp.pprint(row)
    except urllib.error.URLError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    download(goog_url)
