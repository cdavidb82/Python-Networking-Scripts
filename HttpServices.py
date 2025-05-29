# HTTP Services written in Python

import urllib.request
import pprint
import csv

pp = pprint.PrettyPrinter(indent=4)

class CsvReader:

    def __init__(self, csv_url):
        self.csv_url = csv_url


    def download(self):
        try:
            with urllib.request.urlopen(self.csv_url) as response:
                lines = [l.decode('utf-8') for l in response.readlines()]
                reader = csv.DictReader(lines)
                for row in reader:
                    pp.pprint(dict(row))
        except urllib.error.URLError as e:
            print(f"Error: {e}")
        except csv.Error as e:
            print(f"CSV Error: {e}")

            
if __name__ == "__main__":
    reader = CsvReader("https://google.com")
    reader.download()
