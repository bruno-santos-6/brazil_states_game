from PIL import Image


def convert_to_gif(input_image_path, output_image_path, max_size=(800, 600), optimize=True, quality=85):
    try:
        # Abrir a imagem PNG
        image = Image.open(input_image_path)

        # Redimensionar a imagem para um tamanho máximo (opcional)
        image.thumbnail(max_size)

        # Salvar a imagem no formato GIF com a otimização e qualidade desejadas
        image.save(output_image_path, format='GIF', optimize=optimize, quality=quality)

        print("Imagem convertida com sucesso para GIF.")
    except Exception as e:
        print("Erro ao converter a imagem:", e)


convert_to_gif('Brazil_Labelled_Map.png', 'Brazil_Labelled_Map.gif')
