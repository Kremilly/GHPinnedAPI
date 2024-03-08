## Simple example using Fetch

```javascript
// Replace "kremilly" for your GitHub username
fetch('https://gh-pinned-api.vercel.app/api?user=kremilly').then(
   json => json.json()
).then(callback => { 
   console.log(callback) 
})
```
