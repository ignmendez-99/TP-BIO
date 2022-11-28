#!/bin/bash

input="input_files/NM_000249.gb"
output="output_files/Ejercicio5/orfs.fasta"

getorf -sequence $input -outseq $output