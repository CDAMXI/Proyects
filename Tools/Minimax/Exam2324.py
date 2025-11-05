# -*- coding: utf-8 -*-
# Traza de Minimax vs Alpha-Beta para el árbol de la imagen (left-to-right)

from dataclasses import dataclass
from typing import List, Optional, Tuple, Dict, Set

@dataclass
class Node:
    name: str
    kind: str                 # "MAX", "MIN" o "LEAF"
    value: Optional[int] = None
    children: Optional[List["Node"]] = None

def L(name, v):  # hoja
    return Node(name=name, kind="LEAF", value=v, children=[])

def MAX(name, childs):
    return Node(name=name, kind="MAX", children=childs)

def MIN(name, childs):
    return Node(name=name, kind="MIN", children=childs)

# ---------- Construcción EXACTA del árbol de la imagen ----------
# Raíz MAX con 4 hijos MIN (izq→der): A, B, C, D
# A: MAXs -> [ (5,6), (3), (4,5) ]
A = MIN("A", [
    MAX("A1", [L("A1a", 5), L("A1b", 6)]),
    MAX("A2", [L("A2a", 3)]),
    MAX("A3", [L("A3a", 4), L("A3b", 5)]),
])

# B: MAXs -> [ (1), (0,8) ]
B = MIN("B", [
    MAX("B1", [L("B1a", 1)]),
    MAX("B2", [L("B2a", 0), L("B2b", 8)]),
])

# C: MAXs -> [ (3), (1,2), (5) ]
C = MIN("C", [
    MAX("C1", [L("C1a", 3)]),
    MAX("C2", [L("C2a", 1), L("C2b", 2)]),
    MAX("C3", [L("C3a", 5)]),
])

# D: MAXs -> [ (5), (6,7) ]
D = MIN("D", [
    MAX("D1", [L("D1a", 5)]),
    MAX("D2", [L("D2a", 6), L("D2b", 7)]),
])

ROOT = MAX("ROOT", [A, B, C, D])
# ----------------------------------------------------------------

# Utilidades de traza y conteo
class Trace:
    def __init__(self):
        self.lines: List[str] = []
        self.generated_minimax: List[str] = []
        self.generated_ab: List[str] = []
        self._indent = 0

    def add(self, s: str):
        self.lines.append("  " * self._indent + s)

    def indent(self):   self._indent += 1
    def dedent(self):   self._indent = max(0, self._indent - 1)

# -------- Minimax (para baseline de “nodos generados”) ----------
def minimax(n: Node, tr: Trace) -> int:
    tr.generated_minimax.append(n.name)
    if n.kind == "LEAF":
        tr.add(f"LEAF {n.name} = {n.value}")
        return n.value
    if n.kind == "MAX":
        tr.add(f"MAX {n.name} ⬇")
        tr.indent()
        best = -10**9
        for c in n.children:
            v = minimax(c, tr)
            best = max(best, v)
            tr.add(f"MAX {n.name} ← max = {best}")
        tr.dedent()
        return best
    else:  # MIN
        tr.add(f"MIN {n.name} ⬇")
        tr.indent()
        best = 10**9
        for c in n.children:
            v = minimax(c, tr)
            best = min(best, v)
            tr.add(f"MIN {n.name} ← min = {best}")
        tr.dedent()
        return best

# -------- Alpha-Beta con traza detallada y conteos --------------
def alphabeta(n: Node, alpha: int, beta: int, tr: Trace) -> int:
    tr.generated_ab.append(n.name)
    if n.kind == "LEAF":
        tr.add(f"LEAF {n.name} = {n.value}")
        return n.value

    if n.kind == "MAX":
        tr.add(f"MAX {n.name} (α={alpha}, β={beta}) ⬇")
        tr.indent()
        v = -10**9
        for c in n.children:
            tr.add(f"→ hijo {c.name}")
            tr.indent()
            v = max(v, alphabeta(c, alpha, beta, tr))
            tr.dedent()
            tr.add(f"{n.name}: v={v}")
            alpha = max(alpha, v)
            tr.add(f"{n.name}: α←{alpha}, β={beta}")
            if alpha >= beta:
                tr.add(f"✂ corte β en {n.name} (α≥β)")
                # No se generan más hijos de este MAX
                break
        tr.dedent()
        return v

    else:  # MIN
        tr.add(f"MIN {n.name} (α={alpha}, β={beta}) ⬇")
        tr.indent()
        v = 10**9
        for c in n.children:
            tr.add(f"→ hijo {c.name}")
            tr.indent()
            v = min(v, alphabeta(c, alpha, beta, tr))
            tr.dedent()
            tr.add(f"{n.name}: v={v}")
            beta = min(beta, v)
            tr.add(f"{n.name}: α={alpha}, β←{beta}")
            if beta <= alpha:
                tr.add(f"✂ corte α en {n.name} (β≤α)")
                # No se generan más hijos de este MIN
                break
        tr.dedent()
        return v

# ------------------ Ejecutar y mostrar resultados ----------------
if __name__ == "__main__":
    tr_mm = Trace()
    v_mm = minimax(ROOT, tr_mm)

    tr_ab = Trace()
    v_ab = alphabeta(ROOT, alpha=-10**9, beta=10**9, tr=tr_ab)

    # Conjuntos de nodos (internos y hojas) generados por cada uno
    mm_set = set(tr_mm.generated_minimax)
    ab_set = set(tr_ab.generated_ab)
    not_generated = mm_set - ab_set  # “evitados” gracias a poda

    print("="*70)
    print("TRAZA MINIMAX (sin podas)")
    print("-"*70)
    print("\n".join(tr_mm.lines))
    print(f"\nValor minimax raíz = {v_mm}")
    print(f"Nodos generados por Minimax: {len(mm_set)} → {sorted(mm_set)}")

    print("\n" + "="*70)
    print("TRAZA ALFA-BETA (left-to-right)")
    print("-"*70)
    print("\n".join(tr_ab.lines))
    print(f"\nValor alfa-beta raíz = {v_ab}")
    print(f"Nodos generados por Alfa-Beta: {len(ab_set)} → {sorted(ab_set)}")

    print("\n" + "="*70)
    print("RESUMEN")
    print("-"*70)
    print(f"Nodos que NO se generan con Alfa-Beta (vs Minimax): {len(not_generated)}")
    print(f"Lista de nodos evitados: {sorted(not_generated)}")
