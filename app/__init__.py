from flask import Flask
from config import Config

townsquare = Flask(__name__)
townsquare.config.from_object(Config)


from app import routes