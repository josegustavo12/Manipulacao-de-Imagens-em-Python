from image_blur import ImageBlur

def main():
    
    
    # uso do blur
    blur = ImageBlur('data/imagem.jpg', 'data/imagem_blurred.png')
    blur.apply_blur()
    blur2 = ImageBlur('data/imagem_blurred.png', 'data/imagem_blurred2.png')
    blur2.apply_blur()


if __name__ == "__main__":
    main()
