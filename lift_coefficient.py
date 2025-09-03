import os
import subprocess
import matplotlib.pyplot as plt


def frange(start, stop, step):
    """Génère des nombres flottants comme range."""
    while start <= stop:
        yield round(start, 6)
        start += step


def generate_vspaero_file(
    filename,
    geom_file="dr_400.vsp3",
    alpha_start=-5,
    alpha_end=15,
    alpha_step=1,
    mach=0.1,
    altitude=0,
    max_iter=20
):
    alpha_values = list(frange(alpha_start, alpha_end, alpha_step))

    with open(filename, "w") as f:
        f.write(f"{geom_file}\n")
        f.write("SET\n0\n")
        f.write("CASE\n")
        f.write(f"{len(alpha_values)}\n")

        for alpha in alpha_values:
            f.write("alpha\n")
            f.write(f"{alpha:.2f}\n")
            f.write("beta\n0.0\n")
            f.write("mach\n")
            f.write(f"{mach}\n")
            f.write("alt\n")
            f.write(f"{altitude}\n")
            f.write("ReCref\n0\n")
            f.write("clamp\n0\n")
            f.write("velocity\n0\n")
            f.write("wake iterations\n")
            f.write(f"{max_iter}\n")
            f.write("end\n")

        f.write("PLOT\nEND\n")

    return alpha_values


def run_vspaero(input_file):
    """Exécute VSPAERO avec le fichier donné."""
    try:
        result = subprocess.run(
            ["vspaero", "<", input_file],
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("VSPAERO terminé.")
    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'exécution de VSPAERO :")
        print(e.stderr)


def read_history_file(history_file):
    """Lit le fichier .history et retourne alpha et CL."""
    alphas = []
    cls = []

    with open(history_file, "r") as f:
        lines = f.readlines()

    # Sauter les lignes d'en-tête
    for line in lines:
        if line.strip().startswith("#") or not line.strip():
            continue
        data = line.split()
        if len(data) < 6:
            continue
        alpha = float(data[0])
        cl = float(data[2])
        alphas.append(alpha)
        cls.append(cl)

    return alphas, cls


def plot_results(alphas, cls):
    """Affiche le graphe CL vs alpha."""
    plt.figure(figsize=(8, 5))
    plt.plot(alphas, cls, marker='o', linestyle='-', color='blue')
    plt.title("Coefficient de portance $C_L$ en fonction de l’angle d’attaque $\\alpha$")
    plt.xlabel("Angle d'attaque α [°]")
    plt.ylabel("Coefficient de portance $C_L$")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Étape 1 : Générer le fichier .vspaero
    vspaero_file = "dr400_simulation.vspaero"
    history_file = "dr_400.history"

    generate_vspaero_file(
        filename=vspaero_file,
        geom_file="dr_400.vsp3",
        alpha_start=-4,
        alpha_end=10,
        alpha_step=2,
        mach=0.1,
        altitude=0,
        max_iter=30
    )

    # Étape 2 : Lancer VSPAERO
    run_vspaero(vspaero_file)

    # Étape 3 : Lire les résultats et tracer le graphe
    if os.path.exists(history_file):
        alphas, cls = read_history_file(history_file)
        plot_results(alphas, cls)
    else:
        print(f"Fichier {history_file} non trouvé.")


