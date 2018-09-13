# -*- coding: utf-8 -*-

"""

██████╗ ██╗   ██╗███████╗████████╗    ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗     ███╗   ███╗██████╗    ██████╗  ██████╗
██╔══██╗██║   ██║██╔════╝╚══██╔══╝    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ████╗ ████║██╔══██╗   ██╔══██╗██╔════╝
██████╔╝██║   ██║███████╗   ██║       ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝    ██╔████╔██║██████╔╝   ██║  ██║██║     
██╔══██╗██║   ██║╚════██║   ██║       ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗    ██║╚██╔╝██║██╔══██╗   ██║  ██║██║     
██║  ██║╚██████╔╝███████║   ██║       ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║    ██║ ╚═╝ ██║██║  ██║██╗██████╔╝╚██████╗
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝                                                                                                                                
--.....------:ohdhhysooooosyyysoosyhhhyyyhhhddddddyoshdmmmmmmmmmmmmddhyy+/////::++/////osoooooosssoo
......-----:oyyyso++oosssyyyyyssssyhhhhhddddmmmmmmddhdmmmmmmmdddddddddyy++ooo++syso///::////++o+++++
.-------:+yhysssssssyyyyyyyyyysyhhhhddmmmmmmmmmmmmmmmmmmmmmmddddddddddhdhddhsoyhhyyso+/:::::/+//++++
-----/+yhyyysssyyyyyyyyyyyyyyyhhddddmmmmmmmmmmmmmmmmmmmmmmmmmmmmddddmmmmmmmmmmmdddhyso+/:::::///////
-/+ossssoosyyssyhhhhhyyyyyyyyhddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNmmmmddhsso+/:--/::////
yysooooossyyysyyyhhhyyysyyyyhddmmmmmmmmmmmdmmmmmmmmmmmdddddmddddmmmmmmmmmmmmmmmmmmmmmmdhyso+:-:::://
yyyyhysssyyyysyssssssssssssyhhdddddhhhhddddddmmmmmmmdhhhdddhyssyyhhmdddmmmNNmmmmmmmNNNNmdhyso+:-::::
hhhyysoosyyyyyso++ooosssyyyyyyyyyyyyhhhhhhhhhddddhhdhhysyyyysssssyoydhhdmmmmmmmmmmmmmmNNmmdhyso/::::
hysoosyhhyyyyysssssoo+++/+++/+/++oooosssyyhhhysssysssosso/oyysooooo++syhhdmmmmmmmmmmmmmmmmmmhyss+:::
yyyyhhyyyyhhyyyso+/:::::::::/++osssssssossso+/::::::::::///o+ooooooosysyyhhddmmmmmmNmmmmmmmNmdhyyo++
yhhhhyyyyhhhhhhhyyyo//:++/+osysso++/////:::----:------------:::::////+++oososydddmNmmmmmmmmmmmdhysss
hhys++oshhhhhhhhhhy/:::++oooso+///:///:-....----......`````..----:--:::+/+o++/ohddmmmmmmmmmmmmddddhh
ys++//+yhhyyyyyyyyo:::/oso++/:://://:.....----....`````````......-----////oo++/+ydmmmmmmmmmmmmdhdddd
o+++++syyysoooo+os/::/ooo+/:-:/:::-.....----....``````````.......---.-/::/++o++:/yydmmmmdmdddddhdddd
+++++oyyyyo/////o/-:+ss//:--:/::-..............```````````...........---::+//+//:/yhdmmmmmmmdddyhddd
oo++osyyysoo+///o++oyy//::-:::--..............````````````............---:+++////:+yhdmmmmmmmmdyshdd
yyyyhhhhyyso++/++yyyh+//://::::----...........```````````.............---:+/+/:////shhddmmmmmmdyoyhh
hhhhhhhhyysooo+oosyyo////+///////::--:-:::::----...```................---:///////+//yhddddddddds+oss
dddhhyso++//////+oys//://::////++++////:-------....```................----:///+//++:/shhhyhhhhhs/os+
hhhyysooo++++///+yy+//::---.....--------.--........```.................----:::/:/:/:::oooosssyys+oo/
yyyyso+ooooo+++oshy+/++o+/:--.....-------.............-..`````........---:::::/:::::--:++::://///+//
yssso+::////+sooyysoyddddyo+/--.........-..--:///:::--:-:-.````.....----:://://::::::--:+/:/:::::///
ysooo+:::://+h+::/shhhhhhdddhs+::......--/osyhhddhyo+/----:::--.....--::///:////:::-:::://:/::://+//
sso++/:::::/soyyyyy++++o++ossyyo:-.....-/osyssssosooo+/:::::/++/-..----:::/:///+::/:-::::////+/:+++/
ooo+/::::::+y:-::+o++++o+o+++++os+----:/+++++++++o++//:::--::+o+--------::::://+/://-::::///+o+::///
+/::::::::++oo+++o+oossysso+++++oso/::/++/+//++++ooooo++/::--:/+:-------:-:::/+o//+/---/++ssyys///::
--------:/+++ooso++sdmmmmddhsoo++so:--/o++++++shdmmmmddhyso+::://:------:-::::+so//+//:++/////sso+//
--------:+o+ssss//yyyyyyysyhdyo+oo-..../oo++oyhdhhyysssyhhhhyo+++//-------::::/ss++///:--:/+o:-+yo//
--------:+o+syy+/os++++++//++ooos:....../osos++//////////+++++//:------------:/oso++:--/+o++os--+o//
/:////:::+o+shy+/ooosssssoo+++oo:........-/ossyhyyyyyyssso/::----------------::+o+/:-:/+oo+/+s:-/+/:
///+++////+oshs/+ooooosooo++::/-...........--/+ssso++++++++oo+//:-------------::++:::++/://--o:-:+::
//+++++///++yy+:-::///:::::--:-......-.......:++oooooosooo+//+++/:-------------:+:://sso///--+..//::
+////++////+ys--...........-:-...`...--.---...--::::::----....-----------------//://ossso+:---.:+:::
+/::://///:+y+-...........---...```.-....--::-.....````````......----.-..--::::/:::/++++o:---.-+/:::
++::::///:-+o:..............-...``.........-::-.....```````````.....-.---://////:::+o+//:---.-+/:/::
++::::::::-+o---.-.----:-.:/---.......````....:/--.................--:::////:/:/::+/---:::--/o/::/::
++::::::::-++--:-----:+ssosysssooo+/:--..----:+so:----........---://++/:::::::::/+/-:/::::+sys//:/::
++/////::::++--/:////oo++oosyssssyyhhyyssssso//ss+/::::::://////++ooo/::::::::://:..---:+shhhy/////:
++++///::::+o::/:/://+++++++sssssoosooooo+++---/so////////////////ss+::::::::://....-:/oo+yhhy/////:
yyyyyyss++/os/:/:///+/++++/+/+++++++++++++/-.---oo//////++/////:::++::::::::::o:----/oo+//+yhh+////:
yyyyyhyyso+sy/:/::/++++++++++++ooo++++++:-...---+o/////:/+/++/::://::::::/:::/s/+yyso++/////oys///::
hhhhhhhhysoyho/////o+++++ooo+++++ooo++:--....---+o/////://////:://:::::///:::o/:+hhyhsoo+/////+o+/::
hhhhhhhhyyshdh///:/oo++shdsoshysyyyyhyyyso++++//os+/////:///////+/::::::::::+o::+dhhddhyso++++//oo:/
oooosshhyyyhddy////+ooosydhoyy++++/++ooooooosyyyhhy+////::::///:/::////:::::o/::+hhoydmmdhso+/+////:
sssssyhhhhyyhmmy////+++ooosyhhyyyysyyhhyyyyyyssososo++////:////:///////:::::+-::/yh++shddmdyso+////:
yyyhyhddddhddmmmy///+o++//++++oosysoooo+++/////+ssss+++////:////:///::://:-/:-:-/yyo/+sshmmmdyo+/:/:
yhhddddddddmmmmmmh///oo++/////++ooooooossoo+//::/ssysso////::::::/:::://--//----:syo//++ohmmmmhs++//
--:+ssyyyhdddmmmmmh+//+++////////++++++//+//::::/+++/++/////:::::::://:--:/-----:ooo//+++ohmmmmmho++
--/yhooso+oooosssyyho://++////////////////////::---:/+/:::::::::::::/:--:+:---:-:o/++/++/+shdmmmmdss
-:+yyoossssssssoooosho///++++++//+++++o++/:::---::/++/::::::::::////:---++:::::-:+/+//////oydddddmmd
::+sss+oooyssssssoooyy////++++osssso+/:--:---::::/+/::::::::/:::///:---/o::::::-:o:/+:////+yhhhhdddd
-:osss++oosssssooo++ys////////++//::::::::::://++///::::://///////:::-:o+-:::::-:+/://:////shhhhhhhd
.+oosso+oosssso+++/+yo///:////+++++++++oosssso//:::::://///+/////::::-+o:::::::-/o/:///////+yhhhhhyy
/++oosooossssoo+//+ss/////////+osssysssooo++////:::://////////::/:::-:so::::::::/o+:////////yhhhhyss
++oosooooossso+++oo++:///++ooo+++++++++++o++oo/////////::::///:::::--+s++://///:/s+/++/+/::/yhhhyso/
ooosssssoooso++oo:://::://////+///++oo++/////:::::::::/:::///:::----:s+++/:////:/yo+++//////syho++::
oooooooooooo+o+/-::/::::////////////:::::::::::::::::://:/:/::::---:ss+++///+ssoos+++o//+/:+ss++/://
hhhyyssoosoo+/::///::::::::////////////::::::::::::::::/:::::::::::syo+++++ymNNmmmmdhhsss//ooo::::/+
mddhhhyyso+//:/++/::/::::::::://///////:::::::::::::::::::::::::::+dd++osyhmmddddddmmdhs+s//so/:::oy
Nmmdhso++////++///::::::::::::::///:::::::::::://////::::::::-:://yddddmmmmddmmmmmmmmdy+oo+//ossssyy
ys++//+++++//+/////:::::::::::::://::::::::::::::::::::::::::::://dmmddmmmmmmmmmmmmmddy++++//////+//
"""

