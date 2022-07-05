import requests
from typing import Dict, List

base_api_url = "https://api.github.com/"

def getUserInfo(username : str) -> Dict:
    if not username:
        return {"avatar_url" : "", "login": ""}
    url = base_api_url+"users/"+username
    try:
        response = requests.get(url).json()
    except Exception as e:
        raise(e)
    
    return {"avatar_url" : response["avatar_url"], "login" : response["login"]}

def cleanData(data):
    for row in data:
        #remove unused info
        row.pop("id")
        row.pop("node_id")
        row.pop("full_name")
        row.pop("private")
        row.pop("owner")
        row.pop("html_url")
        row.pop("fork")
        row.pop("url")
        row.pop("forks_url")
        row.pop("keys_url")
        row.pop("collaborators_url")
        row.pop("teams_url")
        row.pop("hooks_url")
        row.pop("issue_events_url")
        row.pop("events_url")
        row.pop("assignees_url")
        row.pop("branches_url")
        row.pop("tags_url")
        row.pop("blobs_url")
        row.pop("git_tags_url")
        row.pop("git_refs_url")
        row.pop("trees_url")
        row.pop("statuses_url")
        row.pop("languages_url")
        row.pop("stargazers_url")
        row.pop("contributors_url")
        row.pop("subscribers_url")
        row.pop("subscription_url")
        row.pop("commits_url")
        row.pop("git_commits_url")
        row.pop("comments_url")
        row.pop("issue_comment_url")
        row.pop("contents_url")
        row.pop("compare_url")
        row.pop("merges_url")
        row.pop("archive_url")
        row.pop("downloads_url")
        row.pop("issues_url")
        row.pop("pulls_url")
        row.pop("milestones_url")
        row.pop("notifications_url")
        row.pop("labels_url")
        row.pop("releases_url")
        row.pop("deployments_url")
        row.pop("git_url")
        row.pop("ssh_url")
        row.pop("clone_url")
        row.pop("svn_url")
        row.pop("homepage")
        row.pop("updated_at")
        row.pop("has_issues")
        row.pop("has_projects")
        row.pop("has_downloads")
        row.pop("has_wiki")
        row.pop("has_pages")
        row.pop("mirror_url")
        row.pop("disabled")
        row.pop("open_issues_count")
        row.pop("allow_forking")
        row.pop("is_template")
        row.pop("web_commit_signoff_required")
        row.pop("visibility")
        row.pop("open_issues")
        row.pop("default_branch")
        row.pop("score")

        #remove redundant info
        row.pop("stargazers_count")
        row.pop("watchers_count")
        row.pop("forks_count")

        #row["license"] = row["license"]["name"]
    return data

def getRepos(username : str, params : List[Dict] = [{}]) -> Dict:

    if not username :
        return {} 
    url = base_api_url+"search/repositories?q=user:" + username
    for param in params:
        if len(param):
            url += " "
            if param["operator"] == "==":
                url += param["field"] + ":" + param["value"]
            elif param["operator"] == "contains":
                url += param["value"] + " in:" + param["field"]
            elif param["operator"] in [">","<",">=","<="]:
                url += param["field"] + ":" + param["operator"] + param["value"]
    #url = requests.utils.quote(url)
    print(url)
    try:
        response = requests.get(url).json()
    except Exception as e:
        raise(e)
    return cleanData(response["items"])

def formatFilters(filters : str) -> List [ Dict ] :
    splited_filter = filters.split(",")
    res = list()
    for query in splited_filter:
        splited_query = []
        operator = ""
        if ">=" in query:
            operator = ">="
            splited_query = query.split(">=")
        elif "<=" in query:
            operator = "<="
            splited_query = query.split("<=")
        elif ">" in query:
            operator = ">"
            splited_query = query.split(">")
        elif "<" in query:
            operator = "<"
            splited_query = query.split("<")
        elif "==" in query:
            operator = "=="
            splited_query = query.split("==")
        elif "contains" in query:
            operator = "contains"
            splited_query = query.split("contains")
        else:
            raise Exception("wrong operator")
        
        res.append({"field": splited_query[0].strip(), "operator": operator, "value": splited_query[1].strip() })
    return res