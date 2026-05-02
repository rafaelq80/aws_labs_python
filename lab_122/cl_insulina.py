# Sequência completa do pré-pró-insulina humana (inclui peptídeo sinal,
# cadeia B, peptídeo C e cadeia A)
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Fragmentos individuais que compõem a pré-pró-insulina:
# lsInsulin: peptídeo sinal (leader sequence) — direcionamento ao retículo endoplasmático
lsInsulin = "malwmrllpllallalwgpdpaaa"
# bInsulin: cadeia B da insulina madura
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
# aInsulin: cadeia A da insulina madura
aInsulin = "giveqcctsicslyqlenycn"
# cInsulin: peptídeo C — removido durante a maturação da insulina no pâncreas
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Insulina madura = cadeia B + cadeia A (sem peptídeo sinal nem peptídeo C)
insulin = bInsulin + aInsulin

# pH inicial para o cálculo; pode ser iterado de 0 a 14 para encontrar o pI
pH = 0

# Dicionário de valores de pKa para as cadeias laterais dos 7 aminoácidos
# ionizáveis que influenciam a carga líquida da proteína:
#   Positivos em pH baixo: h (histidina), k (lisina), r (arginina)
#   Negativos em pH alto:  y (tirosina), c (cisteína), d (asp. ácido), e (glu. ácido)
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53,
       'h': 6.00,  'r': 12.48, 'd': 3.65, 'e': 4.25}

# Conta quantas vezes cada aminoácido ionizável aparece na sequência da insulina.
# O método count() percorre a string e retorna o número de ocorrências do caractere.
# float() converte o inteiro resultante para ponto flutuante, necessário para a
# fórmula de Henderson-Hasselbalch a seguir.
# Resultado: dicionário no formato {'y': 4.0, 'c': 6.0, 'k': 1.0, ...}
seqCount = {x: float(insulin.count(x))
            for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}

print("Contagem de aminoácidos ionizáveis:", seqCount)

# Cálculo da carga líquida usando a equação de Henderson-Hasselbalch:
#
#   Grupos básicos (K, H, R) — contribuem com carga POSITIVA:
#       carga = count × 10^pKa / (10^pH + 10^pKa)
#
#   Grupos ácidos (Y, C, D, E) — contribuem com carga NEGATIVA:
#       carga = count × 10^pH / (10^pH + 10^pKa)
#
#   Carga líquida = Σ(positivas) − Σ(negativas)
#
# Quando pH = pI (ponto isoelétrico), a carga líquida é zero.
netCharge = (
    # Soma das contribuições positivas (K, H, R)
    + sum((seqCount[x] * (10**pKR[x])) / ((10**pH) + (10**pKR[x]))
          for x in ['k', 'h', 'r'])
    # Subtrai a soma das contribuições negativas (Y, C, D, E)
    - sum((seqCount[x] * (10**pH)) / ((10**pH) + (10**pKR[x]))
          for x in ['y', 'c', 'd', 'e'])
)

print(f"Carga líquida em pH {pH}: {netCharge:.4f}")