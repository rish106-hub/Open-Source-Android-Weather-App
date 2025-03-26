import requests
import logging

def get_olid(title, author):
    """Get Open Library ID for a book"""
    try:
        response = requests.get(
            "https://openlibrary.org/search.json",
            params={
                "title": title,
                "author": author
            }
        )
        response.raise_for_status()
        data = response.json()
        
        # Ensure we have at least one valid result
        if not data.get('docs'):
            logging.warning(f"No results found for {title} by {author}")
            return None
            
        olid = data['docs'][0]['olid']
        return olid
        
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error occurred: {str(e)}")
        return None
    except (ValueError, KeyError, IndexError) as e:
        logging.error(f"Data parsing error: {str(e)}")
        return None