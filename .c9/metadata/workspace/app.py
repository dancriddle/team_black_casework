{"changed":true,"filter":false,"title":"app.py","tooltip":"/app.py","value":"import os\nimport urllib\nimport urllib2\n\nfrom flask import Flask, render_template, jsonify\napp = Flask(__name__)\n\n\ntitles = [\n    {\n        'id':1,\n        'number': 'CS72510',\n        'reference': '2345678', \n        'done': False\n    }\n]\n\n\n@app.route('/')\ndef index():\n  return render_template('coraEmulator.html')\n  \n@app.route('/test/')\ndef test():\n  print 'I test got clicked!'\n  return render_template('error.html')\n  \n@app.route('/JPLquery/')\ndef JPLquery():\n  print 'I got clicked!'\n  url = \"https://testrestfulapi-srallis1.c9.io/todo/api/v1.0/tasks/1\"\n  req = urllib2.Request(url)\n  resp = urllib2.urlopen(req).read()\n  print resp\n  return render_template('restrictionQuery.html')\n  \n@app.route('/todo/api/v1.0/titles', methods=['GET'])\ndef get_tasks():\n    return jsonify({'titles': titles})\n    \n@app.errorhandler(500)\ndef internal_error(error):\n    print \"Error 500\"\n    return render_template('error.html',error='500')\n\n@app.errorhandler(404)\ndef not_found(error):\n    print \"Error 404\"\n    return render_template('error.html',error='404')\n\nif __name__ == '__main__':\n    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))","undoManager":{"mark":96,"position":100,"stack":[[{"group":"doc","deltas":[{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"remove","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"remove","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":26,"column":26},"end":{"row":26,"column":27},"action":"remove","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":26,"column":26},"end":{"row":26,"column":27},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":38},"end":{"row":41,"column":0},"action":"insert","lines":["",""]},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":4},"end":{"row":42,"column":0},"action":"insert","lines":["",""]},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":42,"column":0},"end":{"row":49,"column":26},"action":"insert","lines":["@app.errorhandler(500)","def internal_error(error):","","    return \"500 error\"","","@app.errorhandler(404)","def not_found(error):","    return \"404 error\",404"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":21},"end":{"row":45,"column":22},"action":"remove","lines":["\""]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":20},"end":{"row":45,"column":21},"action":"remove","lines":["r"]},{"start":{"row":45,"column":19},"end":{"row":45,"column":20},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":18},"end":{"row":45,"column":19},"action":"remove","lines":["r"]},{"start":{"row":45,"column":17},"end":{"row":45,"column":18},"action":"remove","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":16},"end":{"row":45,"column":17},"action":"remove","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":15},"end":{"row":45,"column":16},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":14},"end":{"row":45,"column":15},"action":"remove","lines":["0"]},{"start":{"row":45,"column":13},"end":{"row":45,"column":14},"action":"remove","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":12},"end":{"row":45,"column":13},"action":"remove","lines":["5"]},{"start":{"row":45,"column":11},"end":{"row":45,"column":12},"action":"remove","lines":["\""]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":10},"end":{"row":45,"column":11},"action":"remove","lines":[" "]},{"start":{"row":45,"column":9},"end":{"row":45,"column":10},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":8},"end":{"row":45,"column":9},"action":"remove","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":7},"end":{"row":45,"column":8},"action":"remove","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":6},"end":{"row":45,"column":7},"action":"remove","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":5},"end":{"row":45,"column":6},"action":"remove","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":4},"end":{"row":45,"column":5},"action":"remove","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":4},"end":{"row":45,"column":40},"action":"insert","lines":["return render_template('error.html')"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":0},"end":{"row":44,"column":1},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":1},"end":{"row":44,"column":2},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":2},"end":{"row":44,"column":3},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":3},"end":{"row":44,"column":4},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":4},"end":{"row":44,"column":5},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":6},"end":{"row":44,"column":7},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":7},"end":{"row":44,"column":8},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":["\""]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":17},"end":{"row":44,"column":18},"action":"insert","lines":["5"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":18},"end":{"row":44,"column":19},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":19},"end":{"row":44,"column":20},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"insert","lines":["\""]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"remove","lines":["k"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"remove","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":15},"end":{"row":29,"column":16},"action":"remove","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"remove","lines":["y"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"remove","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":13},"end":{"row":29,"column":22},"action":"insert","lines":["JPL query"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"remove","lines":["k"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":9},"end":{"row":30,"column":10},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"remove","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"remove","lines":["_"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"remove","lines":["y"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":4},"end":{"row":30,"column":12},"action":"insert","lines":["JPLquery"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":39},"end":{"row":45,"column":40},"action":"insert","lines":[","]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":40},"end":{"row":45,"column":41},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":41},"end":{"row":45,"column":42},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":42},"end":{"row":45,"column":43},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":43},"end":{"row":45,"column":44},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":44},"end":{"row":45,"column":45},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":45},"end":{"row":45,"column":46},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":46},"end":{"row":45,"column":47},"action":"insert","lines":["'"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":47},"end":{"row":45,"column":48},"action":"insert","lines":["5"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":48},"end":{"row":45,"column":49},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":49},"end":{"row":45,"column":50},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":50},"end":{"row":45,"column":51},"action":"insert","lines":["'"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":4},"end":{"row":49,"column":26},"action":"remove","lines":["return \"404 error\",404"]},{"start":{"row":49,"column":4},"end":{"row":49,"column":52},"action":"insert","lines":["return render_template('error.html',error='500')"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":49},"end":{"row":49,"column":50},"action":"remove","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":48},"end":{"row":49,"column":49},"action":"remove","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":47},"end":{"row":49,"column":48},"action":"remove","lines":["5"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":47},"end":{"row":49,"column":48},"action":"insert","lines":["4"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":48},"end":{"row":49,"column":49},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":49},"end":{"row":49,"column":50},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":49},"end":{"row":49,"column":50},"action":"remove","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":49},"end":{"row":49,"column":50},"action":"insert","lines":["4"]}]}],[{"group":"doc","deltas":[{"start":{"row":48,"column":21},"end":{"row":49,"column":0},"action":"insert","lines":["",""]},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":4},"end":{"row":49,"column":21},"action":"insert","lines":["print \"Error 500\""]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":19},"end":{"row":49,"column":20},"action":"remove","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":18},"end":{"row":49,"column":19},"action":"remove","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":17},"end":{"row":49,"column":18},"action":"remove","lines":["5"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":17},"end":{"row":49,"column":18},"action":"insert","lines":["4"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":18},"end":{"row":49,"column":19},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":19},"end":{"row":49,"column":20},"action":"insert","lines":["4"]}]}],[{"group":"doc","deltas":[{"start":{"row":32,"column":67},"end":{"row":32,"column":68},"action":"remove","lines":["2"]}]}],[{"group":"doc","deltas":[{"start":{"row":32,"column":67},"end":{"row":32,"column":68},"action":"insert","lines":["3"]}]}],[{"group":"doc","deltas":[{"start":{"row":32,"column":67},"end":{"row":32,"column":68},"action":"remove","lines":["3"]}]}],[{"group":"doc","deltas":[{"start":{"row":32,"column":67},"end":{"row":32,"column":68},"action":"insert","lines":["1"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":1},"end":{"row":22,"column":2},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":2},"end":{"row":22,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":26,"column":2},"end":{"row":27,"column":0},"action":"remove","lines":["",""]}]}]]},"ace":{"folds":[],"scrolltop":176,"scrollleft":0,"selection":{"start":{"row":13,"column":21},"end":{"row":13,"column":21},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":11,"state":"start","mode":"ace/mode/python"}},"timestamp":1416932072382}