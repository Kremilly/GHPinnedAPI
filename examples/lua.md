## Simple example using Lua

```lua
local http = require("socket.http")
local json = require("json")

-- Replace "kremilly" with your GitHub username
local url = "https://gh-pinned-api.vercel.app/api?user=kremilly"
local response, status = http.request(url)

if status == 200 then
    local data = json.decode(response)
    print(data)
else
    print("Error fetching data:", status)
end
```

### Install the libraries

To install the libraries, execute this

```shell
luarocks install luasocket
luarocks install dkjson
```
