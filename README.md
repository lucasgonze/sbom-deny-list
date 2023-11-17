# SBOM False Positive Filter

A tool to remove false positives from an SBOM. This allows humans to flag and remove incorrect items in output from an automated generator. 

Assumes your SBOM uses CycloneDX.

Test out your installation like this: 
`python3 filter-deny-list.py sample-data.json sample-deny-list.txt`

Using:
1. Generate a CycloneDX SBOM using a tool like Snyk. See `sample-data.json` for an example.
2. Read the "components" part of the SBOM to find incorrectly identified items, maybe using a JSON editor like jsoneditoronline.org. Typically these are fuzzy matches based on snippet text.
3. When you find a wrong item, copy its `bom-ref` value.
4. Paste the bom-ref value into a line in a file. See `sample-deny-list.txt`
5. Run `python3 filter-deny-list.py your-sbom.json your-deny-list.txt > filtered-sbom.json`




