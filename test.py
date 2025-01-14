import requests

def check_huggingface_api_key(api_key):
    try:
        API_URL = "https://api-inference.huggingface.co/models/gpt2"
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(API_URL, headers=headers)

        if response.status_code == 200:
            print("API key is valid!")
        else:
            print(f"Invalid API key. Status code: {response.status_code}")
            print("Details:", response.json())

    except Exception as e:
        print("An error occurred:", str(e))

# Replace 'your_api_key' with your actual Hugging Face API key
your_api_key = "YOUR API KEY HERE"
check_huggingface_api_key(your_api_key)
