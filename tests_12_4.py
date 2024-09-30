import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            run_1 = Runner('Вося', -10)
            logging.info("'test_walk' выполнен успешно")
            for i in range(10):
                run_1.walk()
            self.assertEqual(run_1.distance, 100)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format="%(asctime)s - %(levelname)s - %(message)s")

    def test_run(self):
        try:
            run_2 = Runner(5, 7)
            logging.info("'test_run' выполнен успешно")
            for i in range(10):
                run_2.run()
            self.assertEqual(run_2.distance, 140)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format="%(asctime)s - %(levelname)s - %(message)s")

