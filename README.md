# Run App Localy

## Creating a virtual environment in Windows

1. Open a command prompt and navigate to the directory where you want to create the virtual environment.
2. Type `python -m venv .venv` and press Enter.
3. To activate the virtual environment, type `.venv\Scripts\activate` and press Enter.
4. You can now install packages and run your Python code within the virtual environment.
5. To install requirements, type `python -m pip install -r requirements.txt`
6. To deactivate the virtual enviroment, type `deactivate`

## Local Containers

1. Create image orchestratos: `docker build -t orch_app orchestrator`
2. Create and run container: `docker run -d -p 3000:3000 -e USERS_PATH=host.docker.internal:3001 orch_app`
3. Create image users: `docker build -t users_app users`
4. Create and run container: `docker run -d -p 3001:3001 -e DATABASE_URL=... users_app`
