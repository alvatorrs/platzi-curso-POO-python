#Ejemplo usando el decorador property

class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    #getter
    @property
    def region(self):
        return self.__region

    #setter
    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self.__pais}')

#Creamos el objeto
casilla = CasillaDeVotacion(123, ['CDMX','EDOMEX','GDJ'])
print(casilla.region)

#definiendo region
casilla.region = 'GDJ'
print(casilla.region)
