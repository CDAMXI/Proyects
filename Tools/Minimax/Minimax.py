# minimax_vivo_sin_poda.py
#Creado usando ChatGPT para entender y visualizar el algoritmo Minimax sin poda alfa-beta.
# Visualiza la traza de Minimax (sin alfa-beta) sobre el mismo grafo del enunciado.
# Colores:
#  - Amarillo: nodo en evaluación (paso actual)
#  - Verde: evaluado y USADO (queda en la ruta óptima desde la raíz)
#  - Rojo: evaluado y NO USADO (no queda en la ruta óptima)
#  - Gris: pendiente
#
# Avanza automáticamente cada 5 s.

import time
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
# status: 'pending' | 'current' | 'used' | 'unused'
node_status: Dict[str, str] = {k: "pending" for k in POS}
node_value: Dict[str, Optional[int]] = {k: None for k in POS}
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
        # Colores por estado
        if st == "current":
            fc = "yellow"
        elif st == "used":
            fc = "green"
        elif st == "unused":
            fc = "red"
        else:
            fc = "lightgray"

        circle = plt.Circle((x, y), 0.28, edgecolor="black", facecolor=fc, lw=1.5)
        ax.add_patch(circle)

        # Texto interno: tipo y valor si se conoce
        label_top = ""
        if name == "ROOT":
            label_top = "MAX"
        elif name.startswith("MIN"):
            label_top = "MIN"
        elif name.startswith("MAX"):
            label_top = "MAX"

        val = node_value.get(name)
        if name in ["ROOT","MIN_L","MIN_R","MAX_A","MAX_B","MAX_C","MAX_D"]:
            text = f"{label_top}\n{'' if val is None else val}"
        else:
            # Hojas: valor y orden de visita si existe
            order = visit_order.get(name)
            base = name  # el nombre ya es el valor textual
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
    # Avanza automáticamente cada 5 segundos
    time.sleep(1)

def mark_subtree(node: Node, status: str):
    # Marca un subárbol como 'used' o 'unused'
    stack = [node]
    while stack:
        n = stack.pop()
        node_status[n.name] = status
        for c in n.children:
            stack.append(c)

# -------------------- Minimax con generación de pasos --------------------
def minimax_trace(node: Node, fig, ax, depth: int = 0) -> int:
    global visit_counter

    # Foco en el nodo actual
    node_status[node.name] = "current"
    step_pause(fig, ax, node.name, f"Evaluando {node.name} ({node.kind})")

    if node.kind == "LEAF":
        visit_counter += 1
        visit_order[node.name] = visit_counter
        node_value[node.name] = node.value
        # Al terminar la hoja, sigue como evaluada. El color final (used/unused)
        # se decide cuando el ancestro elija la rama óptima.
        node_status[node.name] = "current"
        step_pause(fig, ax, node.name, f"Hoja {node.name} = {node.value}  (orden #{visit_counter})")
        return node.value

    # Nodo interno
    vals: List[Tuple[Node, int]] = []
    for child in node.children:
        v = minimax_trace(child, fig, ax, depth + 1)
        vals.append((child, v))
        # Mostrar parcial
        partial = (max(x[1] for x in vals) if node.kind == "MAX"
                   else min(x[1] for x in vals))
        node_value[node.name] = partial
        step_pause(fig, ax, node.name,
                   f"{node.kind} parcial en {node.name}: {partial}")

    # Decisión final del nodo
    if node.kind == "MAX":
        best_val = max(v for _, v in vals)
        best_children = [c for c, v in vals if v == best_val]
    else:
        best_val = min(v for _, v in vals)
        best_children = [c for c, v in vals if v == best_val]

    node_value[node.name] = best_val

    # Marcado de ramas: la(s) elegida(s) como USED; las demás como UNUSED
    # Si hay empate, se marcan como usadas todas las empatadas.
    used_set = set(n.name for n in best_children)
    for c, _ in vals:
        if c.name in used_set:
            mark_subtree(c, "used")
        else:
            mark_subtree(c, "unused")

    # El propio nodo queda "used/unused" decidido por su ancestro.
    # De momento lo dejamos como evaluado (current -> used provisional),
    # el ancestro se encargará después. Aquí lo ponemos como 'used' para que
    # visualmente quede verde salvo que su padre lo marque rojo.
    node_status[node.name] = "used"

    step_pause(fig, ax, node.name,
               f"{node.kind} decide en {node.name}: {best_val}")

    return best_val

# -------------------- Ejecutar visualización --------------------
if __name__ == "__main__":
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))
    # Estado inicial
    draw_scene(ax, None, "Minimax sin poda: preparación")
    fig.canvas.draw()
    plt.pause(0.001)
    time.sleep(2)

    final_v = minimax_trace(root, fig, ax)

    # Finalmente, propaga el marcado de la ruta óptima desde la raíz:
    # Elegimos al/los hijo(s) óptimo(s) de la raíz y marcamos el resto como unused.
    # Esto ya lo hace minimax_trace en cada nivel, pero repetimos para asegurar consistencia.
    # Determinar hijos óptimos de la raíz:
    children_vals = []
    for ch in root.children:
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

    step_pause(fig, ax, "ROOT", f"Final: V={final_v} en ROOT")

    # Mantener la ventana abierta al terminar
    plt.ioff()
    draw_scene(ax, None, f"Resultado final: V={final_v}")
    plt.show()
