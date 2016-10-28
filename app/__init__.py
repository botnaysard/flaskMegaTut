from flask import Flask

app = Flask(__name__) # create a variable and assign the Flask instance to it
from app import views # import the app package from views (not the same thing as the above variable)

