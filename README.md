# SBOM False Positive Filter

A tool to remove false positives from an SBOM. This allows humans to flag and remove incorrect items in output from an automated generator. 

Assumes:
1. You have installed [jq](https://en.wikipedia.org/wiki/Jq_(programming_language))
2. Your SBOM uses CycloneDX

Setup / Installation:
1. Install jq
2. Test out your installation like this: `./filter-deny-list.sh sample-data.json sample-deny-list.txt`

Using:
1. Generate a CycloneDX SBOM using a tool like Snyk. See `sample-data.json` for an example.
2. Read the "components" part of the SBOM to find incorrectly identified items, maybe using a JSON editor like jsoneditoronline.org. Typically these are fuzzy matches based on snippet text.
3. When you find a wrong item, copy its `bom-ref` value.
4. Paste the bom-ref value into a line in a file. See `sample-deny-list.txt`
5. Run `filter-deny-list.sh your-sbom.json your-deny-list.txt > filtered-sbom.json`




