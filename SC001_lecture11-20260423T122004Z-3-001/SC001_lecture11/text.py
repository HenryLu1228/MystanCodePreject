import pandas as pd

data = pd.read_csv('titanic_data/test.csv')
print(data.PassengerId[data.Sex == 'male'][data.Pclass == 1][data.Age <= 17])