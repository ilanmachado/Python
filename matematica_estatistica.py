import math
import statistics

# math.prod - retorna um produto de um container numérico
# nuns_v1 = [2, 3, 6, 8]
# nuns_v2 = (2, 3, 6, 8)
# nuns_v3 = {2, 3, 6, 8}
#
# print(math.prod(nuns_v1))
# print(math.prod(nuns_v2))
# print(math.prod(nuns_v3))


# math.isqrt -> retorna a parte inteira da raíz quadrada de um número

# print(math.isqrt(9))
# print(math.sqrt(9))
# print(math.isqrt(17))
# print(math.sqrt(17))

# math.dist - retorna a distância euclidiana entre dois pontos 2D e 3D

# Ponto 3D
pt3d1 = (12, 50, 40)
pt3d2 = (6, 7, 13)

# Ponto 2D
pt2d1 = [12, 50]
pt2d2 = [6, 7]

# print(math.dist(pt3d1, pt3d2))
# print(math.dist(pt2d1, pt2d2))

# math.hypot - retorna hipotenusa ou norma Euclidiana
# print(math.hypot(*pt3d1))
# print(math.hypot(*pt2d1))

# ESTATÍSTICA
import statistics

# statistics.fmean() -> calcula a média de números reais
# val_reais = [1.45, 6.789, 3.14, 89.98765]
# val_int = [1, 6, 3, 89]

# print(statistics.fmean(val_reais))
# print(statistics.fmean(val_int))

# statistics.geometric_mean() -> calcula a média geométrica de números reais
# print(statistics.geometric_mean(val_reais))
# print(statistics.geometric_mean(val_int))

# statistics.multimode() -> retorna o valor mais frequente em uma sequencia
seq1 = 'Ilan Machado'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
