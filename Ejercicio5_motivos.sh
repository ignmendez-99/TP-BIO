#!/bin/bash


input="output_files/Ejercicio1_protein.fasta"
output="output_files/Ejercicio5/motifs.patmatmotifs"
download=true

if $download
then
    wget https://ftp.expasy.org/databases/prosite/prosite.dat
    wget https://ftp.expasy.org/databases/prosite/prosite.doc
    mkdir prosite
    mv prosite.dat prosite
    mv prosite.doc prosite
fi

prosextract prosite
patmatmotifs -sequence $input -outfile $output