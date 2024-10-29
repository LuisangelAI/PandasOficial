# Importamos la biblioteca pandas y la llamamos pd 
import pandas as pd 
# Creamos una Serie de pandas que es como una lista con etiquetas 
# Los valores son nombres de jugadores de PSG
# El índice especifica los números de camisetas de esos jugadores
psg_players_list = pd.Series(
    ['Navas', 'Mbappe', 'Neymar', 'Messi']#,# Lista de jugadores
# index = [1, 7, 10, 30] # Lista de Camisetas
)
# creamos un diccionario que asocia numeros de camiseta con nombres de jugadores
psg_dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi' }
# Creamos una serie de pandas usando el diccionario
psg_players_dict = pd.Series(psg_dict)
# Imprimimos la serie para ver su contenido
#print(psg_players_dict)

# print(psg_players)
print(psg_players_dict )
# Imprimimos el valor en la posicion (index) 7 de la serie creada a partir del diccionario
print(psg_players_dict[7])
print(psg_players_dict[0:3])
# diccionario con datos de jugadores
# Diccionario con datos de jugadores
dict = { 'Jugador' : ['Navas', 'Mbappe', 'Neymar', 'Messi'],
        'Altura': [183.0, 170.0, 170.0, 165.0],
        'Goles' : [2, 200, 150, 200]}
# Creamos un DataFrame con el diccionario e indices personalizados
df = pd.DataFrame(dict, index = [1, 7, 10, 30])
# Imprimimos el DataFrame
print(df)