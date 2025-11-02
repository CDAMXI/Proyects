# minimax_alphabeta_vivo.py
#Creado usando ChatGPT para entender y visualizar el algoritmo Minimax con poda alfa-beta.
# Traza visual de Minimax con Poda Alfa-Beta sobre el mismo grafo del enunciado.
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
    name: Optional[str] = None

# Árbol exacto del enunciado
# Lado izquierdo
leaf_4  = Node("LEAF", 4,  name="4")
leaf_8  = Node("LEAF", 8,  name="8")
leaf_9L = Node("LEAF", 9,  name="9L")
leaf_3  = Node("LEAF", 3,  name="3")
max_A   = Node("MAX", children=[leaf_4, leaf_8], name="MAX_A")
max_B   = Node("MAX", children=[leaf_9L, leaf_3], name="MAX_B")
min_L   = Node("MIN", children=[max_A, max_B],   name="MIN_L")
# Lado derecho
leaf_2  = Node("LEAF", 2,  name="2")
leaf_m2 = Node("LEAF", -2, name="-2")
leaf_9R = Node("LEAF", 9,  name="9R")
leaf_m1 = Node("LEAF", -1, name="-1")
max_C   = Node("MAX", children=[leaf_2, leaf_m2], name="MAX_C")
max_D   = Node("MAX", children=[leaf_9R, leaf_m1], name="MAX_D")
min_R   = Node("MIN", children=[max_C, max_D],     name="MIN_R")
root    = Node("MAX", children=[min_L, min_R], name="ROOT")

# -------------------- Layout para dibujar parecido a la pizarra --------------------
POS = {
    "ROOT":   (0, 3),
    "MIN_L":  (-2, 2),
    "MIN_R":  ( 2, 2),
    "MAX_A":  (-3, 1),
    "MAX_B":  (-1, 1),
    "MAX_C":  ( 1, 1),
    "MAX_D":  ( 3, 1),
    "4":   (-3.5, 0),
    "8":   (-2.5, 0),
    "9L":  (-1.5, 0),
    "3":   (-0.5, 0),
    "2":   ( 0.5, 0),
    "-2":  ( 1.5, 0),
    "9R":  ( 2.5, 0),
    "-1":  ( 3.5, 0),
}
EDGES = [
    ("ROOT", "MIN_L"), ("ROOT", "MIN_R"),
    ("MIN_L", "MAX_A"), ("MIN_L", "MAX_B"),
    ("MIN_R", "MAX_C"), ("MIN_R", "MAX_D"),
    ("MAX_A", "4"), ("MAX_A", "8"),
    ("MAX_B", "9L"), ("MAX_B", "3"),
    ("MAX_C", "2"), ("MAX_C", "-2"),
    ("MAX_D", "9R"), ("MAX_D", "-1"),
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
def draw_scene(ax, focus: Optional[str] = None, title: str = ""):
    ax.clear()
    # Aristas
    for a, b in EDGES:
        xa, ya = POS[a]
        xb, yb = POS[b]
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
            fc = "darkgray"
            hatch = "//"
        else:
            fc = "lightgray"

        circle = plt.Circle((x, y), 0.28, edgecolor="black", facecolor=fc, lw=1.5, hatch=hatch)
        ax.add_patch(circle)

        # Texto interno: tipo, valor y α/β si aplica
        label_top = ""
        if name == "ROOT":
            label_top = "MAX"
        elif name.startswith("MIN"):
            label_top = "MIN"
        elif name.startswith("MAX"):
            label_top = "MAX"

        val = node_value.get(name)
        a = node_alpha.get(name)
        b = node_beta.get(name)
        if name in ["ROOT","MIN_L","MIN_R","MAX_A","MAX_B","MAX_C","MAX_D"]:
            # α/β compactos
            ab = ""
            if a is not None or b is not None:
                a_txt = "-∞" if a is None or a == -math.inf else str(int(a))
                b_txt = "∞"  if b is None or b ==  math.inf else str(int(b))
                ab = f"\nα={a_txt} β={b_txt}"
            text = f"{label_top}\n{'' if val is None else val}{ab}"
        else:
            # Hojas: valor y orden de visita
            order = visit_order.get(name)
            base = name  # su nombre ya es el valor textual
            text = f"{base}\n#{order}" if order else base

        ax.text(x, y, text, ha="center", va="center", fontsize=10)

    ax.set_xlim(-4.4, 4.4)
    ax.set_ylim(-1.0, 3.5)
    ax.axis("off")
    ax.set_title(title, fontsize=12)

def step_pause(fig, ax, focus: Optional[str], title: str):
    draw_scene(ax, focus, title)
    fig.canvas.draw()
    plt.pause(0.001)
    time.sleep(5)  # avanza automáticamente cada 5s

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
            # Poda
            if alpha >= beta and i < len(node.children) - 1:
                # Podar subárboles restantes
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
            # Poda
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

    # El propio nodo se deja como 'used' provisional (su padre decidirá)
    node_status[node.name] = "used"
    step_pause(fig, ax, node.name, f"{node.kind} decide en {node.name}: {best_val}  (α={alpha if alpha!=-math.inf else '-∞'}, β={beta if beta!=math.inf else '∞'})")
    return best_val

# -------------------- Ejecutar visualización --------------------
if __name__ == "__main__":
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))
    draw_scene(ax, None, "Minimax con poda alfa-beta: preparación")
    fig.canvas.draw()
    plt.pause(0.001)
    time.sleep(2)

    final_v = alphabeta_trace(root, fig, ax, -math.inf, math.inf)

    # Propagar marcado final desde la raíz entre sus hijos que no fueron podados
    children_vals = []
    for ch in root.children:
        if node_status.get(ch.name) == "pruned":
            continue
        children_vals.append((ch, node_value[ch.name]))

    if root.kind == "MAX":
        best = max(v for _, v in children_vals)
    else:
        best = min(v for _, v in children_vals)

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
