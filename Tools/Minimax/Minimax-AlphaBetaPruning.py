# minimax_alphabeta_vivo.py
# Creado para entender y visualizar Minimax con poda alfa-beta sobre
# el MISMO árbol del enunciado (izquierda→derecha).
# Colores:
#  - Amarillo: nodo en evaluación (paso actual)
#  - Verde: evaluado y USADO (ruta óptima)
#  - Rojo: evaluado y NO USADO
#  - Gris claro: pendiente (aún no evaluado)
#  - Gris oscuro (con hatch): PRUNED (poda alfa-beta)
#
# Avanza automáticamente cada 5 s.

import time
import math
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Tuple

# -------------------- Modelo de árbol --------------------
@dataclass
class Node:
    kind: str  # 'MAX', 'MIN' o 'LEAF'
    value: Optional[int] = None
    children: List["Node"] = field(default_factory=list)
    name: Optional[str] = None  # id único (para estado/posiciones)

# Utilidad para crear hoja con nombre único (texto mostrado = dígitos del nombre)
def L(name_with_suffix: str, v: int) -> Node:
    return Node("LEAF", v, name=name_with_suffix)

def MAX(name: str, childs: List[Node]) -> Node:
    return Node("MAX", children=childs, name=name)

def MIN(name: str, childs: List[Node]) -> Node:
    return Node("MIN", children=childs, name=name)

# ---------- Árbol EXACTO de la NUEVA imagen ----------
# Hojas (izq→der): 2,1,0,2,-1,  2,4,1,-2,2,  3,3,4,0,-1
# Raíz MAX con 3 hijos MIN (izq→der): MINL, MINM, MINR

# MIN izquierdo: (2,1), (0,2), (-1)
L1 = MAX("L1", [L("2a", 2), L("1a", 1)])
L2 = MAX("L2", [L("0a", 0), L("2b", 2)])
L3 = MAX("L3", [L("m1a", -1)])
MINL = MIN("MINL", [L1, L2, L3])

# MIN central: (2,4), (1), (-2,2)
M1 = MAX("M1", [L("2c", 2), L("4a", 4)])
M2 = MAX("M2", [L("1b", 1)])
M3 = MAX("M3", [L("m2a", -2), L("2d", 2)])
MINM = MIN("MINM", [M1, M2, M3])

# MIN derecho: (3), (3,4), (0,-1)
R1 = MAX("R1", [L("3a", 3)])
R2 = MAX("R2", [L("3b", 3), L("4b", 4)])
R3 = MAX("R3", [L("0b", 0), L("m3a", -1)])
MINR = MIN("MINR", [R1, R2, R3])

ROOT = MAX("ROOT", [MINL, MINM, MINR])
# ------------------------------------------------------

# -------------------- Layout para dibujar parecido a la imagen --------------------
# Coordenadas “manuales” para que se parezca a la figura.
POS = {
    # Niveles: y=3 (ROOT), y=2 (MIN), y=1 (MAX), y=0 (LEAF)
    "ROOT": (0.0, 3.0),

    "MINL": (-6.0, 2.0),
    "MINM": ( 0.0, 2.0),
    "MINR": ( 6.0, 2.0),

    "L1": (-7.7, 1.0), "L2": (-6.0, 1.0), "L3": (-4.3, 1.0),
    "M1": (-1.7, 1.0), "M2": ( 0.0, 1.0), "M3": ( 1.7, 1.0),
    "R1": ( 4.3, 1.0), "R2": ( 6.0, 1.0), "R3": ( 7.7, 1.0),

    # Hojas (bajo cada MAX)
    "2a": (-8.3, 0.0), "1a": (-7.1, 0.0),
    "0a": (-6.6, 0.0), "2b": (-5.4, 0.0),
    "m1a": (-4.3, 0.0),

    "2c": (-2.3, 0.0), "4a": (-1.1, 0.0),
    "1b": ( 0.0, 0.0),
    "m2a": ( 1.1, 0.0), "2d": ( 2.3, 0.0),

    "3a": ( 4.3, 0.0),
    "3b": ( 5.7, 0.0), "4b": ( 6.3, 0.0),
    "0b": ( 7.4, 0.0), "m3a": ( 8.0, 0.0),
}

