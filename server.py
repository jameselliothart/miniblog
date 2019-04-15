from flask import (
    Flask,
    render_template
)

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route for "/"
@app.route('/')
def home():
    return render_template('home.html')


# If running stand alone, run the application
if __name__ == '__main__':
    app.run(debug=True)
