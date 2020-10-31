import unittest
from secao20_testes.ex_robo.robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self) -> None:
        self.megaman = Robo('Mega man', bateria=50)
        print('setUp() sendo executado...')

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), 'BEEP BOOP BEEP BOOP. EU SOU MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49), 'A bateria deveria estar em 49%'

    def tearDown(self) -> None:
        print('tearDOwn() sendo executado...')


if __name__ == '__main__':
    unittest.main()