EDGES = [
    ("ROOT","MINL"), ("ROOT","MINM"), ("ROOT","MINR"),

    ("MINL","L1"), ("MINL","L2"), ("MINL","L3"),
    ("L1","2a"), ("L1","1a"),
    ("L2","0a"), ("L2","2b"),
    ("L3","m1a"),

    ("MINM","M1"), ("MINM","M2"), ("MINM","M3"),
    ("M1","2c"), ("M1","4a"),
    ("M2","1b"),
    ("M3","m2a"), ("M3","2d"),

    ("MINR","R1"), ("MINR","R2"), ("MINR","R3"),
    ("R1","3a"),
    ("R2","3b"), ("R2","4b"),
    ("R3","0b"), ("R3","m3a"),
]

# -------------------- Estado de visualización --------------------
# status: 'pending' | 'current' | 'used' | 'unused' | 'pruned'
node_status: Dict[str, str] = {k: "pending" for k in POS}
node_value: Dict[str, Optional[int]] = {k: None for k in POS}
node_alpha: Dict[str, Optional[float]] = {k: None for k in POS}
node_beta:  Dict[str, Optional[float]] = {k: None for k in POS}
visit_order: Dict[str, int] = {}
visit_counter = 0

# -------------------- Utilidades de dibujo --------------------
def _leaf_label(name: str) -> str:
    # Muestra sólo los dígitos del nombre interno (p.ej. "2a" -> "2")
    digits = "".join(ch for ch in name if ch.isdigit() or ch == "-")
    return digits if digits else name

def draw_scene(ax, focus: Optional[str] = None, title: str = ""):
    ax.clear()
    # Aristas
    for a, b in EDGES:
        xa, ya = POS[a]; xb, yb = POS[b]
        ax.plot([xa, xb], [ya, yb])

    # Nodos
    for name, (x, y) in POS.items():
        st = node_status.get(name, "pending")
        hatch = None
        if st == "current":
            fc = "yellow"
        elif st == "used":
            fc = "green"
        elif st == "unused":
            fc = "red"
        elif st == "pruned":
            fc = "darkgray"; hatch = "//"
        else:
            fc = "lightgray"

        circle = plt.Circle((x, y), 0.28, edgecolor="black", facecolor=fc, lw=1.5, hatch=hatch)
        ax.add_patch(circle)

        # Texto interno
        internal_nodes = {"ROOT","MINL","MINM","MINR","L1","L2","L3","M1","M2","M3","R1","R2","R3"}
        if name in internal_nodes:
            label_top = "MAX" if name in {"L1","L2","L3","M1","M2","M3","R1","R2","R3"} else ("MIN" if name.startswith("MIN") else "")
            val = node_value.get(name)
            a = node_alpha.get(name); b = node_beta.get(name)
            ab = ""
            if a is not None or b is not None:
                a_txt = "-∞" if a is None or a == -math.inf else str(int(a))
                b_txt = "∞"  if b is None or b ==  math.inf else str(int(b))
                ab = f"\nα={a_txt} β={b_txt}"
            text = f"{label_top}\n{'' if val is None else val}{ab}"
        else:
            order = visit_order.get(name)
            base = _leaf_label(name)
            text = f"{base}\n#{order}" if order else base

        ax.text(x, y, text, ha="center", va="center", fontsize=10)

    ax.set_xlim(-9.2, 9.0)
    ax.set_ylim(-1.0, 3.6)
    ax.axis("off")
    ax.set_title(title, fontsize=12)

def step_pause(fig, ax, focus: Optional[str], title: str):
    draw_scene(ax, focus, title)
    fig.canvas.draw()
    plt.pause(0.001)

def mark_subtree(node: Node, status: str):
    stack = [node]
    while stack:
        n = stack.pop()
        node_status[n.name] = status
        for c in n.children:
            stack.append(c)

