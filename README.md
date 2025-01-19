# ASPIRE Backend Developer Take-home Assignment

If you're reading this, it means you are being considered for a Backend Developer position on the ASPIRE project. This position involves blending your talents as a backend web developer and AI-researcher to create integrated, LLM-powered services for the students and staff of UCSD. To demonstrate your skills, this repo has been constructed as a shrunk down and simplified form of the ASPIRE application, utilizing much of the tech-stack, patterns, database tables, and data as the real thing. For context, ASPIRE is an application mapping course contents, tracking student knowledge, and facilitating various educational aids or interventions, the ultimate goal being to improve student outcomes university wide. All of these systems involve one or several LLM integrations to assist in or automate the process, your task is to create and integrate one of these LLM integrations and offer it as a service via an API endpoint. 

More specifically, you have been provided with tables and data representing a course's domain, this includes some of the concepts taught in an 'Introduction to Python' course, the relationships between those concepts (concept_a is prerequisite to learning concept_b), the modules or 'concept_collections' of the course, and the junctions connecting concepts to the modules they belong to. Unfortunately, the professor forgot to write a summary for their modules. On top of being a handy reference, this summary is useful context for the LLM when performing actions related to the contents of the module, luckily, most concepts do have their own content summary. Using the data and tables provided to you, we would like you to create and integrate a service that generates a summary of the contents of a module, and then updates the matching 'concept_collection' database entry with that summary. Your service should be accessible via a corresponding API endpoint and conform to the repository's preexisting hexagonal architecture and protocols. The methods and data you use to complete this task are up to you, some basic services and database interfaces have been provided as examples, but you are free to modify these or create new ones as required. 

**You will be given 24 hours to complete this task. If you do not complete the task in time, you will NOT be immediately disqualified, push what you have at the 24-hour mark and feel free to try and complete the task taking any additional time required. Make sure to push any and all work you've completed to a public repo shared with us.**

*Best of luck to you!*

## Quick Start Guide
### Key Dependencies & Technologies
- Python 3.11
- PostgreSQL 16.2
- FastAPI
- Pydantic
- SQLModel (SQLAlchemy + Pydantic)
- Langchain + langchain-openai
- Docker

**Docker Desktop is required** 

For applicants using MacOS, it should be as simple as [Installing](https://docs.docker.com/desktop/setup/install/mac-install/) and starting the Docker Desktop App, then following the rest of this guide.

For those on Windows, if you have not previously setup Docker be warned, its often a **[Major Pain](https://www.imdb.com/title/tt0110443/)**. If this is you, please feel free to contact us so we can walk you through the setup process before starting the 24 hour countdown. 

### Starting the App
1) Copy + Paste the '.env.template file' at the root level of the repository (same place as the template), rename to '.env', then set the 'OPENAI_API_KEY' variable to the API key provided to you.
2) Start Docker Desktop.
3) Navigate to the working directory of this repo in your terminal.
4) Run 'docker volume create takehome-db'
5) Run 'docker compose build' - Wait for the script to complete.
6) Run 'docker compose up -d'
7) Navigate to the 'containers' tab in the Docker Desktop app and confirm two containers are present and running in the 'backend-dev-takehome' folder.
8) Navigate to http://localhost:8080/takehome/docs# and confirm the FastAPI server is working and displays two API endpoints.
9) *OPTIONAL* - With your preferred SQL viewer, connect to the PostgreSQL DB with the credentials found in the .env.template file and confirm 4 tables have been created and populated with data.

### Development Guidelines & Tips
**Getting Started**

There are three files named 'llm_services.py', one at app/domain/services, one at app/domain/protocols/services, and one at app/routes. These have been created for you to write your service and api endpoint respectively. It is expected that additional services and DB interfaces will be required to complete this task and it will be up to you to decide the appropriate locations for these methods, examples can be found in the 'concept.py' and 'concept_collection.py' files for reference. 

**Key Points:**
- If using the provided API key, **ONLY USE 'gpt-3.5-turbo', 'gpt-3.5-turbo-instruct, or any other gpt-3.5 based models'** for LLM queries, other models are restricted by the key.
- AI assistance *is* allowed but be aware that obvious over reliance will count against you.
- Try to use the pre-existing dependencies that come with this repo if possible, they should be sufficient to complete this task. Additional dependencies may be added if required, however, we'll expect some added value to result from the inclusion and for you to explain your reasoning.  
- This repo is structured so dataflow from the DB to the API is as follows: app/infrastructure/repositories -> app/domain/services -> app/routes
- Most methods and functions are expected to have a standardized output structure defined within the app/domain/models directory, either in the form of a SQLModel class or a Pydantic Class.

**Troubleshooting:**

If any issues occur due to incorrect DB seeding or Docker, please contact us and we will provide assistance and reimburse the time spent troubleshooting.

**Problem:** The database was not properly populated with starting data.

**Solution:** Delete the containers and attached DB volume 'takehome-db', navigate to app/infrastructure/seeds.py and add logging to the '_populate_db' function to ensure seed.json is being loaded in correctly and that the order of tables loaded is as follows 'Concept' -> 'ConceptCollection' -> 'ConceptToConcept', 'ConceptToCollection', run 'docker volume create takehome-db' then 'docker compose up -d', then inspect the logs and new db instance. If this doesn't work, contact us and we can help troubleshoot.

**Problem:** I've made changes to the code but nothing seems different.

**Solution:** It's possible Docker is not reloading properly on a code change, try restarting the application container and executing the code in question again. If this doesn't work, try printing something at the top of one of the API endpoint functions found in app/routes, restart the container for safety, and query that endpoint. If it prints to the docker logs then your changes have been applied properly, if it doesn't print you can contact us and we'll try to help troubleshoot.
