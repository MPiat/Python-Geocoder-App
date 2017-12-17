from flask import Flask, render_template, request
from backend import file_handling
import os

app=Flask(__name__)
#Prepare the program for bad data
#@app.route('/')
#def home():
#    return render_template("home.html")
@app.route('/')
def upload():
    return render_template("upload.html")

@app.route('/uploader', methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        file_handling(f.filename)
        os.remove(f.filename)
        return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True)
