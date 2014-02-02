#!/usr/bin/env python2

proteins = range(10)
answers = ['cancer','cancer','cancer','cancer','cancer',\
           'nonCancer','nonCancer','nonCancer','nonCancer',\
           'nonCancer']

protein_answer = zip(proteins, answers)

predictions = ['nonCancer','nonCancer','nonCancer','cancer',\
               'cancer', 'cancer','nonCancer','nonCancer',\
               'nonCancer', 'nonCancer']
