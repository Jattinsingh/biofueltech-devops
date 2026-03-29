from flask import Flask, render_template
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def generate_graph():
    months = ["M1","M3","M6","M9","M12"]
    revenue = [20000,50000,80000,100000,120000]

    plt.figure()
    plt.plot(months, revenue, marker='o')
    plt.title("Revenue Growth Projection")

    if not os.path.exists("static"):
        os.makedirs("static")

    plt.savefig("static/graph.png")
    plt.close()

@app.route('/')
def home():
    generate_graph()
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/founder')
def founder():
    return render_template('founder.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)