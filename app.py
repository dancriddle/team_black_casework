import os
import urllib
import urllib2

from flask import Flask, render_template, jsonify
app = Flask(__name__)


titles = [
    {
        'id':1,
        'number': 'CS72510',
        'reference': '2345678', 
        'done': False
    }
]


@app.route('/')
def index():
  return render_template('coraEmulator.html')
  
  
@app.route('/test/')
def test():
  print 'I test got clicked!'
  return render_template('error.html')
  

@app.route('/JPLquery/')
def JPLquery():
  print 'I got clicked!'
  url = "https://testrestfulapi-srallis1.c9.io/todo/api/v1.0/tasks/1"
  req = urllib2.Request(url)
  resp = urllib2.urlopen(req).read()
  print resp
  return render_template('restrictionQuery.html')
  
@app.route('/todo/api/v1.0/titles', methods=['GET'])
def get_tasks():
    return jsonify({'titles': titles})
    
@app.errorhandler(500)
def internal_error(error):
    print "Error 500"
    return render_template('error.html',error='500')

@app.errorhandler(404)
def not_found(error):
    print "Error 404"
    return render_template('error.html',error='404')

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))