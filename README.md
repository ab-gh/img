# img

## what this project is

This is my submission for the cs50 web Capstone project.

It provides a Django RESTful API and web app for uploading, viewing, sharing, and commenting on photos - in much the same vein as sites like Imgur or Flickr, but with a focus on profiles and portfolios.

The project consists of two Django apps, `api` and `web`.

### `api`

The `api` app serves as the RESTful API, at `/api` with the following routes:

**`/image/<id>`**
- returns the image and metadata for the given image ID

**`/tag/<id>` / `/tag/<name>`**
- returns all the images with the given tag

**`/search`**
- searches Public posts with given parameters

### `web`

The `web` app serves as the responsive react web client

