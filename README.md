
---

# Projeto de Manipulação de Imagens com Python

Este projeto explora diversas técnicas de manipulação de imagens utilizando Python. A primeira funcionalidade implementada é a aplicação de um filtro de desfoque (blur) utilizando a média dos pixels ao redor.

## Estrutura do Projeto

O projeto é organizado em duas partes principais:

1. **`image_blur_media.py`**: Contém a implementação da classe `ImageBlurMedia`, responsável por aplicar o desfoque em uma imagem utilizando a média dos pixels vizinhos.
2. **`main.py`**: Script que utiliza a classe `ImageBlurMedia` para aplicar o desfoque em imagens.

## `image_blur_media.py`

### Código do Filtro de Desfoque com Média

```python
from PIL import Image

class ImageBlur:
    def __init__(self, input_image_path, output_image_path):
        self.input_image_path = input_image_path
        self.output_image_path = output_image_path

    def apply_blur(self):
        imagem = Image.open(self.input_image_path)
        dimensao = (600, 600)
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

                for dx in range(-1, 2):
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

            if x % 10 == 0:
                print(f"Processando coluna {x} de {largura}")

        imagem_blur.save(self.output_image_path)
        imagem_blur.show()
        print(f"Imagem processada e salva em {self.output_image_path}")

```

#### Explicação do Código

- **`__init__`**: Método construtor que inicializa os caminhos dos arquivos de entrada e saída.
- **`apply_blur`**: Método que aplica um desfoque na imagem usando a média dos pixels vizinhos. Cria uma nova imagem onde cada pixel é a média dos valores RGB dos pixels em uma janela 3x3 ao redor.

#### Justificativa para o Redimensionamento da Imagem

- **Por que redimensionar a imagem?**
    - Durante os testes, observei que o efeito de desfoque se tornava quase imperceptível na imagem original, que tinha uma resolução muito alta (3198x2399 pixels). Devido ao grande número de pixels, o desfoque aplicado a cada pixel individual representava uma mudança mínima na imagem como um todo.
    - Ao redimensionar a imagem para (600x600) pixels, a proporção do desfoque em relação ao tamanho da imagem aumenta significativamente, tornando o efeito mais visível. Na imagem original, cada pixel modificado representava apenas 0,038% da imagem total, enquanto na imagem redimensionada, cada pixel modificado representa 0,16% da imagem, ou seja, o efeito de desfoque é aproximadamente 421% mais perceptível.
    - Somente um adendo que eu (o autor) não sei o quanto é correto essa explicação, de forma prática é isso mesmo

## `main.py`

### Descrição

O arquivo `main.py` contém a função principal que utiliza a classe `ImageBlur` para aplicar o filtro de desfoque por média em uma imagem.

### Código

```python
from image_blur import ImageBlur

def main():
    # Aplicar o desfoque
    blur = ImageBlur('data/imagem.jpg', 'data/imagem_blurred.png')
    blur.apply_blur()
    
    # Reaplicar o desfoque para testar o efeito acumulado
    blur2 = ImageBlur('data/imagem_blurred.png', 'data/imagem_blurred2.png')
    blur2.apply_blur()

if __name__ == "__main__":
    main()
```

### Explicação

- **Instâncias da Classe `ImageBlur`**:
  - **Primeira Instância**: Aplica o desfoque na imagem original (`imagem.jpg`) e salva o resultado como `imagem_blurred.png`.
  - **Segunda Instância**: Aplica novamente o desfoque na imagem já borrada (`imagem_blurred.png`) e salva como `imagem_blurred2.png` para testar o efeito acumulativo de múltiplas aplicações do filtro.

## Requisitos

- **Pillow**: Biblioteca Python para processamento de imagens. Instale-a com o seguinte comando:
  ```bash
  pip install Pillow
  ```

## Execução

1. Certifique-se de que o arquivo `imagem.jpg` está localizado na pasta `data/`.
2. Execute o script `main.py` para aplicar o desfoque:
   ```bash
   python main.py
   ```

---

Essa versão aprimorada explica mais detalhadamente o processo de redimensionamento e por que ele foi necessário para tornar o efeito de desfoque mais visível.