# Import the create_app function from the project module
from project import create_app

# Create a Flask application instance using the create_app function
app = create_app()

# Check if the script is being executed as the main module
if __name__ == "__main__":
    # If so, run the Flask application
    app.run()