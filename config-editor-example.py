import json
import sys
import pprint

configfilename = sys.argv[1]
configfile = open(configfilename)

config = json.load(configfile)
pprint.pprint(config)
