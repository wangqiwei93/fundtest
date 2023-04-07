import requests

url = "https://yzw.corptssl.com/stage-api/fundAtlas/getDetail"

payload={'city': '杭州市'}

headers = {
  'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJqaW5rb25nIiwibG9naW5fdXNlcl9rZXkiOiJhMjJjZTAyMS1lODNkLTRhMmItOWQ4ZC1jOWQ5NzE3ZThkNGUifQ.bbDe0xbhEovdWKFgPEWjTuWFCiZn9kU_ORi1_-T1MB5xOEbOoYfj6Fqr7a3MKDy8zgBNPtNjk5v3EqxpYpQcfg'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

