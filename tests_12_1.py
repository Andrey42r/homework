import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def test_walk(self):
        run_1 = Runner('Tesla')
        for i in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    def test_run(self):
        run_2 = Runner('Lada')
        for i in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

    def test_challenge(self):
        run_3 = Runner('Dodge')
        run_4 = Runner('Porshe')
        for i in range(10):
            run_3.run()
            run_4.walk()
        self.assertNotEqual(run_3.distance, run_4.distance)

    is_frozen = False
