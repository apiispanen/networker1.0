import requests
from bs4 import BeautifulSoup
import json

import difflib

def google_it(search_term, other_info=""):
    search_term = search_term.replace(' ', '%20')
    other_info = other_info.replace(' ', '%20')+'%20"linkedin"'
    print(search_term)
    url = f"https://www.google.com/search?q={search_term}%20{other_info}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    search_results = soup.find_all("div", class_="g")
    if search_results:
        first_result = search_results[0]
        title = first_result.find("h3").get_text()
        url = first_result.find("a")["href"]
        # print(f"Title: {title}")
        # print(f"URL: {url}")
        return title
    else:
        print("No search results found.")
        return None

# Based on an input string that includes json, clean the string to output the JSON:
def get_json(input_string):
    start_index = input_string.find('{')

    # Find the index of the last '}' character
    end_index = input_string.rfind('}')

    # Extract the JSON portion of the string
    json_string = input_string[start_index:end_index+1]

    # Parse the JSON string into a Python object
    print(json_string)
    data = json.loads(json_string)
    return data

# Based on an input of a name, return the json of this person's info:
def json_pull(name, filename="conversations.json"):
    # Load the existing data from the file
    with open(filename, "r") as f:
        data = json.load(f)

    name_list = list(data["People"].keys())
    search_name = name

    closest_match = difflib.get_close_matches(search_name, name_list, n=1, cutoff=.4)
    if closest_match:
        print("We are assuming '", search_name, "' is", closest_match[0])
        print(data["People"][name])
        result = data["People"][name] 
    else:
        print("No match found for", search_name)
        result = "None given"
    
    return result

# Based on an input including name & JSON of the conversation, update the appropriate fields in their JSON: 
def json_update(name, json_response, filename="conversations.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    conversation_json = get_json(json_response)
    name_list = list(data["People"].keys())
    closest_match = difflib.get_close_matches(name, name_list, n=1, cutoff=.4)
    if closest_match:
        print("We are assuming '", name, "' is", closest_match[0])
        # print(data["People"][name])
        for key in conversation_json['People'][name]:
            data['People'][closest_match[0]][key] = conversation_json['People'][name][key]
    else:
        print("No match found for ", name, "Adding new entry")
        data["People"][name] = conversation_json['People'][name]
        

    # Write the updated data back to the file
    with open("conversations.json", "w") as f:
        json.dump(data, f, indent=4)


conversation_json = """{   "People":{
            "John Doe": {
            "School": "Bunker Hill",
            "Location": "Boston, MA",
            "Interests":"Painting",
            "Fun Facts":"Skiied in the alps" }}}"""

json_update("John Doe", conversation_json)



    



# json_pull("Sam Casey")

# conversation = """
# {   "People":
#             "[PERSONS NAME]": {
#             "School": "",
#             "Location": "",
#             "Interests":"",
#             "Fun Facts":"",
#             "Previous Conversations":{} }}



#  Sam Casey:

#     School: UC Berkeley
#     Location: San Francisco, CA
#     Interests: Hiking, reading, and spending time with Penny, his dog
#     Fun Facts: I once hiked the entire Pacific Coast Trail!
#     Previous Conversations: We talked about how much we love our dogs """

# json_log(conversation)