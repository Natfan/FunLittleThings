import spotipy
import argparse

sp = spotipy.Spotify()
parser = argparse.ArgumentParser()
parser.add_argument("term", help="The artist that you want to search for")
parser.add_argument("-c", "--count", help="The amount of results that you want, capped at 20", type=int)
args = parser.parse_args()

def spoprint():
    results = sp.search(q=args.term, limit=args.count)
    for i, t in enumerate(results['tracks']['items']):
        print(' ', i, t['name'])

if args.count:
    if args.count > 20:
        print("enter a count lower than or equal to 20")
    else:
        spoprint()
else:
    spoprint()
