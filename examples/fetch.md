## Simple example using Fetch

```javascript
// Replace "kremilly" for your GitHub username
fetch('https://api.kremilly.com/github?user=kremilly').then(
   json => json.json()
).then(callback => { 
   console.log(callback) 
})
```
