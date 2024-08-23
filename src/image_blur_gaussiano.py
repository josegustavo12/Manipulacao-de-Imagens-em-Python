from PIL import Image

class ImageBlurGauss:
    
    def __init__(self, input_image_path, output_image_path, kernel_size=5, sigma=1):
        self.input_image_path = input_image_path
        self.output_image_path = output_image_path
        self.kernel_size = kernel_size
        self.sigma = sigma

    @staticmethod # serve para que eu consiga usar essa função dentro da própria classe
    def rgb_to_gray(imagem):
        width, height = imagem.size
        gray_imagem = Image.new('L', (width, height))  # Cria uma nova imagem em escala de cinza
        pixels = gray_imagem.load()
        for i in range(width):
            for j in range(height):
                r, g, b = imagem.getpixel((i, j))
                # Fórmula de luminância para converter para escala de cinza
                gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
                pixels[i, j] = gray
        return gray_imagem
    
    @staticmethod
    def convolucao(imagem, filt):
        """
        Aplica uma convolução 2D em uma imagem usando um filtro específico.
        """
        width, height = imagem.size
        k_width, k_height = len(filt), len(filt[0])
        kcx, kcy = k_width // 2, k_height // 2

        # Cria uma nova imagem em escala de cinza para armazenar o resultado
        output_imagem = Image.new('L', (width, height))
        pixels = output_imagem.load()
        imagem_pixels = imagem.load()

        for x in range(width):
            for y in range(height):
                acc = 0
                # Itera sobre o kernel
                for i in range(k_width):
                    for j in range(k_height):
                        # Coordenadas da imagem
                        xi = x + i - kcx
                        yj = y + j - kcy

                        if 0 <= xi < width and 0 <= yj < height:
                            acc += imagem_pixels[xi, yj] * filt[i][j]

                # Normaliza o valor acumulado
                acc = int(round(abs(acc) // sum(map(sum, filt))))
                pixels[x, y] = min(max(acc, 0), 255)  # Garante que o valor seja entre 0 e 255
                
                # print a cada 10 pixels para mostrar onde está a convolução
                if x % 10 == 0 and y % 10 == 0:
                    print(f"Convolução - Posição ({x}, {y})")
        return output_imagem


    @staticmethod
    def kernel_gauss(size, sigma=1):
        """
        Gera um kernel Gaussiano 2D.
        """
        kernel = []
        center = size // 2
        total = 0

        for x in range(size):
            row = []
            for y in range(size):
                # Calcula o valor do kernel Gaussiano
                g = (1 / (2.0 * 3.141592653589793 * sigma**2)) * \
                    2.718281828459045**(-((x-center)**2 + (y-center)**2) / (2.0*sigma**2))
                row.append(g)
                total += g
            kernel.append(row)

        # Normaliza o kernel para garantir que a soma seja 1
        for i in range(size):
            for j in range(size):
                kernel[i][j] /= total

        return kernel

    def apply_gauss(self):
        # Abre a imagem e a converte para escala de cinza
        imagem = Image.open(self.input_image_path)
        
        # Redimensiona a imagem para 600x600
        dimensao = (600, 600)
        imagem_resized = imagem.resize(dimensao)
        imagem_gray_resized = self.rgb_to_gray(imagem_resized)
        
        # Define um filtro Gaussiano e aplica a convolução
        gaussian_filt = self.kernel_gauss(self.kernel_size, sigma=self.sigma)
        imagem_blurred = self.convolucao(imagem_gray_resized, gaussian_filt)

        # Salva a imagem resultante
        imagem_blurred.save(self.output_image_path)

        # Mostra a imagem original redimensionada e a imagem suavizada
        imagem_resized.show()
        imagem_blurred.show()