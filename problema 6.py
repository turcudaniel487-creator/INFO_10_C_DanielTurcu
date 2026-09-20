n = 99999
ultima_cifra = n % 10
penultima_cifra = (n // 10) % 10
cat_9 = n // 9
rest_9 = n % 9
suma_cifrelor_n = ultima_cifra + penultima_cifra + (n // 100) % 10 + (n // 1000) % 10 + (n // 10000) % 10
rasturnatul_n = n // 10000 + (n // 1000) % 10 * 10 + (n // 100) % 10 * 100 + (n // 10) % 10 * 1000 + n % 10 * 10000
print(ultima_cifra, penultima_cifra, cat_9, rest_9, suma_cifrelor_n, rasturnatul_n, sep="\n")