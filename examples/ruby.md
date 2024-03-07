## Simple example using Ruby

```ruby
require 'net/http'
require 'json'

# Replace "kremilly" with your GitHub username
url = URI('https://gh-pinned-api.vercel.app/api?user=kremilly')
response = Net::HTTP.get(url)
data = JSON.parse(response)

puts data
```

### Install the libraries

To install the libraries, execute this

```shell
gem install net-http
gem install json
```
