from PIL import Image
import numpy as np

# Classe para aplicar o filtro gaussiano manualmente em uma imagem
class ImageBlurGauss:
    def __init__(self, input_image_path, output_image_path):
        # Inicializa a classe com os caminhos de entrada e saída das imagens
        self.input_image_path = input_image_path
        self.output_image_path = output_image_path
        
        

