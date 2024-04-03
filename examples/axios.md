## Simple example using the library Axios.js

```javascript
const axios = require('axios');

// Replace "kremilly" with your GitHub username
axios.get('https://gh-pin.kremilly.com/api?user=kremilly')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
```

### Install the library

To install the library, execute this

```shell
npm install axios
```
