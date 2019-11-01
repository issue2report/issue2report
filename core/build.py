import json
from core.pdf import PDF
from core.github import Github

class Build(object):
    def __init__(self,output_dir,frozen_opts,p,g,t):
        self.p = p
        self.g = g
        self.t = t
        self.output_dir = output_dir
        self.frozen_opts = frozen_opts

    def replaces(self,content):
        for k,v in self.frozen_opts.items():
            content = content.replace(k,v)
        return content

    def build_templates(self,customer):
        for page in self.t.get_pages():
            md = self.replaces(open("templates/{}/{}.md".format(self.t.template_name,page),"r").read())
            self.p.md_to_pdf(self.output_dir + "/{}.pdf".format(page),md,"templates/{}/{}.css".format(self.t.template_name,page))

    def generate_report_md(self,issue):
        body = []
        body.append("# {}".format(issue["title"]))
        body.extend(self.g.get_labels(issue["labels"]))
        body.append(issue["body"])
        body.extend(self.g.get_comments_by_issue(issue["comments_url"]))
        return "\n".join(body)
