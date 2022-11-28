import argparse

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-input_file', metavar='GENBANK_FILE', default='input_files/NM_000249.gb')
    parser.add_argument('-output_file', metavar='FASTA_FILE', default='output_files/Ejercicio1_protein.fasta')
    args = parser.parse_args()

    genbank_file_path = args.input_file
    output_path = args.output_file

    genbank_file = open(genbank_file_path, 'r')
    genbank_count = 1

    for genebank in SeqIO.parse(genbank_file, 'genbank'):
        print(f'------------- Genbank record #{genbank_count} -------------')
        neuclotide_sequence = genebank.seq
        neuclotide_sequence_complementary = genebank.seq.reverse_complement()

        orfs = [1, 2, 3]
        longest_protein_by_orf = {1: '', 2: '', 3: ''}
        longest_protein_complementary_by_orf = {1: '', 2: '', 3: ''}
        longest_protein = ''

        for orf in orfs:
            longest_protein_local = ''
            neuclotide_sequence_with_ORF_applied = neuclotide_sequence[orf-1:]
            aminoacids = neuclotide_sequence_with_ORF_applied.translate()
            aminoacids_separated_by_stop_codons = aminoacids.split('*')
            for protein in aminoacids_separated_by_stop_codons:
                start_position = protein.find('M')
                if start_position != -1:
                    protein = protein[start_position:]
                    if len(protein) > len(longest_protein_local):
                        longest_protein_local = protein
                    if len(protein) > len(longest_protein):
                        longest_protein = protein
            longest_protein_by_orf[orf] = longest_protein_local
        
            longest_protein_local = ''
            neuclotide_sequence_complementary_with_ORF_applied = neuclotide_sequence_complementary[orf-1:]
            aminoacids_complementary = neuclotide_sequence_complementary_with_ORF_applied.translate()
            aminoacids_complementary_separated_by_stop_codons = aminoacids_complementary.split('*')
            for protein in aminoacids_complementary_separated_by_stop_codons:
                start_position = protein.find('M')
                if start_position != -1:
                    protein = protein[start_position:]
                    if len(protein) > len(longest_protein_local):
                        longest_protein_local = protein
                    if len(protein) > len(longest_protein):
                        longest_protein = protein
            longest_protein_complementary_by_orf[orf] = longest_protein_local

        print(f'--- Longest protein ---\n{longest_protein}')
        print(f'--- Length of longest protein ---\n{len(longest_protein)}')

        protein_records = []

        for key, val in longest_protein_by_orf.items():
            protein_records.append(SeqRecord(val, description=f'Protein translated from {genebank.id} with ORF = {key}, using main stripe'))
        
        for key, val in longest_protein_complementary_by_orf.items():
            protein_records.append(SeqRecord(val, description=f'Protein translated from {genebank.id} with ORF = {key}, using complementary stripe'))
        
        SeqIO.write(protein_records, output_path, 'fasta')

        genbank_count += 1
