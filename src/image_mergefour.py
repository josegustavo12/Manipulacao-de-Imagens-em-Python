from PIL import Image

class MergeFour(): # passei mto tempo pensando nesse nome e ainda não gostei :(
    def __init__(self, path_foto_1, path_foto_2, path_foto_3, path_foto_4, output_image_path):
            
            # iniciando o path de todas as fotos
            self.path_foto_1 = path_foto_1
            self.path_foto_2 = path_foto_2
            self.path_foto_3 = path_foto_3
            self.path_foto_4 = path_foto_4
            self.output_image_path = output_image_path

    def Merge(self):

        dimensao = (300, 300) # dimensão das imagens
        # lista com tds as imagens (1 ao 4) e já redimensionadas 
        imagem = [(Image.open(self.path_foto_1)).resize(dimensao), 
                  (Image.open(self.path_foto_2)).resize(dimensao), 
                  (Image.open(self.path_foto_3)).resize(dimensao), 
                  (Image.open(self.path_foto_4)).resize(dimensao)]
        # nova imagem com a dimensao 600,600 por ser 4 fotos de 300,300
        imagem_compfour = Image.new('RGB', (600,600))  
        # usando o comando .paste para colar as imagens (pensei em fazer colocando pixel por pixel, mas ia dar um trampo mto desnecessario)
        imagem_compfour.paste(imagem[0], (0,0))
        imagem_compfour.paste(imagem[1], (0,300))
        imagem_compfour.paste(imagem[2], (300,0))
        imagem_compfour.paste(imagem[3], (300,300))



        imagem_compfour.save(self.output_image_path)
        imagem_compfour.show()
        print(f"Imagem processada e salva em {self.output_image_path}")
