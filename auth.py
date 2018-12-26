from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import os.path

def auth():
    scopes=['https://www.googleapis.com/auth/photoslibrary',
            'https://www.googleapis.com/auth/photoslibrary.sharing',
            'https://www.googleapis.com/auth/drive']
    flow = InstalledAppFlow.from_client_secrets_file('client_id.json' , scopes=scopes)
    # (authorization_prompt_message="") will not ask everytime
    # (prompt='consent') will ask every time
    credentials = flow.run_local_server(host='localhost',
                                        port=8080,
                                        prompt='consent',
                                        success_message='compelete.',
                                        open_browser=True)
    print("refresh_token : " , credentials.refresh_token)
    f = open('local.properties' , "w")
    f.write("client_id = " + credentials.client_id + '\n')
    f.write("client_secret = " + credentials.client_secret + '\n')
    f.write("refresh_token = " + credentials.refresh_token + '\n')
    return credentials

def main():
    auth()

if __name__ == '__main__':
  main()
