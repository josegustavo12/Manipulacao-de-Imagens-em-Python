from PIL import Image, ImageFilter

class ImageBlur:
    def __init__(self, input_image_path, output_image_path):
        self.input_image_path = input_image_path
        self.output_image_path = output_image_path

    def apply_blur(self):
        imagem = Image.open(self.input_image_path)
        
        # Aplica um desfoque gaussiano com raio ajustável
        imagem_blur = imagem.filter(ImageFilter.GaussianBlur(radius=5))  # Experimente aumentar o raio se necessário
        
        # Salva e exibe a imagem borrada
        imagem_blur.save(self.output_image_path)
        imagem_blur.show()


