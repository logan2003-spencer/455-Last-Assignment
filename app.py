from flask import Flask, render_template, request
import pandas as pd  # Import pandas to load CSV files

app = Flask(__name__)

# Load the CSV data into pandas DataFrames
collaborative_data = pd.read_csv("data/Collaborative_Filtering.csv")  # Collaborative data (replace path if needed)
content_data = pd.read_csv("data/content_filtering.csv")  # Content data (replace path if needed)

def get_collaborative_recommendations(user_item_id):
    """
    Obtain recommendations using collaborative filtering data.
    Here we're using collaborative_data DataFrame for the recommendations.
    """
    # Assuming the 'collaborative_data' CSV has columns like ['user_id', 'item_id', 'rating']
    user_recommendations = collaborative_data[collaborative_data['personId'] == int(user_item_id)]['contentId'].tolist()
    return user_recommendations[:5]  # Limit to top 5 recommendations

def get_content_recommendations(user_item_id):
    """
    Obtain recommendations using content filtering data.
    Here we're using content_data DataFrame for the recommendations.
    """
    # Assuming the 'content_data' CSV has columns like ['item_id', 'title', 'description']
    # For simplicity, just return the first 5 items
    return content_data['item_id'].tolist()[:5]  # Limit to top 5 recommendations

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = {}
    if request.method == "POST":
        user_item_id = request.form["user_item_id"]
        recommendations["collaborative"] = get_collaborative_recommendations(user_item_id)
        recommendations["content"] = get_content_recommendations(user_item_id)
    return render_template("index.html", recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
