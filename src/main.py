from image_blur_media import ImageBlurMedia
# ImageBlurMedia(path_imagem_de_origem, path_imagem_de_destino)
from image_blur_gaussiano import ImageBlurGauss
# ImageBlurGauss(path_imagem_de_origem, path_imagem_de_destino, kernel)
from image_mergefour import MergeFour
# MergeFour(path_imagem_de_origem_1, path_imagem_de_origem_2, path_imagem_de_origem_3, path_imagem_de_origem_4, path_imagem_de_origem_4, path_imagem_de_destino)

from PIL import Image
def main():
    
    
    # uso do blur de media
    blur_media = ImageBlurMedia('data/imagem.jpg', 'data/imagem_blurred_media_testeft.png')
    blur_media.apply_blur()
    # uso do blur de gauss
    #blur = ImageBlurGauss('data/imagem.jpg', 'data/imagem_filtrogaussk9.png', kernel_size=9, sigma=2)
    #blur.apply_gauss()
    
    

if __name__ == "__main__":
    main()