# -------------------- Alfa-Beta con traza --------------------
def alphabeta_trace(node: Node, fig, ax, alpha: float, beta: float, depth: int = 0) -> int:
    global visit_counter

    node_status[node.name] = "current"
    node_alpha[node.name] = alpha
    node_beta[node.name]  = beta
    step_pause(fig, ax, node.name, f"Evaluando {node.name} ({node.kind}) con α={alpha if alpha!=-math.inf else '-∞'}, β={beta if beta!=math.inf else '∞'}")

    if node.kind == "LEAF":
        visit_counter += 1
        visit_order[node.name] = visit_counter
        node_value[node.name] = node.value
        step_pause(fig, ax, node.name, f"Hoja {node.name} = {node.value}  (orden #{visit_counter})")
        return node.value

    vals: List[Tuple[Node, int]] = []
    if node.kind == "MAX":
        value = -math.inf
        for i, child in enumerate(node.children):
            v = alphabeta_trace(child, fig, ax, alpha, beta, depth + 1)
            vals.append((child, v))
            value = max(value, v)
            alpha = max(alpha, value)
            node_value[node.name] = value
            node_alpha[node.name] = alpha
            node_beta[node.name]  = beta
            step_pause(fig, ax, node.name, f"MAX parcial en {node.name}: {value}  (α={alpha if alpha!=-math.inf else '-∞'}, β={beta if beta!=math.inf else '∞'})")
            if alpha >= beta and i < len(node.children) - 1:
                for rest in node.children[i+1:]:
                    mark_subtree(rest, "pruned")
                step_pause(fig, ax, node.name, f"PODA en {node.name} porque α≥β ({alpha}≥{beta})")
                break
    else:  # MIN
        value = math.inf
        for i, child in enumerate(node.children):
            v = alphabeta_trace(child, fig, ax, alpha, beta, depth + 1)
            vals.append((child, v))
            value = min(value, v)
            beta = min(beta, value)
            node_value[node.name] = value
            node_alpha[node.name] = alpha
            node_beta[node.name]  = beta
            step_pause(fig, ax, node.name, f"MIN parcial en {node.name}: {value}  (α={alpha if alpha!=-math.inf else '-∞'}, β={beta if beta!=math.inf else '∞'})")
            if alpha >= beta and i < len(node.children) - 1:
                for rest in node.children[i+1:]:
                    mark_subtree(rest, "pruned")
                step_pause(fig, ax, node.name, f"PODA en {node.name} porque α≥β ({alpha}≥{beta})")
                break

    # Determinar hijos óptimos entre los realmente evaluados (no podados)
    evaluated = [(c, v) for (c, v) in vals]
    if node.kind == "MAX":
        best_val = max(v for _, v in evaluated)
        best_children = [c for c, v in evaluated if v == best_val]
    else:
        best_val = min(v for _, v in evaluated)
        best_children = [c for c, v in evaluated if v == best_val]

    node_value[node.name] = best_val

    # Marcar usados/unused entre los evaluados
    used_set = set(n.name for n in best_children)
    for c, _ in evaluated:
        if node_status.get(c.name) == "pruned":
            continue
        if c.name in used_set:
            mark_subtree(c, "used")
        else:
            mark_subtree(c, "unused")

    node_status[node.name] = "used"
    step_pause(fig, ax, node.name, f"{node.kind} decide en {node.name}: {best_val}  (α={alpha if alpha!=-math.inf else '-∞'}, β={beta if beta!=math.inf else '∞'})")
    return best_val

# -------------------- Ejecutar visualización --------------------
if __name__ == "__main__":
    plt.ion()
    fig, ax = plt.subplots(figsize=(12, 6))
    draw_scene(ax, None, "Minimax con poda alfa-beta: preparación")
    fig.canvas.draw()
    plt.pause(0.001)

    final_v = alphabeta_trace(ROOT, fig, ax, -math.inf, math.inf)

    # Propagar marcado final desde la raíz entre sus hijos no podados
    children_vals = []
    for ch in ROOT.children:
        if node_status.get(ch.name) == "pruned":
            continue
        children_vals.append((ch, node_value[ch.name]))

    best = max(v for _, v in children_vals)  # raíz es MAX
    for ch, v in children_vals:
        if v == best:
            mark_subtree(ch, "used")
        else:
            mark_subtree(ch, "unused")

    node_status["ROOT"] = "used"
    node_value["ROOT"] = final_v

    step_pause(fig, ax, "ROOT", f"Final: V={final_v} en ROOT (αβ)")

    plt.ioff()
    draw_scene(ax, None, f"Resultado final (αβ): V={final_v}")
    plt.show()
