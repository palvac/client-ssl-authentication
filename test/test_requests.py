import requests

url = "https://localhost/api/"

cert_path = "/Users/daniel.mbaluka/work/research/app/devops/ssl/client/client.crt"
key_path = "/Users/daniel.mbaluka/work/research/app/devops/ssl/client/client.key"
response = requests.post(
    url=url,
    cert=(cert_path, key_path),
    verify=False
)

print("status code: {}".format(response.status_code))
print("content: {}".format(response.content))