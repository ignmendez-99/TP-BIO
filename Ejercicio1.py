import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-gb')
    parser.add_argument('-o', default='.')
    args = parser.parse_args()
    genbank_file_path = args.gb
    output_path = args.o

    genbank_file = open(genbank_file_path,'r')

    for genebank in SeqIO.parse(genbank_file, 'genbank'):
        neuclotide_sequence = genebank.seq
        neuclotide_sequence_complementary = genebank.seq.reverse_complement()

        orfs = [1, 2, 3]
        longest_protein = ''

        for orf in orfs:
            neuclotide_sequence_with_ORF_applied = neuclotide_sequence[orf-1:]
            aminoacids = neuclotide_sequence_with_ORF_applied.translate()
            aminoacids_separated_by_stop_codons = aminoacids.split('*')
            for protein in aminoacids_separated_by_stop_codons:
                start_position = protein.find('M')
                if start_position != -1:
                    protein = protein[start_position:]
                    if len(protein) > len(longest_protein):
                        longest_protein = protein
        
            neuclotide_sequence_complementary_with_ORF_applied = neuclotide_sequence_complementary[orf-1:]
            aminoacids_complementary = neuclotide_sequence_complementary_with_ORF_applied.translate()
            aminoacids_complementary_separated_by_stop_codons = aminoacids_complementary.split('*')
            for protein in aminoacids_complementary_separated_by_stop_codons:
                start_position = protein.find('M')
                if start_position != -1:
                    protein = protein[start_position:]
                    if len(protein) > len(longest_protein):
                        longest_protein = protein

        print(longest_protein)
        print(len(longest_protein))