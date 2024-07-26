import os
import requests
from datetime import datetime
from PIL import Image
from io import BytesIO
import time

# Replace 'your_username' with your actual Windows username
username = 'tvanpelt'

# Define the target directory
target_directory = f'C:/users/{username}/pictures/'

# Create the 'pictures' folder if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Counter to keep track of the image number
image_counter = 1

while True:
    # Get the current date and format it as "ddmonyy"
    current_date = datetime.now()
    formatted_date = current_date.strftime('%d%b%y').lower()
    
    # Construct the URL
    url = 'https://soho.nascom.nasa.gov/data/realtime/hmi_igr/1024/latest.jpg'
    
    # Send a request to the URL
    response = requests.get(url)
    
    if response.status_code == 200:
        # Open the image using PIL
        image = Image.open(BytesIO(response.content))
        
        # Construct the filename with an incrementing counter
        filename = '{}_sun_{}.jpg'.format(formatted_date, image_counter)
        image_counter += 1
        
        # Save the image to the 'pictures' folder
        image.save(os.path.join(target_directory, filename))
        print(f"Image saved as {filename}")
    else:
        print("Failed to fetch the image")
    
    # Sleep for 60 minutes (3600 seconds) before the next capture
    time.sleep(3600)
