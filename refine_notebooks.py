import json
import os

def refine_notebook(file_path, h1_new=None, next_lesson_name=None, next_lesson_path=None, prev_lesson_name=None, prev_lesson_path=None):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # 1. Update H1 Header and Fix Orthography in all Markdown cells
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'markdown' and cell.get('source'):
            source = cell['source']
            
            # Update H1
            if h1_new and source[0].startswith('# '):
                source[0] = f"# {h1_new}\n"
            
            # General Orthography Fixes in current cell
            full_text = "".join(source)
            full_text = full_text.replace("## Que aprenderas?", "## ¿Qué aprenderás?")
            full_text = full_text.replace("## Que aprenderás?", "## ¿Qué aprenderás?")
            full_text = full_text.replace("¿Que aprenderás?", "¿Qué aprenderás?")
            full_text = full_text.replace("Por que usar", "¿Por qué usar")
            full_text = full_text.replace("Anatomia de una funcion", "Anatomía de una función")
            full_text = full_text.replace("multiples valores", "múltiples valores")
            full_text = full_text.replace("esta de acuerdo", "está de acuerdo") # just in case
            
            # Split back into lines if needed (though strings are usually fine in 'source')
            cell['source'] = [full_text]

    # 2. Update/Add Navigation at the end
    nav_cell_found = False
    nav_markdown = "---\n\n"
    if prev_lesson_name and prev_lesson_path:
        nav_markdown += f"**Anterior:** [{prev_lesson_name}]({prev_lesson_path})  \n"
    if next_lesson_name and next_lesson_path:
        nav_markdown += f"**Siguiente:** [{next_lesson_name}]({next_lesson_path})"

    if prev_lesson_name or next_lesson_name:
        for i in range(len(nb['cells']) - 1, -1, -1):
            cell = nb['cells'][i]
            if cell.get('cell_type') == 'markdown':
                source_str = "".join(cell.get('source', []))
                if "**Anterior:**" in source_str or "**Siguiente:**" in source_str:
                    cell['source'] = [nav_markdown]
                    nav_cell_found = True
                    break
        
        if not nav_cell_found:
            nb['cells'].append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [nav_markdown]
            })

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write('\n')

# Execute refinements
targets = [
    {
        "path": r"c:\Users\migue\01_PROFESIONAL\labs\python\01_python_fundamentals\01_01_variables_and_types.ipynb",
        "h1": "01.01 - Variables y Tipos de Datos en Python",
        "next_n": "02.01 - Funciones en Python",
        "next_p": "../02_functions_and_modules/02_01_functions_basics.ipynb"
    },
    {
        "path": r"c:\Users\migue\01_PROFESIONAL\labs\python\02_functions_and_modules\02_01_functions_basics.ipynb",
        "h1": "02.01 - Funciones en Python",
        "prev_n": "01.01 - Variables y Tipos de Datos en Python",
        "prev_p": "../01_python_fundamentals/01_01_variables_and_types.ipynb",
        "next_n": "03.01 - NumPy: Arrays Básicos",
        "next_p": "../03_numpy_essentials/03_01_arrays_basics.ipynb"
    },
    {
        "path": r"c:\Users\migue\01_PROFESIONAL\labs\python\03_numpy_essentials\03_01_arrays_basics.ipynb",
        "h1": "03.01 - NumPy: Arrays Básicos",
        "prev_n": "02.01 - Funciones en Python",
        "prev_p": "../02_functions_and_modules/02_01_functions_basics.ipynb"
    }
]

for t in targets:
    refine_notebook(
        t['path'], 
        h1_new=t.get('h1'),
        next_lesson_name=t.get('next_n'),
        next_lesson_path=t.get('next_p'),
        prev_lesson_name=t.get('prev_n'),
        prev_lesson_path=t.get('prev_p')
    )
    print(f"Refined: {t['path']}")
