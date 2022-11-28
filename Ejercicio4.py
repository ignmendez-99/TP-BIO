import shutil
import xml.etree.ElementTree as ET
import os
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import Entrez

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-input_file', default='output_files/blast.xml')
    parser.add_argument('-pattern', required=True)
    parser.add_argument('-output_file', default='output_files/Ejercicio4.xml')
    parser.add_argument('-output_directory', default='output_files/Ejercicio4_files')
    parser.add_argument('-n', type=int, required=True, default=5)

    args = parser.parse_args()

    blast_file = args.input_file
    pattern = args.pattern
    output_blast = args.output_file
    output_dir = args.output_directory
    max_results = args.n

    xml_tree = ET.parse(blast_file)
    xml_root = xml_tree.getroot()
    proteins = list(xml_root.find('BlastOutput_iterations').iter('Iteration'))
    filter_str = pattern.lower()
    data = []
    ids = []
    descriptions = []
    sequences = []
    for protein in proteins:
        hits = list(protein.find('Iteration_hits').iter('Hit'))
        for hit in hits:
            hit_description = hit.find('Hit_def').text
            if filter_str in hit_description.lower():
                data.append(hit)
                ids.append(hit.find('Hit_accession').text)
                descriptions.append(hit_description)
                sequences.append(hit.find('Hit_hsps').find('Hsp').find('Hsp_qseq').text)

    if max_results is not None:
        data = data[:max_results]
        ids = ids[:max_results]
        descriptions = descriptions[:max_results]
        sequences = sequences[:max_results]

    with open(output_blast, 'w') as save_file:
        save_file.write('<Hits>\n')
        for hit in data:
            xml = ET.tostring(hit, encoding='unicode')
            save_file.write(xml)
            save_file.write('\n')
        save_file.write('</Hits>\n')

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    else:
        shutil.rmtree(output_dir)
        os.mkdir(output_dir)

    Entrez.email = 'ignmendez@itba.edu.ar'

    for i, hit_id in enumerate(ids):
        with open(f"{output_dir}/result_{i}.fasta", 'w') as save_file:
            handle = Entrez.efetch(db="protein", id=hit_id, rettype="fasta", retmode="text")
            save_file.write(handle.read())
