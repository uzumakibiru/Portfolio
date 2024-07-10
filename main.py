from flask import Flask, request,render_template
from send import SendMessage
from random import choice

img_list=[f"Nemo ({i+1})" for i in range(23)]
app= Flask(__name__)

def random_logo():
    img=choice(img_list)
    return img

@app.route("/")
def home():
    logo_img=random_logo()
    return render_template("index.html",logo_img=logo_img)

@app.route("/contact",methods=["GET","POST"])
def contact():
    logo_img=random_logo()
    if request.method=="GET":
        return render_template("contact.html",logo_img=logo_img)
    else:
        name=request.form["name"]
        email=request.form["email"]
        message=request.form["message"]
        msg=SendMessage(name,email,message)
        msg.from_sender()
        msg.to_sender()
        return render_template("contact.html",logo_img=logo_img)

if __name__=="__main__":
    app.run(debug=True)