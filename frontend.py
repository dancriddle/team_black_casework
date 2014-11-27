__author__ = 'paultrelease'

from flask import Flask, render_template, request, logging, abort
import os
app = Flask(__name__)

TITLE_NUMBER = "TN1"

@app.route('/')
def index():
    return render_template("index.html", title_number=TITLE_NUMBER)

@app.route('/addrestriction')
def add_restriction():
    referencenumber = 1234
    #When this is done properly, a call to another microservice will take place
    #to send an e-mail to the client
    return render_template("restriction_added.html", referencenumber=referencenumber, title_number=TITLE_NUMBER)

@app.route('/titlefromreference', methods=['POST'])
def title_from_reference():
    if not request.json or not 'reference' in request.json:
        abort(400)
    app.logger.debug('reference is %s' % request.json['reference'])
    return TITLE_NUMBER


if __name__ == '__main__':
    app.run(debug=True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 5010)))
