from unittest import TestCase


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

    def __repr__(self):
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
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.run_1 = Runner('Усейн', 10)
        self.run_2 = Runner('Андрей', 9)
        self.run_3 = Runner('Ник', 3)

    def test_run_1_tournament(self):
        tournament = Tournament(90, self.run_1, self.run_3)
        results = tournament.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == 'Ник')

    def test_run_2_tournament(self):
        tournament = Tournament(90, self.run_2, self.run_3)
        results = tournament.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == 'Ник')

    def test_run_3_tournament(self):
        tournament = Tournament(90, self.run_1, self.run_2, self.run_3)
        results = tournament.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(f'{i + 1}. {elem}')