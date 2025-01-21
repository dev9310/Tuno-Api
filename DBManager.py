from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import time
import logging
from supabase import create_client

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Manager:
    def __init__(self):
        self.supabase_url = os.getenv('SUPABASE_URL', 'default_supabase_url')
        self.supabase_key = os.getenv('SUPABASE_API', 'default_supabase_key')
        self.supabase = self.get_supabase_client()


    def get_supabase_client(self):
        return create_client(self.supabase_url, self.supabase_key)

    def fetch_data(self):
        """
        Fetches data from Supabase table `Home_song` and returns it as a JSON-like dict.
        """
        supabase = self.get_supabase_client()
        try:
            response = supabase.table("Home_song").select("*").limit(10).execute()
            if 'error' in response:  # Adjusted to check for 'error' in the response
                logger.error(f"Supabase Error: {response['error']}")
                return {"error": response['error']}
            
            return response.data  # Return the raw data
        
        
        except Exception as e:
            logger.error(f"Unexpected error fetching data: {e}")
            return {"error": "Internal server error"}
        
        
def get_supabase_client():
    supabase_url = os.getenv('SUPABASE_URL', 'default_supabase_url')
    supabase_key = os.getenv('SUPABASE_API', 'default_supabase_key')
    return create_client(supabase_url, supabase_key)







