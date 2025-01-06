"""
Description: mad libs in python
Author: Eric
"""
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# The template for the story
STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

@app.route('/', methods=['GET', 'POST'])
def madlib():
    if request.method == 'POST':
        name = request.form['name']
        adj1 = request.form['adj1']
        adj2 = request.form['adj2']
        adj3 = request.form['adj3']
        verb = request.form['verb']
        noun1 = request.form['noun1']
        noun2 = request.form['noun2']
        animal = request.form['animal']
        food = request.form['food']
        fruit = request.form['fruit']
        superhero = request.form['superhero']
        country = request.form['country']
        dessert = request.form['dessert']
        year = request.form['year']
        
        story = STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, 
                        name, superhero, name, country, name, dessert, name, year, noun2)
        return render_template('result.html', story=story)
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)





























