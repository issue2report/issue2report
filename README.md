# issue2report
Generate pentest reports based on github issues.

# Github Token
You need a [github token](https://github.com/settings/tokens) in order to use this tool. Save the token in the following file `.token`.

# Usage
First, run `pip3 install -r requirements.txt` (must be python3)

Then you should create a repository that will contain the information that will be written in the report files stored (Text and Issues). Here is an [example](https://github.com/issue2report/default-template/). **Make sure that the files contain the same name as the example repository**

Then execute using `python3 issue2report.py -t {{template folder name that can be found inside of the templates folder}} -gu {{your github username}} -gr {{github repository name}}`
Ex: `python3 issue2report.py -t default -gu johndoe -gr my_pentest_report`


# File Description
- **issue2report/.token** is your github token.
- **issue2report/templates/file.css** is the CSS configuration for the related file.
- **issue2report/templates/[conclusion, cover, intro, vulnerabilities].md** is the markdowns that you will edit the text to insert the information you want. This should be edited manually.
- **default-template/infos.json** contain the information about the company that was tested, your company and your name to be populated in the report.
- **default-template/[conclusion, resume, scope].md** is the markdowns that should be changed manually too.