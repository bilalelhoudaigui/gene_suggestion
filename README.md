## Gene Suggestion API

Tiny gene suggestion Api that connect to ensembl SQL database and returns a list of suggested gene names for the given query and target species.

### Installation

> Python version used is 3.7.2, please if you have both puthon 2.x and 3.x on your OS, use `python3` instead of `python` (e.g. `python3 -m venv venv`)

    # clone the repository
    $ git clone https://github.com/....
    $ cd gene_suggestion

Create a virtualenv:

    $ python -m venv venv

If you're on Ubuntu, you may need to install python3-env, if it's not already installed (`sudo apt-get install python3-venv`)

Then Activate it:

    $ . venv/bin/activate

Or on Windows cmd:

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install dependencies:

    $ pip install -r requirements.txt


### Run

    $ python api.py run

* Swagger UI: http://127.0.0.1:5000/api/v1
* GET Request example:
    * curl: `curl -X GET "http://localhost:5000/api/v1/gene_suggest?query=BRC&specie=homo_sapiens&limit=10" -H  "accept: application/json"` 
    * URL: http://localhost:5000/api/v1/gene_suggest?query=BRC&specie=homo_sapiens&limit=10

### Test

    $ python api.py test

Run with coverage report:

    $ coverage run --source app -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser

### Using Makefile (tested on Ubuntu)

The `makefile` can be used to automate the processes mentioned above, here are the commands:

`make install` : installs both system-packages and python-packages
`make clean` : cleans up the app
`make tests` : runs the all the tests
`make run` : starts the application
`make all` : performs clean-up, installation, run tests, and starts the application.