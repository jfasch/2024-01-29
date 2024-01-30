import sys
import json
import pprint

infilename = sys.argv[1]
outfilename = sys.argv[2]


configfile = open(sys.argv[1])
config = json.load(configfile)

print(config['instances'][0]['applicationType'])

outf = open(outfilename, 'x')
json.dump(config, outf, indent=4)
