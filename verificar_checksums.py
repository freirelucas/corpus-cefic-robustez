"""Confere os hashes das saidas publicadas contra CHECKSUMS.sha256."""
import hashlib
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
VOLATEIS = {"dados/numeros_verificados.json"}  # regravado por reproduzir.py

falhas = []
for linha in (BASE / "CHECKSUMS.sha256").read_text(encoding="utf-8").splitlines():
    if not linha.strip():
        continue
    esperado, caminho = linha.split("  ", 1)
    alvo = BASE / caminho
    if not alvo.exists():
        falhas.append(f"ausente: {caminho}")
        continue
    obtido = hashlib.sha256(alvo.read_bytes()).hexdigest()
    if obtido != esperado and caminho not in VOLATEIS:
        falhas.append(f"divergente: {caminho}")

if falhas:
    print("FALHOU:")
    for f in falhas:
        print("  -", f)
    sys.exit(1)
print(f"Integridade confirmada em {len((BASE / 'CHECKSUMS.sha256').read_text(encoding='utf-8').strip().splitlines())} arquivos.")
