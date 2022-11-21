import matplotlib
import wordcloud
import num2words
from collections import Counter
from random import randint

from faker import Faker
from matplotlib import pyplot as plt
from num2words import num2words
from wordcloud import WordCloud

# Criando arquivo com nomes e pontuações falsas.
falso = Faker('pt_BR')
Faker.seed(0)
with open("Nomes_Falsos.txt", "w") as arquivo:
    for c in range(85):
        name_falso = falso.name()
        pont_falso = falso.pyint(1, 90)
        arquivo.write(f"Nome: {name_falso} - Pontos = {pont_falso}\n")
arquivo.close()

# Manipulando arquivo criado.
name_cadidatos = []
pont_cadidatos = []
arquivo = open("Nomes_Falsos.txt", "r+")
for linha in arquivo:
    linha = linha.split('=')
    name_cadidatos.append(linha[0])
    pont_cadidatos.append(int(linha[1]))
name_cadidatos.pop(0)
pont_cadidatos.pop(0)

string_pont = []
for _ in pont_cadidatos:
    palavra = num2words(_, lang='pt')
    string_pont.append(palavra)

# Histograma.
n, bins, colunas = plt.hist(pont_cadidatos, density=True,
                            facecolor='#6495ED', alpha=0.75)
num_bins = 25
plt.hist(pont_cadidatos, num_bins, density=True,
         facecolor='#6959CD', alpha=0.80)
plt.xlabel('Pontos', c = 'r')
plt.ylabel('Probabilidade%', c = 'r')
plt.title('Histograma Completo', c = 'b')
plt.show()

# Nuvem de Palavras.
pont_palavras = Counter(string_pont)
wordcloud = WordCloud(width=800,
                      height=600).generate_from_frequencies(pont_palavras)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
wordcloud.to_file("Fake_word_cloud.png")