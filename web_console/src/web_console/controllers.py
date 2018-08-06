from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

from web_console import app, static_folder


@app.route('/')
@app.route('/about')
def home():
    return make_response(open(static_folder + '/index.html').read())
