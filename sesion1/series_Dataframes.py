import pandas as pd
psg_player = pd.Series(
    ['NAVAS','MBAPE','NEYMAR','MESSI'],
    index=[1,7,10,30]

)
psg_dict = {1:'NAVAS', 7:'MBAPE', 10:'NEYMAR', 30:'MESS'}
psg_players_dict = pd.Series(psg_player)
print(psg_players_dict)
print("**************************")
print(psg_players_dict[7])
print("**************************")
print(psg_players_dict[0:3])

print("**************************")

#dicionario con datos de jugadores
dict={ 'jugador':['NAVAS','MBAPE','NEYMAR','MESSI'],
      'Altura':[183.0,170.0,170.0,165.0],
      'Goles':[2,200,150,200]
      }

#crear un DataFrame con el diccioneario y indices personalizados
df = pd.DataFrame(dict, index=[1,7,10,30])

#Imprimir el DataFrame
print(df)