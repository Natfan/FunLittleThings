from __future__ import print_function
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json

with open('.client_id.txt', 'r' as client_idFile:
    client_id = client_idFile.read()
with open('.client_secret.txt', 'r' as client_secretFile:
    client_secret = client_secretFile.read()
with open('.username.txt', 'r' as usernameFile:
    username = usernameFile.read()
with open('.user_id.txt', 'r' as user_idFile:
    user_id = user_idFile.read()
with open('.playlist.txt', 'r' as playlistFile:
    playlist = playlistFile.read()
redirect_uri = 'http://localhost:6666/'

scope = 'playlist-modify-private user-library-read user-library-modify playlist-modify-public playlist-read-collaborative playlist-read-private'
token = util.prompt_for_user_token(client_id, scope)
sp = spotipy.Spotify(auth=token)

searched = []

debug = False;

def req():
    if token:
        util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        sp.trace = debug
        sp.trace_out = debug
        print("args: g(et), s(et), q(uit)")
        answer1 = input()
        if answer1 == 'get' or answer1 == 'g':
            print("args: u(ser), p(laylist), s(earch), q(uit)")
            answer2 = input()
            if answer2 == 'user' or answer2 == 'u':
                sp.current_user()
                with open('data/user.info', 'r+') as userinfo:
                    json.dump(sp.current_user(), userinfo, ensure_ascii=False)
            if answer2 == 'playlist' or answer2 == 'p':
                sp.user_playlist(user_id, playlist)
                with open('data/playlist.info', 'r+') as playlistinfo:
                    json.dump(sp.user_playlist(user_id, playlist), playlistinfo, ensure_ascii=False)
            if answer2 == 'search' or answer2 == 's':
                print("args: t(rack), a(lbum), b(and), q(uit)")
                answer3 = input()
                if answer3 == 'track' or answer3 == 't':
                    print("which track do you want to search for?")
                    answer4 = input()
                    result = sp.search(q='track:' + answer4, type='track')
                    items = result['tracks']['items']
                    track = items[0]
                    trackid = [ track['id'] ]
                    print('The song', track['name'], 'has the ID of', track['id'])
                    print("do you want to add this to the: p(laylist), s(earched list) or n(othing)")
                    answer5 = input()
                    if answer5 == 'playlist' or answer5 == 'p':
                        sp.user_playlist_add_tracks(user_id, playlist, trackid)
                        print("added to the playlist")
                        main()
                    if answer5 == 'searched' or answer5 == 's':
                        searched.append(trackid)
                        print("added to the recently searched list")
                        main()
                    if answer5 == 'nothing' or answer5 == 'n':
                        main()
                if answer3 == 'album' or answer3 == 'a':
                    print("which album do you want to search for?")
                    answer4 = input()
                    result = sp.search(q='album:' + answer4, type='album')
                    items = result['albums']['items']
                    album = items[0]
                    print('The album', album['name'], 'by', album['artist'], 'has the ID of', album['id'])
                    main()
                if answer3 == 'band' or answer3 == 'b':
                    print("which band/musician/artist do you want to search for?")
                    answer4 = input()
                    result = sp.search(q='artist:' + answer4, type='artist')
                    items = result['artists']['items']
                    artist = items[0]
                    print('The artist', artist['name'], 'has the ID of', artist['id'])
                    main()
                if answer3 == 'quit' or answer3 == 'q':
                    sys.exit()
            if answer2 == 'quit' or answer2 == 'q':
                sys.exit()
            else:
                main()

        if answer1 == 'set' or answer1 == 's':
            print("args: (a)dd, (r)emove, (p)osition, s(earched), q(uit)")
            answer2 = input()
            if answer2 == 'add' or answer2 == 'a':
                print("track id?")
                track_id = input()
                track_id2 = [ track_id ]
                sp.user_playlist_add_tracks(user_id, playlist, track_id2)
                with open('data/addhist.info', 'r+') as addhistinfo:
                    json.dump(sp.user_playlist_add_tracks(user_id, playlist, track_id2), userinfo, ensure_ascii=False)
                main()
            if answer2 == 'remove' or answer2 == 'r':
                print("please note that this will remove all occurences of the track!")
                print("track id?")
                track_id = input()
                track_id2 = [ track_id ]
                sp.user_playlist_remove_all_occurrences_of_tracks(user_id, playlist, track_id2)
                with open('data/remhist.info', 'r+') as remhistinfo:
                    json.dump(sp.user_playlist_remove_all_occurrences_of_tracks(user_id, playlist, track_id2), userinfo, ensure_ascii=False)
                main()
            if answer2 == 'position' or answer2 == 'p':
                print("track id?")
                track_id = input()
                track_id2 = [ track_id ]
                print("position?")
                pos = input()
                sp.user_playlist_add_tracks(user_id, playlist, track_id2, pos)
                with open('data/poshist.info', 'r+') as poshistinfo:
                    json.dump(sp.user_playlist_add_tracks(user_id, playlist, track_id2, pos), userinfo, ensure_ascii=False)
                main()
            if answer2 == 'searched' or answer2 == 's':
                if len(searched) >= 1:
                    sp.user_playlist_add_tracks(user_id, playlist, searched[0])
                    print("added", searched[0], "and removing it from the list")
                    searched.pop(0)
                    main()
                else:
                    print("the searched list is empty")
                    main()
                main()
            if answer2 == 'quit' or answer2 == 'q':
                sys.exit()
            else:
                print("reloading the program")
                main()
        if answer1 == 'quit' or answer1 == 'q':
                sys.exit()
        else:
            main()
    else:
        print("cannot find", client_id)
        sys.exit()

def main():
    #sysult.clear()
    req()

main()
