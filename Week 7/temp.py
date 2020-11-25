# create
# curl -X POST -
d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http:/
/127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
global nextId
if not request.json:
abort(400)
book = {
"id": nextId,
"Title": request.json["Title"],
"Author": request.json["Author"],
"Price": request.json["Price"]
}
books.append(book)
