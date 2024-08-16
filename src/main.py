from image_blur_media import ImageBlurMedia
from PIL import Image
def main():
    
    
    # uso do blur
    blur = ImageBlurMedia('data/imagem.jpg', 'data/imagem_blurred.png')
    blur.apply_blur()
    blur2 = ImageBlurMedia('data/imagem_blurred.png', 'data/imagem_blurred2.png')
    blur2.apply_blur()

    
    


if __name__ == "__main__":
    main()
