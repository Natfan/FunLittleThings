from flask import Flask, request, session, redirect
from twilio.twiml.messaging_response import (
        MessagingResponse,
        Message,
        Body,
        Media
)

NOT_FOUND_MESSAGE = "Sadly, we could not find your song!"

app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form['Body']

    if _is_choice_answer(query):
        return _send_selected_song(query)

    songs = list(spootify.search(query))
    if len(songs) == 1:
        return _send_single_song(songs)
    elif len(songs) > 1:
        return _send_multiple_songs(songs)
    else:
        return _send_not_found()

def _send_not_found():
    response = MessagingResponse()
    response.message(NOT_FOUND_MESSAGE)
    return str(reponse)

def _send_single_song(songs):
    response = MessagingReponse()
    song = songs[0]
    song_data = '\n'.join([song.title,
                           song.artist])
    message = Message()
    message.append(Body(song_data))
    return str(response.append(message))

def _send_multiple_songs(songs):
    titles = [song.title for song in songs]
    session['choices'] = titles
    response = MessaagingResponse()
    message = ["We found multiple songs, reply with: "]
    for i, title in enumerate(names, 1):
        message.append("%s for %s" % (i, name))
    message.append("Or start over")
    reponse.message('\n'.join(message))
    return str(message)

def _is_choice_answer(query):
    choices = session.get('choices', [])
    if query.isdigit():
        query = int(query)
        return (query-1) in range(len(choices))
    return False

def _send_selected_songs(query):
    name = session['choices'][int(query)-1]
    songs = spootify.search(query)
    return _send_single_result(employee)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8887, debug=True)
