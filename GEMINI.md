This project is a monorepo containing a python backend with FastApi and an Angular 19 frontend.

## Backend
- To install dependencies in the backend use `uv add`, not `uv pip install`
- To run tests, go in the backend directory and run `uv run pytest`
- Never use pip
- Never try to activate the virtual environment, uv does it for you

## Frontend
- Every component is standalone by default, do not try to add standalone: true everywhere
- Do not use ngIf and ngFor, use @if and @for
- Use signals when possible

## General instructions
- Keep the context clean and small :
  - If you fail to execute a command, do not apologize or add anything that does not add value or information
  - Do not make elaborate sentences, just use bullet points with key information
  - If you want to add a lib, justify your choice, be concise
 