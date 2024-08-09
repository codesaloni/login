from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import pickle
import json

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_user():
    creds = None
    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    #
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('app/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
      
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_event(start_time, end_time, specialty, doctor):
    
    creds = authenticate_user()
    service = build('calendar', 'v3', credentials=creds)

    
    event = {
        'summary': f"Appointment with Dr. {doctor}",
        'description': f"Specialty: {specialty}",
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
    }

    
    event_result = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {event_result.get('htmlLink')}")

def list_events():
    creds = authenticate_user()
    service = build('calendar', 'v3', credentials=creds)

    events_result = service.events().list(calendarId='primary', singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"{start} - {event['summary']}")


list_events()
