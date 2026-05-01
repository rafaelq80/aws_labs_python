import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
txt_path = os.path.join(script_dir, 'preproinsulin-seq.txt')

# 1. Ler e limpar o arquivo
with open(txt_path, "r") as f:
    raw = f.read()

# Remove ORIGIN, números, //, espaços e quebras de linha
cleaned = re.sub(r'ORIGIN|//|\d+|\s+', '', raw).lower()

# 2-4. Salvar e verificar preproinsulin-seq-clean.txt
with open(os.path.join(script_dir, "preproinsulin-seq-clean.txt"), "w") as f:
    f.write(cleaned)

print(f"preproinsulin-seq-clean.txt: {len(cleaned)} chars → {'✓ OK' if len(cleaned) == 110 else '✗ ERRO'}")
print(f"  Sequência: {cleaned}\n")

# 5-6. lsinsulin (aminoácidos 1-24)
ls = cleaned[0:24]
with open(os.path.join(script_dir, "lsinsulin-seq-clean.txt"), "w") as f:
    f.write(ls)
print(f"lsinsulin-seq-clean.txt:    {len(ls)} chars → {'✓ OK' if len(ls) == 24 else '✗ ERRO'}")
print(f"  Sequência: {ls}\n")

# 7-8. binsulin (aminoácidos 25-54)
bs = cleaned[24:54]
with open(os.path.join(script_dir, "binsulin-seq-clean.txt"), "w") as f:
    f.write(bs)
print(f"binsulin-seq-clean.txt:     {len(bs)} chars → {'✓ OK' if len(bs) == 30 else '✗ ERRO'}")
print(f"  Sequência: {bs}\n")

# 9-10. cinsulin (aminoácidos 55-89)
cs = cleaned[54:89]
with open(os.path.join(script_dir, "cinsulin-seq-clean.txt"), "w") as f:
    f.write(cs)
print(f"cinsulin-seq-clean.txt:     {len(cs)} chars → {'✓ OK' if len(cs) == 35 else '✗ ERRO'}")
print(f"  Sequência: {cs}\n")

# 11-12. ainsulin (aminoácidos 90-110)
as_ = cleaned[89:110]
with open(os.path.join(script_dir, "ainsulin-seq-clean.txt"), "w") as f:
    f.write(as_)
print(f"ainsulin-seq-clean.txt:     {len(as_)} chars → {'✓ OK' if len(as_) == 21 else '✗ ERRO'}")
print(f"  Sequência: {as_}\n")

print("Concluído! Todos os arquivos gerados.")