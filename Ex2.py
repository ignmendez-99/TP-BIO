from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastpCommandline

if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     fasta_file_path = sys.argv[1]
    # else:
        # fasta_file_path = 'output_files/Ejercicio1_1.fasta'
    fasta_file_path = 'output_files/Ejercicio1_1.fasta'
    
    fasta_file = open(fasta_file_path, 'r')

    for i,fastaRec in enumerate(SeqIO.parse(fasta_file, 'fasta')):
        # cline = NcbiblastpCommandline(cmd=f"$(dirname {__file__})/ncbi-blast-2.13.0+/blast/bin/blastp", db="swissport", remote=True)
        cline = NcbiblastpCommandline(db="swissprotDB",remote=False)
        with open(f'output_files/blast{i}.out','w') as f:
            f.write(str(cline(str(fastaRec))))