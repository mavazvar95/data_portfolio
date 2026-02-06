import json
import os

def final_polish(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    replacements = {
        "codigo": "código",
        "logica": "lógica",
        "Parametros": "Parámetros",
        "parametros": "parámetros",
        "Documentacion": "Documentación",
        "documentacion": "documentación",
        "estaciones": "estaciones", # check
        "Duracion": "Duración",
        "duracion": "duración",
        "estadisticas": "estadísticas",
        "reutilizable": "reutilizable" # already ok
    }

    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            text = "".join(cell['source'])
            for old, new in replacements.items():
                # Avoid replacing inside backticks if possible, but simple replacement is usually fine for these terms
                text = text.replace(old, new)
            cell['source'] = [text]

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write('\n')

paths = [
    r"c:\Users\migue\01_PROFESIONAL\labs\python\01_python_fundamentals\01_01_variables_and_types.ipynb",
    r"c:\Users\migue\01_PROFESIONAL\labs\python\02_functions_and_modules\02_01_functions_basics.ipynb",
    r"c:\Users\migue\01_PROFESIONAL\labs\python\03_numpy_essentials\03_01_arrays_basics.ipynb"
]

for p in paths:
    final_polish(p)
    print(f"Polished: {p}")
