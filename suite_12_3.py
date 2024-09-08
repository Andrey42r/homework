import unittest
import tests_12_1
import tests_12_2

RunTest = unittest.TestSuite()
RunTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
RunTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RunTest)