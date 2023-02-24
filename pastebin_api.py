import requests

DEVELOPER_KEY = 'fy8qxg9H8XXNXJKXHqv-5yVkoQHL3Ycg'
PASTEBIN_API_URL = 'https://pastebin.com/api/api_post.php'

def main():
    url = post_new_paste("this is a tittle", "this\nis\nthe body", '1H', True)
    print(f'new paste URL: {url}')
    
def post_new_paste(title, body_text, expiration='10M', listed=False):
    """Posts a new public paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional):Expiration date of paste (N= never, 10M= minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y). Defaults to '10'. 
        listed (bool, optional): Whether paste is publicly listed (True) or not (False). Defaults to false.

    Returns:
        str: URL of new paste, if successful. none if unsuccessful
    """
    # setup the parameters for the request message
    paste_params = {
        'api_dev_key': DEVELOPER_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1
    }
    
    # send the POST request to the PasteBin API
    print('sending post request to pasteBin API...', end='')
    resp_msg = requests.post(PASTEBIN_API_URL, data=paste_params)

    #check whethe the POST request was Successful
    if resp_msg.ok:
        print('success')
        return resp_msg.text
    else:
        print('failed')
        print(f'status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')
        
if __name__ == '__main__':
    main()