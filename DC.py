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
config = {}
with open('example.json', 'r') as f:
  config = json.loads(f.read())
_routes = {}

@app.route('/<path:url>', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def route(url=''):
  url = '/' if request.path == '/' else '/{}'.format(url)
  if url == 'api/set_config':
    return set_config()
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

def make_basic_auth_view(username='', password='', next=['/'], auth_func=[]):
  def _basic_auth():
    auth = request.authorization
    if not auth or auth.username != username or auth.password != password:
      return Response('Please Login', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
  auth_func.append(_basic_auth)
  def _():
    for func in auth_func:
      result = func()
      if result:
        return result
    return render_template('next.html', urls=next)
  return _

def make_form_auth_view(username='', password='', next=['/'], action='/', auth_func=[]):
  def _form_auth():
    if username != request.cookies.get('username', '') or password != request.cookies.get('password', ''):
      abort(403)
  auth_func.append(_form_auth)
  def _():
    if request.method == 'GET':
      return render_template('form_auth.html', action=action)
    elif request.method == 'POST':
      if username == request.form.get('username', '') and password == request.form.get('password', ''):
        resp = Response(render_template('next.html', urls=next))
        resp.set_cookie('username', username)
        resp.set_cookie('password', password)
        return resp
      else:
        return Response(render_template('form_auth.html', action=action), 403)
  return _

def make_cookie_auth_view(username='', password='', next=['/'], auth_func=[]):
  def _cookie_auth():
    if username != request.cookies.get('username', '') or password != request.cookies.get('password', ''):
      abort(403)
  auth_func.append(_cookie_auth)
  def _():
    if username == request.cookies.get('username', '') and password == request.cookies.get('password', ''):
      resp = Response(render_template('next.html', urls=next))
      return resp
    else:
      resp = Response('Please Login', 401)
      return resp
  return _

def make_xss_view(path='', auth_func=[]):
  def _():
    for func in auth_func:
      result = func()
      if result:
        return result
    if request.method == 'GET':
      return render_template('xss.html', action=path)
    elif request.method == 'POST':
      return request.form.get('hello', '')
  return _

def make_general_view(urls=[], auth_func=[]):
  def _():
    for func in auth_func:
      result = func()
      if result:
        return result
    return render_template('next.html', urls=urls)
  return _

def get_all_subpage_path(item):
  result = [item['path']]
  subpage = item.get('subpage', [])
  for page in subpage:
    result += get_all_subpage_path(page)
  if '/' in result:
    result.remove('/')
  return result

def add_route_from_config(item, auth_func=[]):
  temp_auth_func = [] + auth_func
  if item['type'] == 'auth':
    if item['auth']['type'] == 'basic_auth':
      _routes[item['path']] = make_basic_auth_view(item['auth']['username'], item['auth']['password'], get_all_subpage_path(item), auth_func=temp_auth_func)
    elif item['auth']['type'] == 'form_auth':
      _routes[item['path']] = make_form_auth_view(item['auth']['username'], item['auth']['password'], get_all_subpage_path(item), item['path'], auth_func=temp_auth_func)
    elif item['auth']['type'] == 'cookie_auth':
      _routes[item['path']] = make_cookie_auth_view(item['auth']['username'], item['auth']['password'], get_all_subpage_path(item), auth_func=temp_auth_func)
  elif item['type'] == 'xss':
    _routes[item['path']] = make_xss_view(path=item['path'], auth_func=temp_auth_func)
  elif item['type'] == 'general':
    _routes[item['path']] = make_general_view(urls=get_all_subpage_path(item), auth_func=temp_auth_func)
  for i in item.get('subpage', []):
    add_route_from_config(i, temp_auth_func + [])
add_route_from_config(config)
