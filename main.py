import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from flask import Flask,request, url_for, session , redirect

app = Flask(__name__)

app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
app.secret_key= 'YOUR KEY'
TOKEN_INFO = 'token_info'


@app.route('/')
def login():
    auth_url = create_spotify_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect_page():
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth.get_access_token(code)
    session[TOKEN_INFO]= token_info
    return redirect(url_for('saveDSWeekly', _external = True))


@app.route('saveDSWeekly')
def save_discover_weekly():

    try:
          token_info = get_token()
    except:
        print("user not logged in")
        return redirect('/')
    
    return("OAUth Successful!")


def get_token():
    taken_info= session.get(TOKEN_INFO , None)
    if not token_info:
        redirect(url_for('login' , external = False))

    now = int(time.time())    

    is_expired = token_info['expires_at'] - now < 60
    if(is_expired):
        create_spotify_oauth = create_spotify_oauth()
        taken_info = spotipy_oauth.refresh_access_token(token_info['refresh_token'])
    return taken_info

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "YOUR_ClIENT_ID",
        client_secret = "YOUR_CLIENT_SECRET",
        redirect_uri = url_for('redirect_page', _external = True),
        scope = 'user-library-read playlist-mofify-public-playlist-modify-private'
        )

app.run(debug=True)
