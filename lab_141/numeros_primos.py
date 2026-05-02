import os
import math

# Verifica se um número é primo.
# Um número é primo se for maior que 1 e não divisível por nenhum
# inteiro entre 2 e sua raiz quadrada.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Gera a lista de todos os números primos no intervalo [1, 250]
primes = [n for n in range(1, 251) if is_prime(n)]

# Exibe os primos no terminal
print(f"Números primos entre 1 e 250 ({len(primes)} encontrados):\n")
print(primes)

# Salva os resultados em results.txt no mesmo diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "results.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"Números primos entre 1 e 250 ({len(primes)} encontrados):\n\n")
    for prime in primes:
        f.write(f"{prime}\n")

print(f"\nResultados salvos em: {output_path}")