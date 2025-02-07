# JobTarget Mid-Level Project
### tools: FastAPI, Vue, Tailwind

### Local Development Setup
1. Clone this repo: `git clone https://github.com/kinga112/jobtarget-api-project`
2. Navigate to the local install directory and install the required python packages: `pip install requirements.txt`
    - *recommended*: Create a virtual environment using venv with Python 3.12.6
3. Run the API server using FastAPI in command prompt: `fastapi dev api.py`
4. In another cmd window, navigate to the `vue-app` directory and install the required npm packages: `npm install`
5. Run the vue development server: `npm run dev`

### Production Setup Suggestions
1. Containerize the FastAPI server with Docker using the official Python Docker image
2. Setup Uvicorn to run the production API instance on Docker
3. Containerize the Vue web application with Docker using the official Node.js Docker image
4. Setup Nginx to run the produciton Vue web application
5. Deploy the newly created Docker containers on AWS ECS for simplified container management in the cloud