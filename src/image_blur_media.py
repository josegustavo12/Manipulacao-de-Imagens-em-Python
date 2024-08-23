from PIL import Image

class ImageBlurMedia:
    def __init__(self, input_image_path, output_image_path):
        self.input_image_path = input_image_path
        self.output_image_path = output_image_path

    def apply_blur(self):
        imagem = Image.open(self.input_image_path)
        dimensao = (300,300)
        imagem = imagem.resize(dimensao)
        imagem = imagem.convert('RGB')
        largura, altura = imagem.size

        imagem_blur = Image.new('RGB', (largura, altura))  

        for x in range(largura):
            for y in range(altura):
                soma_r = 0
                soma_g = 0
                soma_b = 0
                contagem = 0

                for dx in range(-1, 2): # a mudança nesses limites influencia no quão borrado a imagem final é
                    for dy in range(-1, 2):
                        nx = x + dx
                        ny = y + dy

                        if 0 <= nx < largura and 0 <= ny < altura:
                            pixel_valor = imagem.getpixel((nx, ny))
                            soma_r += pixel_valor[0]
                            soma_g += pixel_valor[1]
                            soma_b += pixel_valor[2]
                            contagem += 1
                media_r = soma_r // contagem
                media_g = soma_g // contagem
                media_b = soma_b // contagem
                imagem_blur.putpixel((x, y), (media_r, media_g, media_b))
                
            # Exibir progresso
                if x % 10 == 0 and y % 10 == 0:
                    print(f"Convolução - Posição ({x}, {y})")

        imagem_blur.save(self.output_image_path)
        imagem_blur.show()
        print(f"Imagem processada e salva em {self.output_image_path}")


