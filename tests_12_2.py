from unittest import TestCase
import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        result = {place: runner.name for place, runner in self.all_results.items()}
        print(f'{result}')

    def Tournament_test_1(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results.update(results)
        self.assertEqual(results[-1], self.nick)
        self.tearDownClass()

    def Tournament_test_2(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results.update(results)
        self.assertEqual(results[-1], self.nick)
        self.tearDownClass()

    def Tournament_test_3(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.all_results.update(results)
        self.assertEqual(results[-1], self.nick)


if __name__ == '__main__':
    unittest.main()