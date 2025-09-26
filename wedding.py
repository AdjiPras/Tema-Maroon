from flask import Flask, render_template
import mimetypes

application = Flask(__name__)
application.config['SECRET_KEY'] = 'sfh7^erw9*(%sadHGw%R'

# Pastikan file .mp3 dikenali sebagai audio/mpeg
mimetypes.add_type('audio/mpeg', '.mp3')

# INDEX
@application.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    application.run(debug=True)  # ubah ke debug=False kalau deploy