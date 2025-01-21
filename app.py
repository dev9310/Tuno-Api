from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from DBManager import Manager
from Scarpper import SearchResult

app = Flask(__name__)
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


@app.route("/")
def Home():
    return "Welcome to the API Home Page"

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
    

@app.route('/api/artist/songs', methods=['POST'])
def fetchSongsByArtist():
    db = Manager()
    
    try:
        data = request.get_json()
        if 'query' not in data:
            return jsonify({"status": "error", "message": "Query parameter missing"}), 400
        
        query = data['query']
        supa = db.get_supabase_client()
        print(f"Fetching data from Supabase... for query{query}")
        songs_dict = supa.table('Home_song').select("*").ilike("singer", f'%{query}%').execute()
        singer_detail =  supa.table('Home_singer').select("*").ilike("name" , f"%{query}%")
        print(songs_dict.data)
        return jsonify({"status": "success", "data": songs_dict.data , "singer":singer_detail }), 200
    except Exception as e:
        logger.error(f"Error processing API request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run()
