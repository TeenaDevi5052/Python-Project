import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
phenotic={row.letter:row.code for (index,row) in data.iterrows()}


word=input('Enter a word: ').upper()
output=[phenotic[item] for item in word]
print(output)