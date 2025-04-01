import requests
import json


class TumblrAPI:
    # api parameters
    # num:- default value of num is 20 and maximum is 50
    # start :- default value of post offset is 0.
    @staticmethod
    def create_api_url(blog_name: str, start_index: int, end_index: int) -> str:
        return (
            f"https://{blog_name}.tumblr.com/api/read/json?"
            f"type=photo&num={end_index - start_index + 1}&start={start_index - 1}"
        )


    @staticmethod
    def fetch_data(api_url: str) -> dict:
        try:
            response = requests.get(api_url)
            json_string = response.text.replace('var tumblr_api_read =', '').strip().strip(';')
            return json.loads(json_string)
        
        except requests.exceptions.RequestException as error:
            raise RuntimeError(f"Error fetching data from Tumblr API: {error}")
        
        except json.JSONDecodeError as error:
            raise RuntimeError(f"Error decoding JSON data: {error}")
