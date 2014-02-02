#!/usr/bin/env python

import argparse
import networkx as nx

from main import load_data
from classes import Table

def main():
    data = load_data()

    fgraph = nx.Graph(data.functions)
    hgraph = nx.Graph(data.humanppi)

    T = Table(name='proteindata')

    for p, ans in data.test1:
        T.add('Protein', p)
        T.add('Degree', p.degree(hgraph) )
        T.add('CP Degree', p.cp_degree(hgraph) )
        T.add('Fn CP Degree', p.fn_cp_degree(hgraph, fgraph) )
        T.add('Fn CP Weight', p.fn_cp_weight(hgraph, fgraph))
        T.add('Cancer Weight', p.cancerweight(hgraph, fgraph))
        T.add('CP Degree Nbrs', p.cp_degree_of_neighbors(hgraph))
        T.add('Answer', ans)

    T.order = ['Protein', 'Degree', 'CP Degree', 'Fn CP Degree', 
               'Fn CP Weight', 'Cancer Weight', 'CP Degree Nbrs', 
               'Answer']

    write_table_to_file(T, 'test1data.csv')

def write_table_to_file(table, filename):
    filehandler = open(filename,'w')

    filehandler.write(table.columnnames())
    for line in table.lines_iter():
        filehandler.write(line)
    filehandler.close()


def get_options():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_options()
    main()
