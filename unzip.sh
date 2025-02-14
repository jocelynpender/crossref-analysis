#!/bin/bash

# Navigate to the specified folder
cd "/Users/jocelynpender/Documents/02 - AREAS/Career/2025 Update/Crossref/interview-prep/sample-data/[Sample Dataset] April 2024 Public Data File from Crossref" || exit

# Unzip all .gz files in the specified directory
for file in *.gz; do
    if [ -f "$file" ]; then
        gunzip "$file"
    fi
done