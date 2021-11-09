import json
import requests
import argparse


def itunes(arg):
    r = requests.get(f'https://itunes.apple.com/lookup?id={arg}').json()
    link = r['results'][0]['artworkUrl100']
    with open(f'cover {arg}.jpg', 'wb') as f:
        f.write(requests.get(link.replace('100x100bb.jpg', '10000x10000-999.jpg')).content)


def deezer(arg):
    r = requests.get(f'https://api.deezer.com/album/{arg}').json()
    link = r["cover_xl"]
    with open(f'cover {arg}.jpg', 'wb') as f:
        f.write(requests.get(link.replace('1000x1000-000000-80-0-0.jpg', '1900x1900-000000-100-0-0.jpg')).content)


def main():
    parser = argparse.ArgumentParser(description='Program to download album covers from iTunes and Deezer')
    parser.add_argument('id', metavar='id', nargs='+', help='The album ID or IDs')
    parser.add_argument('-i', '--itunes', help='Download cover from Itunes (default)', action='store_false')
    parser.add_argument('-d', '--deezer', help='Download cover from Deezer', action='store_true')
    args = parser.parse_args()

    for arg in args.id:
        if args.deezer:
            deezer(arg)
        else:
            itunes(arg)


if __name__ == '__main__':
    main()
