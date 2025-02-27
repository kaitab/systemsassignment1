#this contains the flask code
from flask import Flask, request, render_template
import notesapp

app = Flask(__name__)
our_notes = notesapp.NotesApp()

@app.route("/", methods=["GET", "POST"])
def main_page():
    """generates the main page"""
    return render_template("mainpage.html", notes=our_notes.list_all())

@app.route("/add", methods=["POST"])
def add_note():
    """adds a note and sends a success message"""
    title = request.form["title"]
    content = request.form["content"]
    if title and content:
        our_notes.add_note(title, content)
        return render_template("addpage.html")
    else:
        return render_template("errorpage.html")

@app.route("/find")
def search_results():
    """displays search results"""
    term = request.args["term"]
    return render_template("searchpage.html", results=our_notes.search_notes(term))

@app.route("/note/<note_name>")
def get_note(note_name):
    """displays a note given its name"""
    body = our_notes.return_note(note_name)
    return render_template("notepage.html", name=note_name, note_body=body)

if __name__ == '__main__':
    app.run(debug=True)
