from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read swagger.yml to configure endpoints
app.add_api('swagger.yml')

# Create a URL route for "/"
@app.route('/')
def home():
    return render_template('home.html')


# If running stand alone, run the application
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
