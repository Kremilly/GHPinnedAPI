## Simple example using Go

```go
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	// Replace "kremilly" with your GitHub username
	url := "https://gh-pinned-api.vercel.app/api?user=kremilly"

	response, err := http.Get(url)
	if err != nil {
		fmt.Printf("Error fetching data: %s\n", err)
		return
	}
	defer response.Body.Close()

	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Printf("Error reading response body: %s\n", err)
		return
	}

	fmt.Println(string(body))
}
```
