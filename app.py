from flask import Flask, request
import requests
from amazon import scrape_amazon

app = Flask(__name__)


@app.route('/<website>')
def get_data(website):

    return website


@app.route('/amazon', methods=['GET', 'POST'])
def amazon():
    if request.method == 'POST':
        url = request.form.get("link")
        #data = scrape_amazon(request_data)
        result = None
        while result is None:
            try:
                # connect
                result = scrape_amazon(url)
                return result
            except:
                pass

    else:
        return "Hi"


if __name__ == '__main__':
    app.run(debug=True)
