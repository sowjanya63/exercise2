from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def route():
    list=[1,2,3,4]
    return render_template("index.html",l=list)
if __name__ == "__main__":
    app.run(debug=True)
