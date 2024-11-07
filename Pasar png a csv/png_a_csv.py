import os
import pandas as pd
from PIL import Image
import base64
from io import BytesIO

# Ruta de la carpeta que contiene las imágenes PNG
png_folder_path = './Imagenes'
# Ruta del archivo CSV de salida
output_csv_path = './Archivos CSV/imagenes_convertidas.csv'

# Crear la carpeta de salida si no existe
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

# Lista para almacenar los datos de las imágenes
image_data_list = []

# Procesar cada archivo PNG en la carpeta
for filename in os.listdir(png_folder_path):
    if filename.endswith('.png'):
        png_file_path = os.path.join(png_folder_path, filename)
        
        # Leer la imagen
        try:
            with Image.open(png_file_path) as img:
                # Convertir la imagen a bytes
                buffered = BytesIO()
                img.save(buffered, format="PNG")
                image_bytes = buffered.getvalue()
                
                # Convertir a base64 y asegurarse de que no haya saltos de línea
                image_base64 = base64.b64encode(image_bytes).decode('utf-8').replace('\n', '')

                # Extraer metadatos (puedes personalizar esto según lo que necesites)
                ref_inter = filename.split('.')[0]  # Ejemplo: nombre del archivo sin extensión
                image_name = filename
                id_externo = os.path.splitext(filename)[0]  # Puedes personalizar esto

                # Guardar la información en la lista
                image_data_list.append({
                    'id_externo': id_externo,
                    'image_name': image_name,
                    'ref_inter': ref_inter,
                    'image_code': image_base64
                })
                
                print(f'Imagen procesada: {image_name}')
        except Exception as e:
            print(f'Error al procesar la imagen {filename}: {e}')

# Guardar los datos en un archivo CSV
if image_data_list:
    df = pd.DataFrame(image_data_list)
    df.to_csv(output_csv_path, index=False)
    print(f'Datos de imágenes guardados en: {output_csv_path}')


