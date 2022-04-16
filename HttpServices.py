import urllib
import urllib.request
import pprint

pp = pprint.PrettyPrinter(indent=4)

goog_url = 'http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv'


def download(csv_url):
    response = urllib.request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    for l in lines:
        pp.pprint(l + "\n")


if __name__ == '__main__':
    download(goog_url)
