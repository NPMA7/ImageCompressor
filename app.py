from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory
import cv2
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti dengan kunci rahasia Anda

UPLOAD_FOLDER = 'result'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def compress_image(input_path, output_path, quality=20):
    img = cv2.imread(input_path)
    cv2.imwrite(output_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('file')
        quality = int(request.form.get('quality', 20))
        
        compressed_files = []
        for file in files:
            if file:
                input_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(input_path)
                
                output_path = input_path  # Menggunakan nama yang sama

                compress_image(input_path, output_path, quality)
                compressed_files.append(file.filename)

        # Simpan nama file terkompresi dalam sesi
        session['compressed_files'] = compressed_files
        return redirect(url_for('index'))

    compressed_files = session.pop('compressed_files', [])
    return render_template('/index.html', compressed_files=compressed_files)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
