## Simple example using Python

```python
import requests

# Replace "kremilly" with your GitHub username
response = requests.get('https://gh-pin.kremilly.com/api?user=kremilly')
data = response.json()

print(data)
```

### Install the library

To install the library, execute this

```shell
pip install requests
```
