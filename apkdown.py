from src.api import ApkDownApi
import sys

WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

api = ApkDownApi()

argLen = len(sys.argv)

if argLen == 1:
    print "               __       .___                     "         
    print "_____  ______ |  | __ __| _/______  _  ______    "
    print "\__  \ \____ \|  |/ // __ |/  _ \ \/ \/ /    \   "
    print " / __ \|  |_> >    </ /_/ (  <_> )     /   |  \  "
    print "(____  /   __/|__|_ \____ |\____/ \/\_/|___|  /  "
    print "     \/|__|        \/    \/                 \/   \n"

    print FAIL + "          Version 0.0.1 | Dev @Bym24v " + ENDC + "\n"

    print WARNING + "[INFO] Insert command -h to visualize the help\n" + ENDC + "\n"


def ApkDownHelp():

    print "\n"
    print "[Metadata]\n"
    print "  [ -metadata ] package android\n"

    print "[Store]\n"
    print "  [ -store ] name store"
    print "  [ -limit ] limit\n"

    print "[Search]\n"
    print "  [ -search ] name app"
    print "  [ -limit ] limit\n"

    print "[Download]\n"
    print "  [ -down ] name app\n"

    print WARNING + "[EX] Metadata: apkdown.py -metadata cm.aptoide.pt\n" + ENDC
    print WARNING + "[EX] Store: apkdown.py -store apps -limit 3\n" + ENDC
    print WARNING + "[EX] Search: apkdown.py -search Twitter -limit 1\n" + ENDC
    print WARNING + "[EX] Download: apkdown.py -down Twitter\n" + ENDC
    

if argLen > 1:
    CLI = str(sys.argv[1])

    if CLI == "-h":
        ApkDownHelp()
    elif CLI == "-metadata":
        package = str(sys.argv[2])
        print api.get_app_metadata(package)
    elif CLI == "-store":
        name = str(sys.argv[2])
        cli_limit = str(sys.argv[3])
        if cli_limit == "-limit":
            limit = str(sys.argv[4])
            print api.get_store_apps(name, limit)
    elif CLI == "-search":
        name = str(sys.argv[2])
        cli_limit = str(sys.argv[3])
        if cli_limit == "-limit":
            limit = str(sys.argv[4])
            print api.get_search_apps(name, limit)
    elif CLI == "-down":
        name = str(sys.argv[2])
        api.get_download_app(name)
