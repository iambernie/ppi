#!/usr/bin/env python2

import argparse

import networkx as nx

from classes import Sampler
from classes import Results
from classes import Bunch
from classes import Protein
from classes import CancerProtein
from classes import Function

from misc import readfile


def main():
    """
    In pseudo-code:

       load data

       create graphs from data

       for {kfoldcross times}
           do {take sample from training data}
              predict results on remainder (= proteins not in sample)
              measure results on remainder  

       take average f-measure

    Parameters
    ----------
    See args.

    """
    data = load_data()
 
    hgraph = nx.Graph(data.humanppi)
    fgraph = nx.Graph(data.functions)

    if args.test2:
        print "run predictions on test2 set"
        proteins_test2 = data.test2
        predictions = predict_cps(proteins_test2, hgraph, fgraph)
        print zip(proteins_test2, predictions)
        write_test2_prediction(proteins_test2, predictions)

    else:
        sampler = Sampler(data.test1, args.samplesize)
        results = list() #to be populated by Results class objects 

        for i in range(args.kfoldcross):
            sample = zip(*sampler.remainder)[0]
            predictions = predict_cps(sample, hgraph, fgraph)
            result = Results(sampler.remainder, predictions)
            results.append(result)
            sampler.resample()
            if args.verbose:
                result.print_results()
            result.print_confusion_matrix()

        f_measures = [i.f_measure for i in results]
        avg_f_measure = sum(f_measures)/float(len(f_measures))
        print "\n\nAverage F-Measure:", avg_f_measure

    pause = raw_input("Hit Enter to continue... ")

    return 0

def write_test2_prediction(proteins, predictions):
    f = open('PredictionResultsTest2.txt','w')
    for p, pred in zip(proteins, predictions):
        string = ','.join(["Prot_"+str(p), pred])+'\n'
        f.write(string)
    f.close()

def predict_cps(proteins, hgraph, fgraph):
    """

    Parameters
    ----------
    proteins: list of Protein instances.
    hgraph: networkx.Graph() instance
    fgraph: networkx.Graph() instance

    Return
    ------
    predictions: list of predictions, i.e. ['cancer','nonCancer', etc.]

    """
    predictions = list()
    for p in proteins:
        if p.cancerweight(hgraph, fgraph) > 15000:
            predictions.append('cancer')
        else:
            predictions.append('nonCancer')
    return predictions

def load_data():
    """ 
    Loads all data from the ResourceFiles directory. 

    Parameters
    ----------
    None - input data is constant.

    Returns
    -------
    Bunch class containing ResourceFiles.

    Example
    -------
    >>> from ppi.misc import load_data()
    >>> data = load_data()
    >>> data.humanppi[0:5]
    [(Protein: 0, Protein: 6476), (Protein: 1, Protein: 604), 
     (Protein: 1, Protein: 3466), (Protein: 1, Protein: 5215), 
     (Protein: 1, Protein: 7154)]
    >>> data.functions[0:5]
    [(Protein: 0, Function: F0003723), (Protein: 0, Function: F0035097),
     (Protein: 0, Function: F0016568), (Protein: 0, Function: F0051568),
     (Protein: 0, Function: F0016740)]
    >>> data.cancer[0:5]
    [241, 249, 255, 266, 287]
    >>> data.test1[0:5]
    [(Protein: 0, 'nonCancer'), (Protein: 1, 'nonCancer'), 
     (Protein: 1208, 'cancer'), (Protein: 2431, 'cancer'), 
     (Protein: 2, 'nonCancer')]
    
    """
    cancer_txt = readfile('ResourceFiles/Cancer.txt')
    cancer = [line.strip() for line in cancer_txt]
    cancer = [ int(line[5:]) for line in cancer ]

    humanppi_txt = readfile('ResourceFiles/humanPPI.txt')
    humanppi = [line.strip().split(',') for line in humanppi_txt]
    humanppi = [ tuple([int(elem[5:]) for elem in line ])  for line in \
                 humanppi ]
    temp = []
    for p1, p2 in humanppi:
        if p1 in cancer:
            a = CancerProtein(p1)
        else: 
            a = Protein(p1)

        if p2 in cancer:
            b = CancerProtein(p2)
        else: 
            b = Protein(p2)
        temp.append((a,b))
    del humanppi
    humanppi = temp    
        
    functions_txt = readfile('ResourceFiles/Functions.txt')
    functions = [line.strip().split(',') for line in functions_txt]
    functions = [ tuple([int(line[0][5:]), "F"+line[1][5:]] ) for line \
                  in functions ]

    f = []
    for p, fn in functions:
        if p in cancer:
            a = CancerProtein(p)
        else: 
            a = Protein(p)
        b = Function(fn) 
        f.append((a,b))
    del functions
    functions = f    

    test1_txt = readfile('ResourceFiles/Test1.txt')
    test1 = [line.strip().split(',') for line in test1_txt]
    test1 = [ tuple( [int(line[0][5:]), line[1] ] )  for line in test1 ]
    test1 = [ (Protein(p), answer) for p, answer in test1]

    test2_txt = readfile('ResourceFiles/Test2.txt')
    test2 = [line.strip().split(',') for line in test2_txt]
    test2 = [ int(line[0][5:]) for line in test2 ]
    test2 = [ Protein(p) for p in test2]

    data = Bunch(humanppi = humanppi,\
                 functions=functions,\
                 cancer=cancer,\
                 test1=test1,\
                 test2=test2)
    return data


def get_options():
    parser = argparse.ArgumentParser()

    parser.add_argument('-v','--verbose',\
                   action='store_true',\
                   help='Increases verbosity.')
    parser.add_argument('-k','--kfoldcross', type=int, default=10,\
                   help='Cross validates k times')
    parser.add_argument('-s','--samplesize', type=float, default=0.90,\
                   help='Percentage of test1 to train on. Example:\
                   -s 0.9 will use 90 percent of test1 to train on.')
    #parser.add_argument('-t','--trainingset', default=False,
    #               action='store_true',\
    #               help='Run predictions on trainingset Test1.txt.')
    parser.add_argument('-t','--test2', default=False,
                   action='store_true',\
                   help='Run predictions on trainingset Test2.txt.')

    #parser.add_argument('filenames', type=str, nargs='+',
    #               help='photometric data to load.')
    #parser.add_argument('-o','--outputdir', type=str, default='images',\
    #               help='output directory for images.')
    #parser.add_argument('-f','--full',\
    #               action='store_true',\
    #               help='print full arrays.')
    #parser.add_argument('-m','--max_turns', type=int, default=100000,\
    #               help='maximum number of turns')
    #parser.add_argument('t_init', type=str, nargs='+',
    #               help='length of initial set')
    #parser.add_argument('-o','--outputdir', type=str, default='images',\
    #               help='output directory for images.')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_options()
    assert 0 < args.samplesize < 1
    print args
    main()
