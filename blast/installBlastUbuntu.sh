#!/bin/bash

source $(dirname $BASH_SOURCE)/envVars

(
    cd $BLAST_PATH ; 
    wget "https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/$BLAST_VERSION-x64-linux.tar.gz" && 
    tar -x -f $BLAST_VERSION-x64-linux.tar.gz && 
    rm $BLAST_VERSION-x64-linux.tar.gz && 
    $BLAST_PATH/installDBUbuntu.sh
)
