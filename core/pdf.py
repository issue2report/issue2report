import glob
from md2pdf.core import md2pdf
from PyPDF2 import PdfFileMerger

class PDF(object):
    def __init__(self,output_dir,t):
        self.output_dir = output_dir
        self.t = t

    def get_all_pdfs(self,):
        management_dict = {}
        pdf_list = [f for f in glob.glob(self.output_dir + "/*[0-9]-*.pdf", recursive=True)]
        for item in pdf_list:
            splitted = item.split('-', 1)
            management_dict[int(splitted[0].replace('output/', ''))] = splitted[1]
        pdf_list = []
        for k, v in management_dict.items():
            pdf_list.append('output/{}-{}'.format(k, v))
        
        return pdf_list

    def merge_all_pdfs(self,report_name):
        pdfs = self.get_all_pdfs()
        pdfs = self.t.add_template_pdfs(pdfs)
        pdfs.remove(self.output_dir + "/cover.pdf")
        pdfs.remove(self.output_dir + "/intro.pdf")
        pdfs.remove(self.output_dir + "/conclusion.pdf")
        pdfs.insert(0, self.output_dir + "/cover.pdf")
        pdfs.insert(1, self.output_dir + "/intro.pdf")
        pdfs.append(self.output_dir + "/conclusion.pdf")
        merger = PdfFileMerger()
        for pdf in pdfs:
            merger.append(pdf)
        merger.write(report_name)
        merger.close()

    def md_to_pdf(self,pdf_file,body,css_file_path):
        md2pdf(pdf_file, md_content=body, md_file_path=None, css_file_path=css_file_path, base_url=None)
