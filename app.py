import os
import urllib
import urllib2

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


titles = [
    {
        'reference': 2345678,
        'titleNumber': 'CS72510',
        'complete': False
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
 # url = "https://testrestfulapi-srallis1.c9.io/todo/api/v1.0/tasks/1"
  url= "https://team-black-email-service-dancriddle.c9.io/sendmail"
  
  values = {'name'   : 'Michael Foord',
            'email'  : 'JPLService00@gmail.com',
            'subject': 'JPL Query',
            'body'   : 'Main email text goes here' }

  data = urllib.urlencode(values)
  
  req = urllib2.urlopen(url, data)
  #resp = urllib2.urlopen(req).read()
  #print resp
  return render_template('restrictionQuery.html')
  
@app.route('/titlefromreference', methods=['POST'])
def title_from_reference():
    
    print "Got here form referance"
    
    title = filter(lambda t: t['reference'] == int(request.json.get('reference')), titles)
    if not request.json or not 'reference' in request.json:
        abort(400)
        
    if (len(title) == 0):
        data = "Referance not valid"
    else:
        data = title[0]['titleNumber']

    return data
  
@app.route('/complete/<int:reference_id>', methods=['PUT'])
def update_title(reference_id):
    print reference_id
    title = filter(lambda t: t['reference'] == reference_id, titles)
    if len(title) == 0:
        abort(404)
        
    if not request.json:
        abort(400)

    title[0]['titleNumber'] = request.json.get('titleNumber', title[0]['titleNumber'])
    title[0]['complete'] = request.json.get('complete', title[0]['complete'])

    return jsonify({'title': title[0]})
    
    
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