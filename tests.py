#!/usr/bin/env python2

import unittest
import os
from classes import Results
from classes import Sampler


class test_SamplerClass(unittest.TestCase):
    def setUp(self):
        pass

    def test_something(self):
        pass

    def test_something_else(self):
        pass


class test_ResultsClass(unittest.TestCase):
    def setUp(self):
        proteins = range(10)
        answers = ['cancer','cancer','cancer','cancer','cancer',\
                   'nonCancer','nonCancer','nonCancer','nonCancer',\
                   'nonCancer']

        protein_answer = zip(proteins, answers)

        predictions = ['nonCancer','nonCancer','nonCancer','cancer',\
                       'cancer', 'cancer','nonCancer','nonCancer',\
                       'nonCancer', 'nonCancer']

        
        self.obj = Results( protein_answer, predictions )

    def test_something(self):
        pass

    def test_something_else(self):
        pass

class test_resources_available(unittest.TestCase):
    def test_humanppi_txt(self):
        self.assertTrue(os.path.exists('ResourceFiles/humanPPI.txt'))

    def test_functions_txt(self):
        self.assertTrue(os.path.exists('ResourceFiles/Functions.txt'))

    def test_cancer_txt(self):
        self.assertTrue(os.path.exists('ResourceFiles/Cancer.txt'))

    def test_test1_txt(self):
        self.assertTrue(os.path.exists('ResourceFiles/Test1.txt'))

    def test_test2_txt(self):
        self.assertTrue(os.path.exists('ResourceFiles/Test2.txt'))


    
