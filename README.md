# TP-Bioinformatica

## Pre-requisitos
- Hay que tener Python 3 instalado en nuestros sistemas
- Hay que tener instalado EMBOSS

## Ejercicio 1
```
python Ejercicio1.py [-input_file ARCHIVO_GENBANK] [-output_file ARCHIVO_FASTA] 
```

## Ejercicio 2:

Para correr el ejercicio 2 primero debemos instalar blast corriendo el siguiente archivo:

- `blast/installBlastUbuntu.sh`

Luego podemos hacer:

- `source blast/addEnv`

para agregar blast al `$PATH` y asi poder correr `blastp`. Por ulitmo corremos:

- `Ejercicio2.sh local`
o
- `Ejercicio2.sh remoto`

dependiendo de si queremos correrlo local o remoto

### Ejercicio 3
```
python Ejercicio3.py [-input_file BLAST_OUTPUT] [-output_file ARCHIVO_FASTA] [-n N]
```

### Ejercicio 4
```
python Ejercicio4.py [-input_file ARCHIVO_BLAST_XML] -pattern PATTERN [-output_file ARCHIVO_BLAST_XML_OUTPUT] [-output_directory OUTPUT_FASTA_DIRECTORY] [-N MAX_RESULTS]
```