import requests
from flask import Flask, render_template

app = Flask(__name__)

# Fetching a random quote from ZenQuotes API and GIF from Giphy
def get_random_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    quote_data = response.json()
    quote = quote_data[0]['q']
    author = quote_data[0]['a']

    #The following grabs gif urls that are trending

    return quote, author

@app.route('/')
def index():
    quote, author = get_random_quote()
    return render_template('index.html', quote=quote, author=author)

if __name__ == "__main__":
    app.run(debug=True)
