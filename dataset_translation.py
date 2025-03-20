import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/MoizesCBF/iacd_dataset/refs/heads/main/Flight_Price.csv')

df = df.drop(columns=["Unnamed: 0"])

rename_dict = {
    "airline": "Companhia Aérea",
    "flight": "Voo",
    "source_city": "Cidade de Origem",
    "departure_time": "Horário de Partida",
    "stops": "Paradas",
    "arrival_time": "Horário de Chegada",
    "destination_city": "Cidade Destino",
    "class": "Classe",
    "duration": "Duração (Horas)",
    "days_left": "Antecedência da Reserva (Dias)",
    "price": "Preço (Rúpia Indiana)"
}

df = df.rename(columns=rename_dict)

airline_mapping = {
    "Indigo": "IndiGo",
    "GO_FIRST": "Go First",
    "AIR_INDIA": "Air India",
}

df["Companhia Aérea"] = df["Companhia Aérea"].replace(airline_mapping)

time_mapping = {
    "Late_Night": "0h~3h",
    "Early_Morning": "3h~6h",
    "Morning": "6h~12h",
    "Afternoon": "12h~18h",
    "Evening": "18h~21h",
    "Night": "21h~0h"
}

df["Horário de Partida"] = df["Horário de Partida"].replace(time_mapping)
df["Horário de Chegada"] = df["Horário de Chegada"].replace(time_mapping)

stops_mapping = {
    "one": "Uma",
    "zero": "Nenhuma",
    "two_or_more": "Duas ou Mais"
}

df["Paradas"] = df["Paradas"].replace(stops_mapping)

class_mapping = {
    "Economy": "Econômica",
    "Business": "Executiva"
}

df["Classe"] = df["Classe"].replace(class_mapping)

df.to_csv('PassagemAerea.csv', index=False)
