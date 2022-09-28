#!/bin/bash

printUsage(){
    echo "Usage Ejercicio2.sh (local|remoto)";
    exit 1
}

INPUT_FILE="output_files/Ejercicio1_1.fasta"
OUTPUT_FILE="output_files/blast.json"

if [[ $# -ne 1 ]] 
then
    printUsage;
fi

if [[ "$1" = "local" ]]
then
    echo "Doing a local search from $INPUT_FILE to $OUTPUT_FILE"
    blastp -db swissprotDB -query $INPUT_FILE -out $OUTPUT_FILE -outfmt 13
elif [[ "$1" = "remoto" ]]
then
    echo "Doing a renote search from $INPUT_FILE to $OUTPUT_FILE"
    blastp -db swissprot -query $INPUT_FILE -out $OUTPUT_FILE -outfmt 13 -remote
else 
    printUsage;
fi