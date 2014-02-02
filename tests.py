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

"""
class test_KeplerObject(unittest.TestCase):
    def setUp(self):
        self.testobj = KeplerObject(0.1, 1|units.AU, \
                           math.radians(60)|units.rad,\
                           math.radians(30)|units.rad,\
                           math.radians(15)|units.rad)

    def test_type(self):
        self.assertTrue(isinstance(self.testobj, KeplerObject))

    def test_period_without_central_body(self):
        self.assertIsNone(self.testobj.period)

    def test_period_with_central_body(self):
        mass = 1|units.MSun
        self.testobj.central_body_mass = mass
        self.assertTrue(hasattr(self.testobj, 'period'))

    def test_time_since_last_periapsis(self):
        self.testobj.central_body_mass = 4.31e+6|units.MSun
        self.testobj.periastron_epoch = 2002.5 |units.yr
        self.testobj.time = 2012.0 |units.yr
        self.assertEquals(9.5 |units.yr, self.testobj.time_since_last_periapsis)

    def test_mean_anomaly(self):
        self.testobj.periastron_epoch = 2002.5 |units.yr
        self.testobj.time = 2002.5 |units.yr
        self.testobj.central_body_mass = 4.31e+6|units.MSun
        self.assertEquals(0.0, self.testobj.mean_anomaly)

    def test_P_vector(self):
        self.testobj.periastron_epoch = 2002.5 |units.yr
        self.testobj.time = 2002.5 |units.yr
        self.testobj.central_body_mass = 4.31e+6|units.MSun
        self.assertTrue(hasattr(self.testobj, 'P_vector'))

    def test_cartesian(self):
        self.testobj.periastron_epoch = 2002.5 |units.yr
        self.testobj.time = 2012.5 |units.yr
        self.testobj.central_body_mass = 4.31e+6|units.MSun
        self.assertTrue(hasattr(self.testobj, 'cartesian'))

"""

    
