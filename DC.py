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

from flask import Flask, request

app = Flask(__name__)
config = [
  {
    'path': '/',
    'auth': {
      'type': 'bacic_auth',
      'username': 'admin',
      'password': '123456'
    }
  }
]

@app.route('/api/set_config')
def set_config():
  if request.method == 'POST':
    global config
    config = request.args.get('config', config)
    return 'Rust master DC No.1!'
