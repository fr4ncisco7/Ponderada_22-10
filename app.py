import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# 1. Dados Fornecidos (Apenas uma vez)
dados_str = """
6 3.63 1.37
3618 3.48 1.52
4021 3.34 1.66
4423 3.21 1.79
4825 3.08 1.92
5227 2.97 2.03
5629 2.85 2.15
6032 2.74 2.26
6434 2.63 2.37
6836 2.52 2.48
7238 2.42 2.58
7641 2.33 2.67
8043 2.24 2.76
8445 2.15 2.85
8847 2.06 2.94
9249 1.98 3.02
9652 1.91 3.09
10054 1.83 3.17
10457 1.76 3.24
10859 1.69 3.31
11260 1.62 3.38
11663 1.56 3.44
12065 1.50 3.50
12468 1.44 3.56
12870 1.38 3.62
13273 1.32 3.68
13675 1.28 3.72
14077 1.22 3.78
14480 1.17 3.83
14882 1.13 3.87
15285 1.09 3.91
15686 1.04 3.96
16089 1.00 4.00
16491 0.96 4.04
16893 0.92 4.08
17296 0.88 4.12
17698 0.85 4.15
18101 0.82 4.18
18503 0.79 4.21
18906 0.75 4.25
19308 0.72 4.28
19709 0.70 4.30
20112 0.67 4.33
20514 0.65 4.35
20917 0.62 4.38
21319 0.59 4.41
21722 0.57 4.43
22124 0.55 4.45
22526 0.53 4.47
22929 0.50 4.50
23331 0.48 4.52
23733 0.46 4.54
24135 0.45 4.55
24538 0.43 4.57
24940 0.42 4.58
25342 0.40 4.60
25745 0.38 4.62
26147 0.37 4.63
26550 0.35 4.65
26952 0.34 4.66
"""

# 2. Carregar os dados (Renomeando para facilitar a referência na plotagem)
df = pd.read_csv(
    StringIO(dados_str),
    sep='\s+',
    header=None,
    names=['Tempo', 'Tensao_Descarga_R', 'Tensao_Carga_C']
)

# =========================================================
# GRÁFICO 1: Carga no Capacitor (Requisito 1)
# =========================================================
plt.figure(figsize=(10, 5))
plt.plot(
    df['Tempo'],
    df['Tensao_Carga_C'],
    label='Tensão no Capacitor ($V_C$)',
    color='green',
    linewidth=2
)
plt.title('1) Gráfico da Tensão de Carga no Capacitor', fontsize=16)
plt.xlabel('Tempo (Unidade Arbitrária)', fontsize=12)
plt.ylabel('Tensão ($V$)', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()


# =========================================================
# GRÁFICO 2: Descarga no Resistor (Requisito 2)
# =========================================================
plt.figure(figsize=(10, 5))
plt.plot(
    df['Tempo'],
    df['Tensao_Descarga_R'],
    label='Tensão no Resistor ($V_R$)',
    color='orange',
    linewidth=2
)
plt.title('2) Gráfico da Tensão no Resistor durante a Descarga', fontsize=16)
plt.xlabel('Tempo (Unidade Arbitrária)', fontsize=12)
plt.ylabel('Tensão ($V$)', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()


# =========================================================
# GRÁFICO 3: Comparação (Requisito 3)
# =========================================================
plt.figure(figsize=(12, 6))

# Carga no C (Crescente)
plt.plot(
    df['Tempo'],
    df['Tensao_Carga_C'],
    label='Tensão de Carga no Capacitor ($V_C$)',
    linestyle='-',
    linewidth=2,
    color='green'
)

# Descarga no R (Decrescente)
plt.plot(
    df['Tempo'],
    df['Tensao_Descarga_R'],
    label='Tensão no Resistor durante a Descarga ($V_R$)',
    linestyle='--',
    linewidth=2,
    color='orange'
)

plt.title('3) Comparação: Carga no Capacitor vs. Descarga no Resistor', fontsize=16)
plt.xlabel('Tempo (Unidade Arbitrária)', fontsize=14)
plt.ylabel('Tensão ($V$)', fontsize=14)
plt.legend(fontsize=12, loc='center right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()