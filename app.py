from flask import Flask, render_template, make_response
from io import BytesIO
from PIL import ImageGrab

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/screenshot')
def screenshot():
    
    screenshot = ImageGrab.grab()
    
    
    buffer = BytesIO()
    screenshot.save(buffer, format="PNG")
    
    
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
