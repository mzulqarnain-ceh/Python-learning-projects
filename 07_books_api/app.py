from flask import Flask, jsonify,request
import sqlite3, os
app=Flask(__name__)
# database setup function
def get_db():
    pass
def create_table():
    pass
#  API Routes 
@app.route("/books", methods=["GET"])
def get_all_books():
    pass
@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    pass
@app.route("/books", methods=["POST"])
def add_book():
    pass
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    pass
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    pass

if __name__=="__main__":
    create_table()
    app.run(debug=True)
