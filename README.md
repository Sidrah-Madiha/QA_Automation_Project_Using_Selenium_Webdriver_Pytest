# QA-Automation-Project-using-Selenium-Webdriver-and-Pytest
This project automates test cases for testing website "duckduckgo.com" search functionality.

## DEMO OF AUTOMATED TEST RUN ON CHROME BROWSER:

https://www.loom.com/share/7ca1114499734d95a0ba26e10815e0bc


## Test case for automation:
Following scenarios are automated and these are also written in Gherkin and can be found in file named as `"testcases in gherkin.txt"`:

1. Basic DuckDuckGo Search with enter key press
2. Basic DuckDuckGo Search with search button click
3. Clicking a search link
4. "More Result" button check
5. Autocomplete suggestions pertains to search query
6. Search using autocomplete suggestion
7. Do an image search

## Project Setup
1. Clone this repository.
2. Run cd tau-intro-selenium-py to enter the project.
3. Run pipenv install to install the dependencies.
4. Run pipenv run python -m pytest to verify that the framework can run tests.
5. Create a branch for your code changes. 

**Issues while installing project**


If encountered with the following error when executing `pipenv run python -m pytest`:

`ModuleNotFoundError: No module named 'atomicwrites'`
I'm not exactly sure why pipenv install does not include atomicwrites. So far, I have seen it happen only on Windows. To resolve the error, please attempt the following:

1. Upgrade Python to the latest versions. The following worked for me on Windows:
- Python 3.8.3 (python --version)
- pip 20.1 (pip --version)
- pipenv 2018.11.26 (pipenv --version)
- Run pipenv update from within the project directory.
If upgrades don't work, try forcing package installation:

2. Run pipenv install pytest from within the project directory.
3. Run pipenv install atomicwrites from within the project directory.
If these steps don't work in your project, then try to run without pipenv:

1. Install Python packages directly using pip.
2. Run tests directly using python -m pytest.


## Possible Future Improvements:

- Testing tests on firefox, headless chrome to see for any flaky tests.
- Optimizing code for performance, replacing implicit waits and sleeps with explicit waits
- Check test run on parallel threads
