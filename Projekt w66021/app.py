from flask import Flask, render_template, request, send_file
from PIL import Image, ImageEnhance
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        image = Image.open(file)
        action = request.form.get('action')

        try:
            if action == 'resize':
                width = request.form.get('width')
                height = request.form.get('height')
                if width and height:
                    width = int(width)
                    height = int(height)
                    image = image.resize((width, height))
                else:
                    return "Width and height must be provided for resize action."
            elif action == 'rotate':
                angle = request.form.get('angle')
                if angle:
                    angle = int(angle)
                    image = image.rotate(angle)
                else:
                    return "Angle must be provided for rotate action."
            elif action == 'brightness':
                factor = request.form.get('factor')
                if factor:
                    factor = float(factor)
                    enhancer = ImageEnhance.Brightness(image)
                    image = enhancer.enhance(factor)
                else:
                    return "Brightness factor must be provided."
            elif action == 'contrast':
                factor = request.form.get('factor')
                if factor:
                    factor = float(factor)
                    enhancer = ImageEnhance.Contrast(image)
                    image = enhancer.enhance(factor)
                else:
                    return "Contrast factor must be provided."
            elif action == 'collage':
                file2 = request.files['file2']
                if file2 and file2.filename != '':
                    image2 = Image.open(file2)
                    collage_width = image.width + image2.width
                    collage_height = max(image.height, image2.height)
                    collage = Image.new('RGB', (collage_width, collage_height))
                    collage.paste(image.convert('RGB'), (0, 0))
                    collage.paste(image2.convert('RGB'), (image.width, 0))
                    image = collage
                else:
                    return "Second image must be provided for collage action."
        except ValueError as e:
            return str(e)

        img_io = io.BytesIO()
        image = image.convert('RGB')
        image.save(img_io, 'JPEG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
