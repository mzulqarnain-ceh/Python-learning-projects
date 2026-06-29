from flask import Flask, jsonify,request
import sqlite3, os
app=Flask(__name__)
# database setup function
def get_db():
    folder=os.path.dirname(__file__)
    path=os.path.join(folder,"books.db")
    conn = sqlite3.connect(path)
    conn.row_factory=sqlite3.Row
    return conn
def create_table():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author TEXT NOT NULL)")
    conn.commit()
    conn.close()
#  API Routes 
@app.route("/")
def home():
    return jsonify({"message": "Welcome to Books API",
    "routes":{
        "GET /books": "Get All Books",
        "GET /books/<id>": "Get a Specific Book",
        "POST /books": "Add a New Book",
        "PUT /books/<id>": "Update a Book",
        "DELETE /books/<id>": "Delete a Book"
        }
    })
@app.route("/books", methods=["GET"])
def get_all_books():
    conn = get_db()
    books = conn.execute("SELECT * FROM books").fetchall()
    books_list=[{"id": book["id"], "title": book["title"], "author": book["author"]} for book in books]
    return jsonify(books_list)
@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    conn = get_db()
    book = conn.execute("SELECT * FROM books WHERE id=?",(id,)).fetchone()
    conn.close()
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({"id": book["id"], "title": book["title"], "author": book["author"]})
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    if not data or "title" not in data or "author" not in data:
        return jsonify({"error": "title and author are required"}), 400
    conn = get_db()
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (data["title"], data["author"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Book added successfully"}), 201
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()
    if not data or "title" not in data or "author" not in data:
        return jsonify({"error": "title and author are required"}), 400
    conn = get_db()
    book = conn.execute("SELECT * FROM books WHERE id=?",(id,)).fetchone()
    if book is None:
        conn.close()
        return jsonify({"error": "Book not found"}), 404
    conn.execute("UPDATE books SET title=?, author=? WHERE id=?",(data["title"], data["author"], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Book updated successfully"})
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    conn = get_db()
    book=conn.execute("SELECT * FROM books WHERE id=?",(id,)).fetchone()
    if book is None:
        conn.close()
        return jsonify({"error": "Book not found"}), 404
    conn.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Book deleted successfully"})
if __name__=="__main__":
    create_table()
    app.run(debug=True)
