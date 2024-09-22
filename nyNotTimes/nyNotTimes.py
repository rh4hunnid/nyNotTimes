import subprocess
from bs4 import BeautifulSoup, Comment
import webbrowser
import tempfile
import os
import argparse
import time

def main():

    parser = argparse.ArgumentParser(description='Process URL from user input.')
    parser.add_argument('url', type=str, help='The URL to fetch and process.')
    args = parser.parse_args()


    curl_command = ["curl", "-s", args.url]
    try:
        html_content = subprocess.check_output(curl_command).decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Failed to open URL: {e}")
        exit(1)


    soup = BeautifulSoup(html_content, 'html.parser')


    for script in soup.find_all('script'):
        script.decompose()


    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()


    cleaned_html = soup.prettify()


    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
        temp_file.write(cleaned_html.encode('utf-8'))
        temp_file_path = temp_file.name


    webbrowser.open(f"file://{os.path.abspath(temp_file_path)}")


    time.sleep(5)


    try:
        os.remove(temp_file_path)
    except OSError as e:
        print(f"Error deleting temporary file: {e}")

if __name__ == '__main__':
    main()
