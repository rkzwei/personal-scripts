import os
import re
import requests

def download_file(url, folder_path, index):
    response = requests.get(url)
    if response.status_code == 200:
        file_extension = url.split(".")[-1]
        file_name = f"{folder_path}_{index}.{file_extension}"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download: {url}")

def main():
    # Get input from the user
    user_input = input("Enter text containing links: ")

    # Create a folder to save the downloaded files
    folder_name = "downloaded_files"
    os.makedirs(folder_name, exist_ok=True)

    # Define a regex pattern to match URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # Find all matches in the input
    links = re.findall(url_pattern, user_input)

    # Download files
    for index, link in enumerate(links, 1):
        download_file(link, folder_name, index)

    print(f"All files downloaded and saved in the '{folder_name}' folder.")

if __name__ == "__main__":
    main()
