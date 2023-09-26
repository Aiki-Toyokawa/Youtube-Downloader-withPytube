# app.py
# aiki-toyokawa/youtube-downloader-with-pytube
from flask import Flask, render_template, request, jsonify
from pytube import YouTube
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["GET"])
def download():
    video_url = request.args.get("videoUrl")
    download_folder = "C:\\Users\\owner\\Desktop"

    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=download_folder)
        thumbnail_url = yt.thumbnail_url
        return jsonify({"success": True, "thumbnailUrl": thumbnail_url})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
