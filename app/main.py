from flask import Flask, request, render_template
from githubapi import *
from typing import List, Dict

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def getUsernameForm():
    username = request.form["username"]
    filters = request.form["filters"]
    if username and filters:
        try:
            formated_filters = formatFilters(filters)
            return user_render(username = username, filters = formated_filters)
        except Exception as e:
            return render_template("error.html", exception=str(e))
    elif username and not(filters):
        return user_render(username = username)
    else:
        return render_template("error.html", exception=str(e))

@app.route("/", methods = ["GET"])
def user_render(username : str = "", filters : List [ Dict ] = [{}]):
    try:
        if not username:
            return render_template("repos.html", header=[], data=[], image_source="", username="")    
        
        user_info = getUserInfo(username)
        user_image = user_info["avatar_url"]
        username = user_info["login"]

        data = getRepos(username, filters)
        # print("************")
        # print(data)
        # print("************")
        header = data[0].keys()
        return render_template("repos.html", header=header, data=data, image_source=user_image, username=username)
    except Exception as e:
        return render_template("error.html", exception=str(e))


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)