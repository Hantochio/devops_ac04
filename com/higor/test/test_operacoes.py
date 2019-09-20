from unittest import TestCase
from com.higor.operacoes import Operacoes

class TestOperacoes(TestCase):
	
	def setUp(self):
		self.operacoes = Operacoes()
		
	def test_potencia(self):
		self.assertEqual(self.operacoes.potencia(2,4), 16)