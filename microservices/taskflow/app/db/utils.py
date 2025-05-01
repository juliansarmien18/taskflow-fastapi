import os
import subprocess

def run_migrations():
    # Calcular la ruta absoluta del directorio base (un nivel arriba)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    alembic_ini = os.path.join(base_dir, "alembic.ini")
    print(f"Usando archivo alembic.ini en: {alembic_ini}")  # Para verificar la ruta
    subprocess.run(["alembic", "-c", alembic_ini, "upgrade", "head"], check=True, cwd=base_dir)