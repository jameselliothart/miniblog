from flask import render_template
import config

# Get the application instance
connex_app = config.connex_app

# Read swagger.yml to configure endpoints
connex_app.add_api('swagger.yml')

# Create a URL route for "/"
@connex_app.route('/')
def home():
    """
    Responds to the browser URL
    localhost:5000/
    """
    return render_template('home.html')


# If running stand alone, run the application
if __name__ == '__main__':
    connex_app.run(host='127.0.0.1', port=5000, debug=True)
