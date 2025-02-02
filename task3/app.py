from flask import Flask, request, render_template, send_file
import markdown
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file uploaded", 400

        file = request.files["file"]

        if file.filename == "":
            return "No selected file", 400

        if file and file.filename.endswith(".md"):
            md_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(md_path)

            # Convert Markdown to HTML
            with open(md_path, "r", encoding="utf-8") as f:
                md_content = f.read()
                html_content = markdown.markdown(md_content)

            # Save HTML file
            html_filename = file.filename.rsplit(".", 1)[0] + ".html"
            html_path = os.path.join(OUTPUT_FOLDER, html_filename)

            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            return send_file(html_path, as_attachment=True)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
