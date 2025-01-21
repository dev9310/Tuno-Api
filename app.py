from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import logging
import time
import random
from DBManager import Manager
from Scarpper import SearchResult

app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "*"}})


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example function to process data
def process_data(input_data):
    sr = SearchResult()
    query = input_data  # Use the input data as the query
    max_results = 7

    logger.info(f"Fetching top {max_results} results for query: {query}")
    result_data = list(sr.google_custom_search(query, max_results=max_results))
    print("Done")
    return result_data


@app.route("")
def Home():
    return "hejjp"

# API route
@app.route('/api/scrapper', methods=['POST'])
def process_api():
    try:
        data = request.get_json()
        if not data or 'data' not in data:
            return jsonify({"status": "error", "message": "Invalid input data"}), 400

        result = process_data(data['data'])
        return jsonify({"status": "success", "data": result}), 200
    except Exception as e:
        logger.error(f"Error processing API request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500
    
    
@app.route('/api/DbManager' , methods=['POST'])
def DbProcessor():
    db = Manager()
    
    try:
        data = request.get_json()
        query = data['query']
        supa = db.get_supabase_client()    
        print("Effds")
        songs_dict =  supa.table('Home_song').select("*").ilike("singer" , f'%{query}%').execute()
        print(songs_dict.data)
        return jsonify({"status": "success", "data": songs_dict.data}), 200
    except Exception as e:
        logger.error(f"Error processing API request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500
    
    
    
    
    
if __name__ == '__main__':

    app.run(debug=True, port=5001)

