import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)

data = pd.read_csv("data.csv")
data["Fate"] = data["Fate"].apply(lambda x: x.replace("\n", ""))
data["UBoat"] = data["UBoat"].apply(lambda x: x.upper())



print(data)
