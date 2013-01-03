import os
import requests
import flask

app = flask.Flask(__name__)

client = {
	'client_id'      : '', 
	'client_secret'  : '',
	'grant_type'     : 'authorization_code', 
	'redirect_uri'   : ''
}

@app.route('/')
def root():
	uri = 'https://api.instagram.com/oauth/authorize/?client_id={0}&redirect_uri={1}&response_type=code'.format(client['client_id'], client['redirect_uri'])
	return flask.redirect(uri)
	
@app.route('/auth')
def auth():
	client.update({'code': flask.request.args.get('code')})
	return flask.Response(requests.post('https://api.instagram.com/oauth/access_token/', data=client).text, status=200, mimetype='application/json')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
