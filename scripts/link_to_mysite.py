import re
import sys
from pathlib import Path

# Define = "https://www.weijiechen.com/linear-algebra-with-python-book/qmd/"


    chapter_slug = chapter_name.replace(" ", "%20").replace(",", "%2C")
    return f"{base_url}{chapter_slug}.html"

# Función para actualizar los enlaces en el archivo Markdown
un objeto Path
    file_path = Path(file_path)
    
    i)  print(f"Error: El archivo {file_path} no existe.")
        return

    # Lee el archivo originale
        content = file.read()

    # Expresión regular para encontrar todos los enlaces con capítulos
    pr
    def replace_link(match):
        chapter_name = match.group(1)
        return f"[{chapter_name}]({generate_url(chapter_name)})"
Reemplaza los enlaces con el formato correcto
    updated_content = pattern.sub(replace_link, content)

    # Escribe el contenido actualizado de nuevo en el archivo
    with file_path.open('w', encoding='utf-8') as file:
        file.write(updated_content)
 actualizados.")

# Función principal para manejar los argumentos de la línea de comandos
está en el directorio 'scripts'
    script_dir = Path(__file__).parent
    markdown_file_path = script_dir.parent / 'README.md'

)

    update_links_in_markdown(markdown_file_path)
