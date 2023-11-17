import json
import argparse

parser = argparse.ArgumentParser(
    prog='sbom-deny-list',
    description='Filter false positives out of a CycloneDX SBOM',
    epilog="https://github.com/lucasgonze/sbom-deny-list"
    )
parser.add_argument('sbom', 
                    help='File containing CycloneDX JSON')
parser.add_argument('deny', 
                    help='File containing bom-ref values to filter out, one per line')
args = parser.parse_args()

print(args)
f = open(args.sbom)
data = json.load(f)
f.close()

with open(args.deny) as my_file:
    deny_list = my_file.readlines()

if "components" not in data:
    print("Invalid SBOM")
    SystemExit(1)

filtered = []
for component in data["components"]:
    if "bom-ref" not in component or component["bom-ref"] not in deny_list:
        filtered.append(component)
data["components"] = filtered

print(json.JSONEncoder().encode(data))

