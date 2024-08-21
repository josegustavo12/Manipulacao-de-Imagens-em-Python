from image_blur_media import ImageBlurMedia
from image_blur_gaussiano import ImageBlurGauss
from PIL import Image
def main():
    
    
    # uso do blur
   # blur = ImageBlurMedia('data/imagem.jpg', 'data/imagem_blurred_media_4ft.png')
    #blur.apply_blur()

    blur_gauss = ImageBlurGauss('data/imagem.jpg', 'imagem_blurred_gaussiano')
    blur_gauss.processar_imagem()
    


if __name__ == "__main__":
    main()
