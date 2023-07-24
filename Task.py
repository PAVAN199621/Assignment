import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://pavan199621.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("pavan199621@gmail.com", "ATATT3xFfGF0i_tYHUYt_yCC_USYaplmRaqcERgyAcvK0WO-IkklewY5g1Xmfz4euDVwPFuA8IO5V0UuwiJN3pDh4jhwzHM32lX5Li61Mi9RKzmvkKeXH-6AlNkhryCkITh8J7G7j_kQHRvs4-4ViT-zovwQp9Vogr9h9GOmJR3kBw3ITKIApT0=995A379E")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
