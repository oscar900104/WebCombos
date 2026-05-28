from PIL import Image
import numpy as np

def remove_background(input_path, output_path, threshold=240):
    """
    Elimina el fondo blanco de una imagen y la guarda como PNG con transparencia.
    
    Args:
        input_path: Ruta de la imagen de entrada
        output_path: Ruta de la imagen de salida
        threshold: Umbral para considerar un píxel como blanco (0-255)
    """
    # Cargar imagen
    img = Image.open(input_path)
    
    # Convertir a RGBA si no lo es
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Convertir a array numpy para procesamiento más rápido
    data = np.array(img)
    
    # Crear máscara: True donde el píxel es blanco/casi blanco
    # Un píxel se considera blanco si todos sus canales RGB están por encima del umbral
    white_mask = (
        (data[:, :, 0] > threshold) &  # Canal R
        (data[:, :, 1] > threshold) &  # Canal G
        (data[:, :, 2] > threshold)    # Canal B
    )
    
    # Establecer alpha a 0 (transparente) donde hay blanco
    data[white_mask, 3] = 0
    
    # Crear imagen resultante
    result = Image.fromarray(data)
    
    # Guardar como PNG (soporta transparencia)
    result.save(output_path, 'PNG')
    print(f"Imagen guardada en: {output_path}")
    print(f"Fondo eliminado de {np.sum(white_mask)} píxeles")

if __name__ == "__main__":
    # Rutas de archivos
    input_file = r"C:\xampp\htdocs\web combos\public\img\logo.jpg"
    output_file = r"C:\xampp\htdocs\web combos\public\img\logo-transparent.png"
    
    # Eliminar fondo
    remove_background(input_file, output_file, threshold=240)