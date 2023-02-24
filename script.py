from pastebin_api import post_new_paste
from dad_jokes_api import search_for_dad_jokes
import sys

def main():
    search_term = get_search_term()
    joke_list = search_for_dad_jokes(search_term)
    if joke_list:
        title, body_text = get_paste_data(joke_list, search_term)
        paste_url = post_new_paste(title, body_text, '1M')
        print (f'URL of new paste: {paste_url}')
        
def get_search_term():
    num_params = len(sys.argv) - 1
    if num_params > 0:
        return sys.argv[1]
    else: 
        print("error: Missing search term")
        sys.exit(1)
        
def get_paste_data(joke_list, search_term):
    title = f'Dad Jokes that conatin the word "{search_term}"'
    divider = '\n' + ('*' * 40) + '\n'
    body_text = divider.join(joke_list)
    return title, body_text

if __name__ == '__main__':
    main()