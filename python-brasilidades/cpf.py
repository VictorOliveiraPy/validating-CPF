class CPF:
    def __init__(self, document):
        self.document = str(document)
        if self.cpf_is_valid(document):
            self.cpf = document
        else:
            raise ValueError('CPF invalido!!')

    def __str__(self):
        return self.format_cpf()

    def cpf_is_valid(self, document):
        return len(document) == 11

    def format_cpf(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]

        return f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}'


obj = CPF('71218926422')
print(obj)