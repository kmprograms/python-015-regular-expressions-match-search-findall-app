import re
# Paczka re pozwala w Python stosować kilka przydatnych funkcji do pracy z wyrażeniami regularnymi.

# -> re.match()
# -> re.search()
# -> re.findall()

# re.match() wyszukuje dopasowań do wzorca na początku napisu, podczas gdy re.search() wyszukuje dopasowań
# do wzorca w całym napisie.
# Obydwie funkcje zwracają pierwsze wystąpienie wzorca.

print("----------------------------------- 1 ----------------------------------")
s1 = 'Hello kmprograms in 2021'
print(re.match(r'\d+', s1))
result = re.search(r'\d+', s1)
print(result)
print(result.group())
print(result.start())
print(result.end())
print(result.span())

print("----------------------------------- 2 ----------------------------------")
s2 = '2021 - hello kmprograms'
print(re.match(r'\d+', s2))
print(re.search(r'\d+', s2))

print("----------------------------------- 3 ----------------------------------")
s3 = '''2021 - kmprograms
2022 - kmprograms'''
print(re.match(r'\d+', s3))
print(re.search(r'\d+', s3))

print("----------------------------------- 4 ----------------------------------")
s4 = '''kmprograms 2021
2022 - kmprograms'''
print(re.match(r'\d+', s4))
print(re.search(r'\d+', s4))

print("----------------------------------- 5 ----------------------------------")
s5 = '''kmprograms
2022 - kmprograms'''
print(re.match(r'\d+', s5))
print(re.search(r'\d+', s5))

print("----------------------------------- 6 ----------------------------------")
s6 = '''kmprograms
kmprograms - 2022'''
print(re.match(r'\d+', s6))
print(re.search(r'\d+', s6))

print("----------------------------------- 7 ----------------------------------")
# re.findall() pozwala znaleźć wszystkie wystąpienia w napisie które pasują do podanego wzorca
s7 = '''kmprograms - 2021
kmprograms - 2022'''
print(re.findall(r'\d+', s7))