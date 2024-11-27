import requests
import subprocess
import re

def request_page(url):
    """Returns the HTML of the url requested."""
    response = requests.get(url)
    html_content = response.text
    return html_content

def ping(host_url):
    pingg = subprocess.Popen(
        ["ping", "-c", "1", host_url],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, error = pingg.communicate()
    match = re.search(r'time=(.*?) ms', str(out))
    if match:
        return (float(match.group(1)))  # Extract the time value and convert it to an integer
    else:
        return None

def indef_calc():
    while True:
        print(eval(input(" : ")))