# 4. Crie dois sets e atribua no primeiro a diferença simétrica entre os dois.

set1 = {1,2,3,4,5,6,7, 'cachorro'}
set2 = {2,5,20,4,95,2,9,77,33,12, 'cachorro', 'gato', 'cavalo'}
set1.symmetric_difference_update(set2)
print(set1)