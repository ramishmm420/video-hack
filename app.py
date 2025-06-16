from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["url"]
        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
            stream.download(filename="video.mp4")
            return send_file("video.mp4", as_attachment=True)
        except Exception as e:
            return f"Error: {e}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
