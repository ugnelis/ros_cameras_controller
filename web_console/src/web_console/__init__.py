from flask import Flask, request, Response
import rospkg

static_folder = rospkg.RosPack().get_path('web_console') + '/src/static/'

app = Flask(__name__,
            static_folder=static_folder,
            static_url_path='/static')

import web_console.controllers
