from itertools import product

def posibles_finales(puntos_A, puntos_B, partidos_A, partidos_B, enfrentamientos):
    # Partidos individuales (no son entre ellos)
    partidos_ind_A = partidos_A - enfrentamientos
    partidos_ind_B = partidos_B - enfrentamientos

    if partidos_ind_A < 0 or partidos_ind_B < 0:
        raise ValueError("Los partidos restantes no cuadran con el número de enfrentamientos directos.")

    outcomes_ind = [3, 1, 0]  # Victoria, empate, derrota en partidos individuales
    outcomes_dir = [(3, 0), (1, 1), (0, 3)]  # (puntos_A, puntos_B) en los enfrentamientos directos

    # Si no hay partidos individuales, usamos secuencia vacía
    comb_A_ind = list(product(outcomes_ind, repeat=partidos_ind_A)) if partidos_ind_A > 0 else [()]
    comb_B_ind = list(product(outcomes_ind, repeat=partidos_ind_B)) if partidos_ind_B > 0 else [()]
    # Si no hay enfrentamientos directos, secuencia vacía
    comb_dir = list(product(outcomes_dir, repeat=enfrentamientos)) if enfrentamientos > 0 else [()]

    escenarios = []

    for seq_A_ind in comb_A_ind:
        for seq_B_ind in comb_B_ind:
            for seq_dir in comb_dir:
                # Puntos por partidos individuales
                pts_A_ind = sum(seq_A_ind) if seq_A_ind else 0
                pts_B_ind = sum(seq_B_ind) if seq_B_ind else 0

                # Puntos por enfrentamientos directos
                pts_A_dir = sum(a for (a, b) in seq_dir)
                pts_B_dir = sum(b for (a, b) in seq_dir)

                total_A = puntos_A + pts_A_ind + pts_A_dir
                total_B = puntos_B + pts_B_ind + pts_B_dir

                # Guardamos también la descripción de los directos tipo "3-0", "1-1", ...
                seq_dir_str = [f"{a}-{b}" for (a, b) in seq_dir]

                escenarios.append((seq_A_ind, seq_B_ind, seq_dir_str, total_A, total_B))

    return escenarios


# --------- PROGRAMA PRINCIPAL ---------

team1 = input("Team 1: ")
team2 = input("Team 2: ")

ptsEq1 = int(input(f"Give me the points {team1} has: "))
ptsEq2 = int(input(f"Give me the points {team2} has: "))

matchesLeft1 = int(input(f"{team1} has to play (total remaining matches): "))
matchesLeft2 = int(input(f"{team2} has to play (total remaining matches): "))

# Preguntamos si se enfrentarán
ans = input(f"Will {team1} and {team2} play against each other? (y/n): ").strip().lower()

if ans == "y":
    enfrentamientos = int(input(f"How many matches between {team1} and {team2}: "))
else:
    enfrentamientos = 0

try:
    escenarios = posibles_finales(ptsEq1, ptsEq2, matchesLeft1, matchesLeft2, enfrentamientos)
except ValueError as e:
    print(f"\nERROR: {e}")
    exit(1)

print("\n==================== POSIBILIDADES ====================\n")

for i, esc in enumerate(escenarios, start=1):
    seq_A_ind, seq_B_ind, seq_dir_str, final_A, final_B = esc

    # Formato legible de partidos individuales
    seq_A_ind_str = ", ".join(str(x) for x in seq_A_ind) if seq_A_ind else "No individual matches"
    seq_B_ind_str = ", ".join(str(x) for x in seq_B_ind) if seq_B_ind else "No individual matches"

    # Formato de enfrentamientos directos
    dir_str = ", ".join(seq_dir_str) if seq_dir_str else "No head-to-head matches"

    print(f"Scenario {i}:")
    print(f"  {team1} individual matches: [{seq_A_ind_str}]")
    print(f"  {team2} individual matches: [{seq_B_ind_str}]")
    print(f"  Head-to-head ({team1}-{team2}) matches: [{dir_str}]")
    print(f"  --> Final points: {team1} = {final_A}, {team2} = {final_B}")
    print("-" * 60)

print("\n=======================================================\n")
print(f"Total possible scenarios: {len(escenarios)}")
