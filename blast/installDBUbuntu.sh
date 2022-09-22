#!/bin/bash

source $(dirname $BASH_SOURCE)/envVars

mkdir -p $BLAST_PATH/$BLAST_VERSION/data
(
    cd $BLAST_PATH/$BLAST_VERSION/data ; 
    wget "https://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/swissprot.gz" && 
    gzip --decompress swissprot.gz && 
    $BLAST_PATH/$BLAST_VERSION/bin/makeblastdb -in swissprot -out swissprotDB -dbtype prot
)