#!/usr/bin/env /bin/bash

if [ -f "$1" ]; then
    INPUT_FILE="$1"
else
    echo "Usage: $0 <your-CycloneDX.json> <your-deny-list.txt>"
    exit 1
fi

if [ -f "$2" ]; then
    DENY_LIST="$2"
else
    echo "Usage: $0 <your-CycloneDX.json> <your-deny-list.txt>"
    exit 1
fi

tmpfile=$(mktemp)
while read line 
do
    echo "Filtering $line..." 1>&2
    recipe=".components[] | select(.\"bom-ref\"==\"$line\")"
    cat "$INPUT_FILE" | jq "$recipe" >> "$tmpfile"
done < "$DENY_LIST"

cat "$tmpfile"
rm "$tmpfile"
