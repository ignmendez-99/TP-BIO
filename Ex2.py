from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastpCommandline

if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     fasta_file_path = sys.argv[1]
    # else:
        # fasta_file_path = 'output_files/Ejercicio1_1.fasta'
    fasta_file_path = 'output_files/Ejercicio1_1.fasta'
    
    fasta_file = open(fasta_file_path, 'r')

    for fastaRec in SeqIO.parse(fasta_file, 'fasta'):
        # cline = NcbiblastpCommandline(cmd=f"$(dirname {__file__})/ncbi-blast-2.13.0+/blast/bin/blastp", db="swissport", remote=True)
        cline = NcbiblastpCommandline(db="nr", remote=True)
        print(cline(str(fastaRec.seq)))