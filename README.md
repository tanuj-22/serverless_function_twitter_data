
# Serverless Function for Twitter Data 

 A serverless function written in Python and Flask to retrieve Twitter data such as trends, search queries, and hashtags, as well as user information.

## Demo
#### Function Deployed on Vercel
https://twitterdata.vercel.app/


## API Reference

#### Get Trends

```https
  GET /gettrends
```

#### Search Query

```https
  GET /search?query=<your_query>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `query`      | `string` | **Required**.  |

 For query involving space use + instead of space


#### Search User

```https
  GET /user?username=<your_username>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**.  |


#### Search Hashtag

```https
  GET /hashtag?query=<your_query>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `query`      | `string` | **Required**. Do Not Include # |


## Run Locally

Clone the project

```bash
  git clone https://github.com/tanuj-22/serverless_function_twitter_data.git
```

Go to the project directory

```bash
  cd serverless_function_twitter_data
```

Install dependency vercel-cli

```bash
  npm i -g vercel
```
Run local server

```bash
  vercel dev
```
## Deployment

To deploy this project run

```bash
  vercel deploy
```

