import random
import pandas as pd

word_list = pd.read_csv('csv/omime_db.csv')
word = random.choice(word_list['product_type'])
print('Você vai ter que fazer um(a): {}!'.format(word))
