# pdfThumb

Clone this respository:

```shell
git clone https://github.com/kremilly/ghPinnedAPI
```

Install the dependencies:

```shell
pip install -r requirements.txt
```

To run the server, use:

```shell
python index.py
```

## Example of request

```shell
https://gh-pinned-api.vercel.app/api?user=YOUR_USERNAME
```

## Queries Parameters

* `user`: Set the username
* `width`: Set the with of thumbnail
* `height`: Set the height of thumbnail
* `page`: Set the page number of file for generate thumbnail

## Dependencies

* Flask
* requests
* python-dotenv
