import argparse
import json
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


def read_result(data: dict, n: int) -> list:
    results = []
    hits = data['BlastOutput2']['report']['results']['search']['hits']
    for i in range(0, n):
        hit = hits[i]
        result = {'description': hit['description'][0]['title'], 'id': hit['description'][0]['id'], 'seq': hit['hsps'][0]['hseq']}
        results.append(result)
    return results


def write_output_file(results: list, output_file: str) -> None:
    records = []
    for result in results:
        records.append(SeqRecord(Seq(result['seq']), id=result['id'], description=result['description']))

    SeqIO.write(records, output_file, 'fasta')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-input_file', type=str, help='Path al archivo input (output de BLAST) (en formato JSON)', default='output_files/Ejercicio2/blast_1.json')
    parser.add_argument('-output_file', type=str, help='Path al archivo output', default='output_files/Ejercicio3/Ejercicio3_top_resultados.fasta')
    parser.add_argument('-n', type=int, help='Cantidad de resultados', default=10)
    args = parser.parse_args()

    file = open(args.input_file)
    data = json.load(file)

    results = read_result(data, args.n)

    write_output_file(results, args.output_file)
    
