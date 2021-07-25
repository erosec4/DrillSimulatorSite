from flask import Flask, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST']) #default page
def home(): #home page
    return """
    <img src="{{url_for('images', filename='footballField copy.png', width=100)}}" />
    """

if __name__ == "__main__":
    app.run()
    
    
# create git repository
