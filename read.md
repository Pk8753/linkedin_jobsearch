#Welcome to Linkedin's job search using web scrapping and selenium without login into linkedin.

### -> Dependecies you would need to it to install.

    1. pip3 install bs4
    2. pip3 install openpyxl
    3. pip3 install unittest
    4. pip3 install selenium

### -> Steps to use this application.
    1. goto Driver folder, open excel file name "input.xlsx"
    2. input your job role and job location and save it. fill only one row.
    3. goto terminal run below command
        #/> python3 test_jobSearch.py
    4. once test has run successfully, you can see the test reports in Reports folder.
    5. Job Search data will be availbale in JobSeeker.xlsx file under Result folder with HyperLink of job.
