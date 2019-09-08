from flask import Flask, render_template, request, abort

from Saloon import config

app = Flask(__name__)

app.config.from_object(config.Configuration)
