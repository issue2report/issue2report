#!/usr/bin/python3

import json

class Template(object):
    def __init__(self,template_name,output_dir,g):
        self.g = g
        self.output_dir = output_dir
        self.template_name = template_name
        self.info = json.loads(open("templates/{}/info.json".format(self.template_name),"r").read().strip())

    def get_frozen_opts(self,):
        template = self.info
        for k,v in template["frozen_opts"].items():
            template["frozen_opts"][k] = self.g.get_file(v)
        return template["frozen_opts"]

    def get_pages(self,):
        return self.info["pages"].values()

    def add_template_pdfs(self,pdfs):
        for k,v in self.info["pages"].items():
            if int(k) < 0:
                k = (len(pdfs) + 1) - abs(int(k))
            pdfs.insert(int(k),"{}/{}.pdf".format(self.output_dir,v))
        return pdfs
