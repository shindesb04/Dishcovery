import io
import os

import gridfs
import h5py
import numpy as np
import pandas as pd
import pymongo
import requests
import sklearn
import tensorflow as tf
from bson import ObjectId
from flask import Flask, Response, redirect, render_template, request, session
from flask_pymongo import PyMongo
from Ingredients_to_reciepe import recommend_recipes
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from Testing_model import predict

os.environ["TF_ENABLE_ONEDNN_OPTS"]="1"

my_collections = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_collections['Dishcovery']
user_col = my_db['User']

app = Flask(__name__)
app.secret_key = "Dishcovery"
app.config['MONGO_URI']='mongodb://localhost:27017/Dishcovery.images'
mongo=PyMongo(app)


@app.route("/")
def userLogin():
    return render_template("/userLogin.html")


@app.route("/userLogin1", methods=['post'])
def userLogin1():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email,password)
    query = {"email": email, "password": password}
    count = user_col.count_documents(query)
    if count > 0:
        user = user_col.find_one(query)
        session['user_id'] = str(user['_id'])
        session['role'] = 'User'
        return redirect("/home")
    else:
        return render_template("userLogin.html", message="Invalid Login Details",color="red")



@app.route("/userRegister")
def userRegister():
    return render_template("/userRegister.html")


@app.route("/userRegister1", methods=['post'])
def userRegister1():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    query = {"email": email}
    count = user_col.count_documents(query)
    if count > 0:
        return render_template("userRegister.html", message="Duplicate Details!!!.....", color="red")
    query = {"FirstName": fname, "LastName": lname, "email": email, "password": password}
    result = user_col.insert_one(query)
    return render_template("userLogin.html", message="User Registered successfully", color="green")


@app.route("/home")
def userHome():
    return render_template("userHome.html")

@app.route("/process_text", methods=['post'])
def process_text():
        # Load dataset from CSV
    csv_path = 'Source Code/content/Food Ingredients and Recipe Dataset with Image Name Mapping.csv'
    recipes_df = pd.read_csv(csv_path)
    # Use TF-IDF to vectorize ingredients
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(recipes_df['Ingredients'])

    # Compute cosine similarity between recipes
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    user_ingredients = request.form.get('predictionResult')
    print(user_ingredients)
    print("going to method")
    recommended_recipes = recommend_recipes(user_ingredients, recipes_df, tfidf_vectorizer, cosine_similarities,tfidf_matrix)

    # Print the recommended recipes
    print("Recommended Recipes:")
    dish_titles=''
    for recipe in recommended_recipes:
        dish_titles= recipe+", "+dish_titles
    session['result'] = dish_titles
    return redirect('/show_titles')

def remove_last_comma(s):
    # Find the position of the last comma
    last_comma = s.rfind(',')
    # If a comma is found, slice the string to remove it
    if last_comma != -1:
        s = s[:last_comma] + s[last_comma+1:]
    return s


@app.route('/show_titles')
def show_titles():
    # Retrieve the result from the session
    result = session.get('result', 'No result')
    result = remove_last_comma(result)
    #items = comma_separated_string.split(',')
    result = result.split(',')
    return render_template('predicted_title.html', prediction=result)
  

@app.route("/fileupload", methods=['post'])
def fileupload():
    img=request.files['imageupload']
    print("******************************************************")
    image = Image.open(io.BytesIO(img.read()))
    
    # Convert the PIL image to the correct format
    image = image.resize((64, 64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch
    # Now call the predict function with the processed image
    result = predict(input_arr)
    print(result)
    print("******************************************************")
    session['result'] = result
    return redirect('/show_result')

@app.route('/show_result')
def show_result():
    # Retrieve the result from the session
    result = session.get('result', 'No result')
    return render_template('predicted.html', prediction=result)

   
    
@app.route("/fetch_recipe", methods=['POST'])
def fetch_recipe():
    data = request.json
    query = data['item']
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'KThvv+VuO6DEFT+/vT8R7A==V9lPC9jVAdZX6jy0'})
    if response.status_code == 200:
        session['recipes'] = response.json()  # Store data in session
        return {'status': 'success'}
    else:
        return {'status': 'error', 'message': response.text}, response.status_code

@app.route("/display_recipe")
def display_recipe():
    recipes = session.get('recipes', None)
    if recipes:
        # Process each recipe
        for recipe in recipes:
            # Split the ingredients string into a list
            recipe['ingredients'] = recipe['ingredients'].split('|')

            # For instructions, you might want to split by period or another delimiter
            # This example splits by period, but adjust according to your needs
            recipe['instructions'] = recipe['instructions'].split('. ')
            
            # Remove any empty strings that may result from splitting
            recipe['instructions'] = [instr for instr in recipe['instructions'] if instr]

    return render_template('recipe_results.html', recipes=recipes)


if __name__=="__main__":
    app.run(debug=True,port=5010)
