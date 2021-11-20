from serpwow.google_search_results import GoogleSearchResults
import json

serpwow = GoogleSearchResults("B86A0E267E6C4E2898DB140E4C7639A3")

def search(query):
    params = {
        "q": query
    }
    mylist = []
    result = serpwow.get_json(params)
    res = json.dumps(result, indent=2, sort_keys=True)
    try:
        mylist.append(result["organic_results"][0]["snippet"])
        return(mylist)
    except:
        mylist.append(result["organic_results"][0]["link"])
        mylist.append('')
        return(mylist)
