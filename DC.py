# -*- coding: utf-8 -*-

"""

██████╗ ██╗   ██╗███████╗████████╗    ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗     ███╗   ███╗██████╗    ██████╗  ██████╗
██╔══██╗██║   ██║██╔════╝╚══██╔══╝    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ████╗ ████║██╔══██╗   ██╔══██╗██╔════╝
██████╔╝██║   ██║███████╗   ██║       ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝    ██╔████╔██║██████╔╝   ██║  ██║██║     
██╔══██╗██║   ██║╚════██║   ██║       ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗    ██║╚██╔╝██║██╔══██╗   ██║  ██║██║     
██║  ██║╚██████╔╝███████║   ██║       ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║    ██║ ╚═╝ ██║██║  ██║██╗██████╔╝╚██████╗
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝                                                                                                                                
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB#+&BBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBB_ . *$BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB$.~++++++BBBBBBBBBBBBBB
BBBBBBBBBBBBBB_+++++++.=BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB ++++++++ BBBBBBBBBBBBBB
BBBBBBBBBBBBB$ +~++++++++_.BBBBBB ...  .+BBBB+: BBBBBB~=+++++~~=++ BBBBBBBBBBBBB
BBBBBBBBBBBBB#_+=o _++++++++ =,,,~:.++++++++ ,,~++ BB.+++++~ *.+++.BBBBBBBBBBBBB
BBBBBBBBBBBBB#:+.oooo^.~ ~~+++++++++~++++++++++ ~+++ +++++ ooo.~+++&BBBBBBBBBBBB
BBBBBBBBBBBBBB + ooooo:..~+~++++++++++++++++++++++++ +++=OooooO++++:BBBBBBBBBBBB
BBBBBBBBBBBBBB:+=oo ~+++++++++++++++++++++++++++++++.+++ oooooo~+++=BBBBBBBBBBBB
BBBBBBBBBBBBBBB +    +++++++++++++++++++++++++++++++ ++^*ooooo_++~~%BBBBBBBBBBBB
BBBBBBBBBBBBBBB$ + ++++++++++++++++++++++++++++++++++:+:~ ^ooo +++.BBBBBBBBBBBBB
BBBBBBBBBBBBBBBB:+++++++++~++=+++++++++:_++++++++++++++++++,.~+++^BBBBBBBBBBBBBB
BBBBBBBBBBBBBBB.++++++++++++++++++++++++++++++++++++++++++++++~ +++++:BBBBBBBBBB
BBBBBBBBBBBBBB:++~     ^^++++++++++++++++++++++=,^,++++++++++++++++~.BBBBBBBBBBB
BBBBBBBBBBBBB^^~        =$~+++++++++++++++++         $ +++++++++++~+: ^B%BBBBBBB
BBBBBBBBBB.:+~~          $$^++++++++++++++~           $$,+++++++++++++++ BBBBBBB
BBBBBBBo ~~~~~_.         $$=++++++++++++++            $$++~+~+~++,      :BBBBBBB
BBBBBB.~~~~~~~~          $#~+:++++~~++++++          ..$$. . .$$$$$$     B$$ _BBB
BBBBB:=~~~~~~~~~~      ..=++++++_+++++++++~         .:______ $   .$.     .$BB $B
BBBBB ~~~~~~~~~~~~~~~+++++++++++ +++++++++++~~^ .____*######+:&            %BB B
BBBBB ~~~~~~~~~~~~~~++++++++++++ o,+++++++++++~ _____________ B           . B%,&
BBBBB +~~~~~~~~~~~~+++++++++++++._~~~ _+++++++ _______________         ^+++~ BO+
BBBBBB ~~~~~~~~~~++++++++++++++~+++++++++++++= _______________^.,.^~++++++++ B B
BBBBBBB.~+++++++++++++++++++++++++++++++++++++.____________::_ +++++++++++++. ~B
BBBBBB*.o^++++++++++++++++++++++++++++++++++++=._:___________ =+++++++++++++.BBB
BB,,BB.  O+ +++++++++++++++++++++++++++++++++++: ___________ ~++++++++++++++ BBB
BB   .      B +++++++++++++++++++++++++++++++++++: ,_______ +++++++++++++++~ BBB
BB.       ,+^++++++++++++++++++++++++++++++++++++++++~=_~ :++++++++++++++++.BBBB
BB~     =++ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ %BBBB
BBB.+++++.=+~++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.%BBBBB
BBB#,~++ .  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:.BBBBBBB
BBB%#=++++^~++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:+ BBBBBBB
BBBBBB +++^++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ O%BBBB
BBBBBBBB  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.BBBB
BBBBBBBBB + +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ BB
BBBBBBBBB$B +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
BBBBBBBBBBB. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
BBBBBBBBBBBB^+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
