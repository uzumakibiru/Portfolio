from flask import Flask, request,render_template
from send import SendMessage


app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method=="GET":
        return render_template("contact.html")
    else:
        name=request.form["name"]
        email=request.form["email"]
        message=request.form["message"]
        msg=SendMessage(name,email,message)
        msg.from_sender()
        msg.to_sender()
        return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)