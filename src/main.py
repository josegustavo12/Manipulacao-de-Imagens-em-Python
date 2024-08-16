from image_blur_media import ImageBlurMedia
from PIL import Image
def main():
    
    
    # uso do blur
    blur = ImageBlurMedia('data/imagem.jpg', 'data/imagem_blurred_media6x6.png')
    blur.apply_blur()
    #blur2 = ImageBlurMedia('data/imagem_blurred_media.png', 'data/imagem_blurred_media2.png')
    #blur2.apply_blur()
   
    


if __name__ == "__main__":
    main()
