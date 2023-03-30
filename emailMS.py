from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'poolpalesd@gmail.com'
app.config['MAIL_PASSWORD'] = 'zhwarkqkjpdcfivp'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/result", methods=['POST', 'GET'])
# def result():
#     if request.method == "POST":
#         msg = Message(request.form.get("Subject"), 
#                       sender=request.form.get("Email"), 
#                       recipients=['poolpalesd@gmail.com'])
#         msg.body = request.form.get("Body")
#         mail.send(msg)
#         return render_template("result.html", result="Success!")
#     else:
#         return render_template("result.html", result="Failure.") 

def result():
    if request.method == "POST":
        sender_email = request.form.get("Email")
        recipient_email = 'poolpalesd@gmail.com'  
        msg = Message(request.form.get("Subject"), 
                      sender=sender_email, 
                      recipients=[recipient_email])
        msg.body = request.form.get("Body")
        mail.send(msg)
        return render_template("result.html", result="Success!")
    else:
        return render_template("result.html", result="Failure.")

    
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5050)
