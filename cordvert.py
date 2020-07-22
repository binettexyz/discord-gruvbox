# I wrote this in an hour.
# https://gist.github.com/CircuitRCAY/d4dbea9a9631834202a9af0a5feffeef
# Used for CI builds
import argparse
import getpass
import zipfile
import json
import os

parser = argparse.ArgumentParser(description="Convert a .css file to an installable Powercord theme.")
parser.add_argument('-n', "--name", help='Sets the theme name.', default="powercord-theme")
parser.add_argument("-v", "--version", help="Sets the theme version.", default="1.0.0")
parser.add_argument("-d", "--desc", help="Sets the theme description.", default="Converted by Cordvert(tm)")
parser.add_argument("-a", "--author", help="Sets the theme author.", default=getpass.getuser())
parser.add_argument("-t", "--theme", "--css", help="Sets the theme path. /use/a/full/path", default="theme.css")
parser.add_argument("-l", "--license", help="Sets the theme license", default="unknown")
parser.add_argument("-o", "--output", help="Sets the output name.", default="theme.zip")

args = parser.parse_args()

if args == {}:
    parser.print_help()

themename = os.path.basename(args.theme)

manifest = {
    "name": args.name,
    "version": args.version,
    "description": args.desc,
    "author": args.author,
    "theme": themename
}

print("Writing file now....")
with zipfile.ZipFile(args.output, 'w') as z:
    f = open(args.theme, "r")
    z.writestr(themename, f.read())
    z.writestr('powercord_manifest.json', json.dumps(manifest))
    print(f"Written theme to {args.output}!")