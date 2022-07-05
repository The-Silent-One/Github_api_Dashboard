# Github_api_Dashboard

This project uses [flask](https://flask.palletsprojects.com/en/2.1.x/) (python)  to run querries on [github search api](https://docs.github.com/en/search-github) and displays them in a dashboard

## How to use
First, you need [docker](https://www.docker.com) installed on your machine and that's all.
Then run the command 
> ./run.sh

You'll find the app running on [localhost](http://127.0.0.1)
Type the github name in question and see their repos listed below in a table. You can filter on the data by typing your own filter.
For example:
> followers >= 10

This filter will return all the repos with at least one follower/watcher
For more info on filtering, you can consult the [documentation](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)