from flask import Flask, request, abort, Response, render_template
import json

app = Flask(__name__)
config = [
  {
    'path': '/dc1',
    'type': 'auth',
    'auth': {
      'type': 'basic_auth',
      'username': 'admin',
      'password': '123456'
    },
    'next': ['/dc1/dc']
  },
  {
    'path': '/dc2',
    'type': 'auth',
    'auth': {
      'type': 'form_auth',
      'username': 'admin',
      'password': '123456'
    },
    'next': ['/dc2/dc']
  },
  {
    'path': '/dc3',
    'type': 'auth',
    'auth': {
      'type': 'cookie_auth',
      'username': 'admin',
      'password': '123456'
    },
    'next': ['/dc3/dc']
  },
  {
    'path': '/dc1/dc',
    'type': 'xss'
  },
  {
    'path': '/dc2/dc',
    'type': 'xss'
  },
  {
    'path': '/dc3/dc',
    'type': 'xss'
  }
]
_routes = {}

@app.route('/<path:url>', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def route(url=''):
  print(url)
  url = '/{}'.format(url)
  if url == 'api/set_config':
    return set_config()
  elif request.path == '/':
    urls = [i['path'] for i in config if i['type'] == 'auth']
    return render_template('next.html', urls=urls)
  else:
    handler = _routes.get(url, None)
    if handler:
      return handler()
  abort(404)

def set_config():
  if request.method == 'POST':
    try:
      global config
      config = json.loads(request.args.get('config', json.dumps(config)))
      global _routes
      _routes = {}
      add_route_from_config(config)
    except:
      abort(403)
    return 'Rust master DC No.1!'

def make_basic_auth_view(username='', password='', next=['/']):
  def _():
    auth = request.authorization
    if not auth or auth.username != username or auth.password != password:
      return Response('Please Login', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    else:
      return render_template('next.html', urls=next)
  return _

def make_form_auth_view(username='', password='', next=['/'], action='/'):
  def _():
    if request.method == 'GET':
      return render_template('form_auth.html', action=action)
    elif request.method == 'POST':
      if username == request.form.get('username', '') and password == request.form.get('password', ''):
        return render_template('next.html', urls=next)
      else:
        return render_template('form_auth.html', action=action)
  return _

def make_cookie_auth_view(username='', password='', next=['/']):
  def _():
    if username == request.cookies.get('username', '') and password == request.cookies.get('password', ''):
      return render_template('next.html', urls=next)
    else:
      return Response('Please Login', 401)
  return _

def add_route_from_config(config_item_list: list):
  for item in config_item_list:
    if item['type'] == 'auth':
      if item['auth']['type'] == 'basic_auth':
        _routes[item['path']] = make_basic_auth_view(item['auth']['username'], item['auth']['password'], item['next'])
      elif item['auth']['type'] == 'form_auth':
        _routes[item['path']] = make_form_auth_view(item['auth']['username'], item['auth']['password'], item['next'], item['path'])
      elif item['auth']['type'] == 'cookie_auth':
        _routes[item['path']] = make_cookie_auth_view(item['auth']['username'], item['auth']['password'], item['next'])
    elif item['type'] == 'xss':
      def _():
        if request.method == 'GET':
          return render_template('xss.html', action=item['path'])
        elif request.method == 'POST':
          return request.form.get('hello', '')
      _routes[item['path']] = _

add_route_from_config(config)
