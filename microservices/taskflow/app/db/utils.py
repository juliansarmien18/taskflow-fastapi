import os
import subprocess

def run_migrations():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..'))
    alembic_ini = os.path.join(base_dir, "alembic.ini")
    subprocess.run(["alembic", "-c", alembic_ini, "upgrade", "head"], check=True, cwd=base_dir)