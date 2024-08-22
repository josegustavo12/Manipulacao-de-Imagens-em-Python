from image_blur_media import ImageBlurMedia
# ImageBlurMedia(path_imagem_de_origem, path_imagem_de_destino)
from image_blur_gaussiano import ImageBlurGauss
# ImageBlurGauss(path_imagem_de_origem, path_imagem_de_destino, kernel)
from image_mergefour import MergeFour
# MergeFour(path_imagem_de_origem_1, path_imagem_de_origem_2, path_imagem_de_origem_3, path_imagem_de_origem_4, path_imagem_de_origem_4, path_imagem_de_destino)

from PIL import Image
def main():
    
    
    # uso do blur de media
    #blur_media = ImageBlurMedia('data/imagem.jpg', 'data/imagem_blurred_media_4ft.png')
    #blur_media.apply_blur()
    # uso do blur de gauss
    #blur_gauss = ImageBlurGauss('data/imagem.jpg', 'imagem_blurred_gaussiano')
    #blur_gauss.processar_imagem()
    merge_fotos = MergeFour('data/imagem.jpg', 'data/imagem_blurred_media.png','data/imagem_blurred_media2.png','data/imagem_blurred_media4x4.png','data/imagem_merged.png' )
    merge_fotos.Merge()


if __name__ == "__main__":
    main()
