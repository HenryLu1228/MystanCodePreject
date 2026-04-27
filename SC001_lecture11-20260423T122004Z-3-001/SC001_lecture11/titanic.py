import pandas as pd
import matplotlib.pyplot as plt


def main():
	filepath = 'titanic_data/train.csv'
	data = pd.read_csv(filepath)
	print(data)
	print(data.count())

	plt.figure(figsize=(13, 8))
	###########
	plt.subplot2grid((3, 4), (0, 0))
	data.Survived.value_counts(normalize=True).sort_index().plot(kind='bar', color='yellow')

	plt.subplot2grid((3, 4), (0, 1))
	data.Pclass.value_counts(normalize=True).sort_index().plot(kind='bar', color='brown')

	plt.subplot2grid((3, 4), (0, 2))
	data.Sex.value_counts(normalize=True).sort_index().plot(kind='bar', color='purple')

	plt.subplot2grid((3, 4), (1, 0))
	data.Survived[data.Sex == 'male'].value_counts(normalize=True).sort_index().plot(kind='bar', color='blue')

	plt.subplot2grid((3, 4), (1, 1))
	data.Survived[data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar', color='gray')

	plt.subplot2grid((3, 4), (1, 2))
	data.Survived[data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar', color='gray')

	plt.subplot2grid((3, 4), (2, 0))
	data.Survived[data.Sex == 'male'][data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar', color='blue')

	plt.subplot2grid((3, 4), (2, 1))
	data.Survived[data.Sex == 'male'][data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar', color='blue')

	plt.subplot2grid((3, 4), (2, 2))
	data.Survived[data.Sex == 'female'][data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar', color='red')

	plt.subplot2grid((3, 4), (2, 3))
	data.Survived[data.Sex == 'female'][data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar', color='red')

	###########
	plt.show()
# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
