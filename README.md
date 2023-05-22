# FullStack project
> Simple python/html/js project to improve FullStack skills.


## Technologies Used
- fastapi - version 0.95.2
- Jinja2 - version 3.1.2
- pydantic - version 1.10.7
- python-multipart - version 0.0.6
- uvicorn - version 0.22.0



## Setup
Python version 3.10. All project requirements stored in the root directory. 


## Usage
Create virtual environment and install all dependency. Next step the is to run the main.py script.
Here is an example of simple requests to this web application  
- `http://127.0.0.1:8000/` Hello world welcome page
- `http://127.0.0.1:8000/get_problem/problem_name` Gives a list of tasks for training in a certain section. (problem_name must be changed to an existing partition name)
- `http://127.0.0.1:8000/view_problem/1` Shows a description of a specific task and input conditions. It also displays an input field and gives an opportunity to make a correct input, which will later redirect to the page with the answer. (The parameter is currently a stub and must be a number)