import pandas as pd
import numpy as np
import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

class JiraDetails():

    def __init__(self, token: str, url: str, email: str, project_name: str=None, issue_id: str=None) -> None:
        # authoraization = 'Bearer ' + self.token
        self.token = token
        self.url = url
        self.project_name = project_name
        self.email = email
        self.issue_id = issue_id
        self.auth = requests.auth.HTTPBasicAuth(self.email, self.token)
        self.headers = {"Accept": "application/json"}
        self.query = {'jql': f'project={self.project_name}'}

    def receive_projects_data(self):
        return requests.request(
            "GET",
            url=self.url,
            headers=self.headers,
            auth=self.auth
            # params=self.query
        ).text
    
    import requests

    def fetch_all_issues_from_project(self, project_key: str=None, base_url: str=None, max_results: int=1000):
        issues = []
        start_at = 0
        headers = {"Accept": "application/json"}
        auth = requests.auth.HTTPBasicAuth(self.email, self.token)

        while True:
            url = f"http://{base_url}/rest/api/3/search"
            params = {
                "jql": f"project={project_key}",
                "startAt": start_at,
                "maxResults": max_results
            }

            response = requests.get(url, headers=headers, auth=auth, params=params)
            if response.status_code != 200:
                print(f"Error: {response.status_code}")
                print(response.text)
                break

            data = response.json()
            issues.extend(data.get("issues", []))

            if start_at + max_results >= data.get("total", 0):
                break
            start_at += max_results

        return issues




api_key = os.getenv('jira-api-key')
base_url = os.getenv('base_url')
email = os.getenv('email')
# url = "https://jira-api-call.atlassian.net/rest/api/2/project"
# url = "http://jira-api-call.atlassian.net/rest/agile/1.0/issue/{issueIdOrKey}"


# Fetch due date for an issue
# epicIdOrKey = "JAC-1"
# issue_details_url = f"http://{base_url}/rest/agile/1.0/epic/{epicIdOrKey}/issue"
# jira = JiraDetails(token=api_key, url=issue_details_url, email=email)
# jira_details_dict = json.loads(jira.receive_projects_data())
# print(jira_details_dict["issues"][0]["fields"]["duedate"])


# Get changes made in an issuse details
issueIdOrKey = 'JAC-2'
issue_changelog_url = f"http://{base_url}/rest/api/2/issue/{issueIdOrKey}?expand=changelog"
jira = JiraDetails(token=api_key, url=issue_changelog_url, email=email)
# print(json.dumps(jira.receive_projects_data(), indent=4, sort_keys=True, separators=(",", ": ")))


# # Get all change histories
# changelog_df = pd.DataFrame()
# field, field_type, field_name, old_value, old_value_str, new_value, new_value_str, author = [], [], [], [], [], [], [], []
# assignee, epic_name = [], []
# issue_histories = json.loads(jira.receive_projects_data())["changelog"]["histories"]
# issue_changelog = json.loads(jira.receive_projects_data())["fields"]


# for i in range(len(issue_histories)):
#     try:
#         field_name.append(issue_histories[i]["items"][0]["fieldId"])
#         field.append(issue_histories[i]["items"][0]["field"])
#         field_type.append(issue_histories[i]["items"][0]["fieldtype"])
#         old_value.append(issue_histories[i]["items"][0]["from"])
#         old_value_str.append(issue_histories[i]["items"][0]["fromString"])
#         new_value.append(issue_histories[i]["items"][0]["to"])
#         new_value_str.append(issue_histories[i]["items"][0]["toString"])
#         author.append(issue_histories[i]["author"]["displayName"])
#         assignee.append(issue_changelog["assignee"]["displayName"])
#         epic_name.append(issue_changelog["parent"]["fields"]["summary"])
#     except (KeyError, IndexError):
#         continue

# changelog_df = pd.DataFrame({
#     'field': field,
#     'field_type': field_type,
#     'field_name': field_name,
#     'old_value': old_value,
#     'new_value': new_value,
#     'author': author,
#     'assignee': assignee,
#     'epic_name': epic_name
# })

# print(changelog_df)


# Fetch all issues from a project
jira = JiraDetails(token=api_key, url=issue_changelog_url, email=email)
print(jira.fetch_all_issues_from_project(project_key='JAC', base_url=base_url))

