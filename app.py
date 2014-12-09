import os
import urllib
import urllib2
from letter import generate_letter
import json

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
app.config.from_object('config')


titles = [
    {
        'reference': 1234567,
        'titleNumber': 'CS99999',
        'complete': False
    },
    {
        'reference': 2345678,
        'titleNumber': 'CS72510',
        'complete': False
    },
    {
        'reference': 3456789,
        'titleNumber': 'CS88888',
        'complete': False
    }
    
]

@app.route('/')
def index():
    #This is a poor way of doing this, but will have to do for the demo.
    titlenumber = titles[0]['titleNumber']
    titlenumber1 = titles[1]['titleNumber']
    titlenumber2 = titles[2]['titleNumber']
    complete = titles[0]['complete']
    complete1 = titles[1]['complete']
    complete2 = titles[2]['complete']
    
    return render_template('index.html',  titlenumber=titlenumber, complete=complete,titlenumber1=titlenumber1, 
                            complete1=complete1,titlenumber2=titlenumber2, complete2=complete2) 
  

@app.route('/restriction/<int:index>', methods=['GET'])
def restriction(index):
    titlenumber=titles[index]['titleNumber']
    return render_template('coraEmulator.html',titlenumber=titlenumber,index=index)
    
@app.route('/JPLquery/<int:index>', methods=['GET'])
def JPLquery(index):

  url = '%s/sendmail' % app.config['EMAIL_SERVICE']

  app.logger.info(url)

  # These two lines to set status of title to 'In Progress'
  titles[index]['complete'] = 'In Progress'
  #jsonify({'title': title[index]})

  # Construct and send email
  title_number = titles[index]['titleNumber']
  reference_number = str(titles[index]['reference'])

  convenyancer_name = 'Michael Foord'
  convenyancer_email = 'JPLService00@gmail.com'
  message_subject = 'You have a Joint Proprietor notification'
  message_content = generate_letter(reference_number, convenyancer_name, title_number)


  values = {'name'   : convenyancer_name,
            'email'  : convenyancer_email,
            'subject': message_subject,
            'body'   : message_content }
            
  print values

  data = urllib.urlencode(values)
  
  req = urllib2.urlopen(url, data)
  #resp = urllib2.urlopen(req).read()
  #print resp
  return render_template('restrictionQuery.html')

    
@app.route('/test/')
def test():
  print 'I test got clicked!'
  return render_template('error.html')
  
  
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
    

    
@app.route('/complete', methods=['POST'])
def update_title():
    print 'got here from complete'
    title = filter(lambda t: t['reference'] == int(request.json.get('reference')), titles)
    if len(title) == 0:
        abort(404)
        
    if not request.json:
        abort(400)

    title[0]['titleNumber'] = request.json.get('titleNumber', title[0]['titleNumber'])
    title[0]['complete'] = True
    jsonify({'title': title[0]})
    print title
    return "True"
    
@app.errorhandler(500)
def internal_error(error):
    print "Error 500"
    return render_template('error.html',error='500')

@app.errorhandler(404)
def not_found(error):
    print "Error 404"
    return render_template('error.html',error='404')
    

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 5010)))
