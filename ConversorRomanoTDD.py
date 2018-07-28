class ConversorRomano(object):
	def __init__(self):
		super(ConversorRomano, self).__init__()
		self.algarismos = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

	def converterAlgarismo(self, letra):
		for algarismo in self.algarismos:
			if (algarismo == letra):
				return self.algarismos[algarismo]

	def converter(self, numeroRomano):
		numeroRomano = numeroRomano.upper()
		self.validarNumeroRecebido(numeroRomano)

		numeroArabico = self.converterAlgarismo(numeroRomano[0])
		tam = len(numeroRomano)
		if (tam > 1):
			for i in range(1, tam):
				valorDoAtual = self.converterAlgarismo(numeroRomano[i])
				valorDoAnterior = self.converterAlgarismo(numeroRomano[i-1])
				if (valorDoAtual <= valorDoAnterior):
					if (valorDoAtual > numeroArabico):
						raise ValueError("Numero Romano passado eh invalido: "+ numeroRomano)
					numeroArabico += valorDoAtual
				else:
					numeroArabico -= valorDoAnterior
					if (numeroArabico < 0):
						raise ValueError("Numero Romano passado eh invalido: "+ numeroRomano)
					numeroArabico += valorDoAtual - valorDoAnterior

			if (numeroArabico in self.algarismos.values()):
				raise ValueError("Numero Romano passado eh invalido: "+ numeroRomano)

		return numeroArabico

		

	def validarNumeroRecebido(self, numeroRomano):
		tam = len(numeroRomano)
		if (tam <= 1):
			if numeroRomano not in self.algarismos:
				raise ValueError("Algarismo Romano passado eh invalido: "+ numeroRomano)
		else:
			for letra in numeroRomano:
				if letra not in self.algarismos:
					raise ValueError("Numero Romano passado contem algarismos invalidos: "+ numeroRomano)

			algarismosInvalidos = ["VV", "LL", "DD", "IIII", "XXXX", "CCCC", "MMMM"]
			for algarismo in algarismosInvalidos:
				if algarismo in numeroRomano:
					raise ValueError("Numero Romano passado possui sequencia de algarismos invalida: "+ numeroRomano)

			for i in range(1, tam):
				valorDoAtual = self.converterAlgarismo(numeroRomano[i])
				valorDoAnterior = self.converterAlgarismo(numeroRomano[i-1])
				if valorDoAtual > valorDoAnterior:
					if (valorDoAnterior == 5 or valorDoAnterior == 50 or valorDoAnterior == 500 or (valorDoAnterior*5 != valorDoAtual and valorDoAnterior*10 != valorDoAtual)):
						raise ValueError("Numero Romano passado possui sequencia de algarismos invalida: "+ numeroRomano)


		

class TestConversorRomano(object):

	def test_deve_converter_numero_romano_simples_valido(self):
		algarismosSimples = {"I":1, "v":5, "X":10, "L":50, "c":100, "D":500, "m":1000}
		for algarismo in algarismosSimples:
			assert ConversorRomano().converter(algarismo) == algarismosSimples[algarismo]

	def test_deve_rejeitar_numero_romano_simples_invalido(self):
		algarismosInvalidos = ["", "H", "*", "3"]
		for algarismo in algarismosInvalidos:
			try:
				ConversorRomano().converter(algarismo)
				assert False
			except ValueError as e:
				assert True

	def test_deve_converter_numero_romano_de_dois_algarismos_valido(self):
		algarismosDuplos = {"VI":6, "Iv":4, "XX":20}
		for algarismoDuplo in algarismosDuplos:
			assert ConversorRomano().converter(algarismoDuplo) == algarismosDuplos[algarismoDuplo]

	def test_deve_rejeitar_numero_romano_de_dois_algarismos_iguais_invalido(self):
		algarismosDuplos = ["VV", "LL", "DD"]
		for algarismo in algarismosDuplos:
			try:
				ConversorRomano().converter(algarismo)
				assert False
			except ValueError as e:
				assert True

	def test_deve_rejeitar_numero_romano_de_dois_algarismos_diferentes_invalido(self):
		algarismosInvalidos = [
			"IL", "IC", "ID", "IM", "VX", "VL", "VC", "VD", "VM", "XD", "XM", "LC", "LD", "LM", "DM"
		]
		for algarismo in algarismosInvalidos:
			try:
				ConversorRomano().converter(algarismo)
				assert False
			except ValueError as e:
				assert True

	def test_deve_rejeitar_numero_romano_invalido_de_tres_algarismos(self):
		algarismosInvalidos = ["IVI", "IIX", "CMM", "IXL", "IIV","IIX","XXL","XXC","CCD","CCM","IVI","IXI","IXL","XCM"]
		for algarismo in algarismosInvalidos:
			try:
				ConversorRomano().converter(algarismo)
				assert False
			except ValueError as e:
				assert True

	def test_deve_rejeitar_numeros_romanos_com_mais_de_tres_algarismos_repetidos(self):
		algarismosInvalidos = ["IIII", "XXXX", "CCCC", "MMMM"]
		for algarismo in algarismosInvalidos:
			try:
				ConversorRomano().converter(algarismo)
				assert False
			except ValueError as e:
				assert True

	def test_deve_converter_numeros_romanos_validos_com_mais_de_dois_algarismos(self):
		algarismos = {"XIX":19, "XLIV":44, "LXXIII":73, "LXXXVIII":88, "XCIX":99, "CMXXV":925, "MMCCC":2300}
		for algarismo in algarismos:
			assert ConversorRomano().converter(algarismo) == algarismos[algarismo]
			
def main():
	print(ConversorRomano().converter("MMLVIIIX"))
if __name__ == '__main__':
	main()