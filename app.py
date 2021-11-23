# -*- coding: utf-8 -*-


from __future__ import unicode_literals
# 引入套件
from flask import Flask, request, abort
# 初始化Flask物件
app = Flask(__name__, static_url_path='', static_folder='static')
@app.route("/")
def index():
    return app.send_static_file('index.html')





if __name__ == "__main__":
    app.run()
