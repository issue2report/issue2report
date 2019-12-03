import json
import glob
import requests
from md2pdf.core import md2pdf
from PyPDF2 import PdfFileMerger

class Github(object):
    def __init__(self,token,username,repo):
        self.headers = {"Authorization" : "token {}".format(token),"Accept":"application/vnd.github.v3.raw", "state": "open"}
        self.username = username
        self.repo = repo
        self.base_url = "https://api.github.com"

    def get_issues_by_repo(self,):
        r = requests.get(self.base_url + "/repos/{}/{}/issues".format(self.username,self.repo),headers=self.headers)
        return r.json()

    def get_comments_by_issue(self,url):
        r = requests.get(url,headers=self.headers)
        comments = []
        for comment in r.json():
            comments.append(comment["body"])
        return comments

    def get_file(self,file_path):
        url = "{}/repos/{}/{}/contents/{}".format(self.base_url,self.username,self.repo,file_path)
        r = requests.get(url,headers=self.headers)
        return r.text

    def get_labels(self,labels):
        formatted_labels = []
        for label in labels:
            formatted_labels.append("<span style=\"background-color:#{};font-weight: bold;\">{}</span><br>".format(label["color"],label["name"]))
        return formatted_labels
