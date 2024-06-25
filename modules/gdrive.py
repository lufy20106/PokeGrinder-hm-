import os
import requests
from googleapiclient.discovery import build

# Replace with your API key
api_key = 'AIzaSyD1nlxaUKSfV60SPXbrPrqn65kdM2_68yw'

# Replace with your target folder ID in Google Drive (optional)
target_folder_id = '112ozvi8K5-tYyEyMW2LLfcgHuTZp-15X'

def upload_image_to_drive(image_url, custom_name):
    # Download the image from URL
    image_data = requests.get(image_url).content

    # Build the Drive API service
    drive_service = build('drive', 'v3', developerKey=api_key)

    # Prepare file metadata
    file_metadata = {
        'name': custom_name,
        'parents': [target_folder_id] if target_folder_id else []
    }

    # Upload the file to Google Drive
    media = drive_service.files().create(
        body=file_metadata,
        media_body=bytes(image_data),
        fields='id'
    ).execute()

    print(f"File '{custom_name}' uploaded successfully with ID: {media.get('id')}")