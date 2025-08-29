from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
import requests
import json
import os

load_dotenv()

class OutlookMail():

    def __init__(self, Authorization: str, start_date: datetime, end_date: datetime, num_of_msgs: int=5, content_type: str='application/json') -> None:
        self.Authorization = Authorization
        self.content_type = content_type
        self.start_date = start_date
        self.end_date = end_date
        self.headers={'Authorization': self.Authorization, 'Content-Type':self.content_type}
        self.url = self.create_request()
        self.num_of_msgs = num_of_msgs
    
    def create_request(self) -> str:
        created_url = (
            f"https://graph.microsoft.com/v1.0/me/messages"
            f"?$filter=receivedDateTime ge {self.start_date} and receivedDateTime le {self.end_date}"
        )
        return created_url
    
    def return_messages(self) -> pd.DataFrame:
        response = requests.get(url=self.url, headers=self.headers)
        messages = response.json()
        # return messages
        # return self.url

        if str(response.status_code).startswith('4'):
            return pd.DataFrame({'Status Code': [messages['error']['code']], 'Status Message': [messages['error']['message']]})
        
        msgs_df = pd.DataFrame()
        for i in range(0, self.num_of_msgs, 1):
            temp_msgs_df = pd.DataFrame(
                {
                    'receiving_date': [messages['value'][i]['createdDateTime']],
                    'emailAddress': [messages['value'][i]['sender']['emailAddress']['address']],
                    'subject': [messages['value'][i]['subject']]
                }
            )
            msgs_df = pd.concat([msgs_df, temp_msgs_df])
            msgs_df.reset_index(drop=True, inplace=True)
        return msgs_df


Authorization = 'Bearer ' + os.getenv('client_token')
# Authorization = 'Bearer fake_token'
outlook = OutlookMail(Authorization=Authorization, start_date='2025-08-22T23:59:59Z', end_date='2025-08-29T23:59:59Z')
print(outlook.return_messages().head())


# outlook.head()
# print(url)

