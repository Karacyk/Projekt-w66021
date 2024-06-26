from PIL import Image

def resize_image(image_path, new_width, new_height):
    """Funkcja zmieniająca rozdzielczość obrazu."""
    image = Image.open(image_path)
    resized_image = image.resize((new_width, new_height))
    return resized_image
