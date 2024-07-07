<h1>Welcome to the Job Listing Generator readme!</h1>

This is an app that uses the Langchain framework library to generate a personalized job listing and keep a summarized record of the generated ones.
 
 <h3>Let's get started!</h3>
 
 Prerequisites:

- Docker: Make sure you have Docker installed on your machine. You can follow the official Docker installation guide for your operating system: [Install Docker](https://docs.docker.com/get-docker/)
- Python: Ensure that Python is installed on your machine. You can check the Python version by running python --version in your terminal.

---

__Step-by-Step Guide:__
   - 1 - **Clone the Repository**:
       - Open your terminal and navigate to the directory where you want to clone the project.
       - Run the following command to clone the repository:  
       ---
      ```shell
      git clone https://github.com/pedromussi0/JobListingGenerator.git
      ```
      ---
   - 2 - **Set up Environment Variables**:
       - Create a new file named .env in the root of the project directory.
       - Open the .env file in a text editor and set the following environment variables:
       ---
        ```shell
        POSTGRES_USER=<your_postgres_username>
        POSTGRES_PASSWORD=<your_postgres_password>
        OPENAI_API_KEY=<your_openai_api_key>
        ```
        ---
       - Replace <your_postgres_username> and <your_postgres_password> with your desired PostgreSQL username and password. These credentials will be used to create a new user in the PostgreSQL container. 
       - Replace <your_openai_api_key> with your actual OpenAI API key.
       ---
   - 3 - **Create a Docker Compose File**:
       - Open a text editor and create a new file named 'docker-compose.yml' in the root of the project directory. 
       - Copy the following contents into the docker-compose.yml file:
       ---
       ```shell
       version: '3'

      services:
        web:
          build:
            context: .
            dockerfile: Dockerfile
          ports:
            - "8000:8000"
          depends_on:
            - db
          volumes:
            - .:/code
          environment:
            - USER=${POSTGRES_USER}
            - PASSWORD=${POSTGRES_PASSWORD}
            - OPENAI_API_KEY=${OPENAI_API_KEY}
          env_file:
            - .env

        db:
          image: postgres:latest
          volumes:
            - db-data:/var/lib/postgresql/data
          environment:
            - POSTGRES_USER=${POSTGRES_USER}
            - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
            - POSTGRES_DB=job_listings_db

      volumes:
        db-data:
       ```
       ---
       - Save the docker-compose.yml file.
       ---
   - 4 - **Build and Run the Docker Container**:
       - Open your terminal and navigate to the project's root directory.
       - Run the following command to build and run the Docker container:
       ---
       ```shell
       docker-compose up --build
       ```
       ---
       - Docker Compose will build the necessary images and start the containers defined in the docker-compose.yml file.
       - Wait for the containers to start. You should see logs indicating the progress.
       ---
   - 5 - **Apply Database Migrations**:
       - Once the Docker containers are up and running, you have to run the migrations for the PostgreSQL database.
       - Open a new terminal window or tab.
       - Run the following command to access the web container:
       ---
       ```shell
       docker-compose exec web bash
       ```
       ---
       - You will be connected to the container's command-line interface.
       - To run the migrations, run the following command:
       ---
       ```shell
       python manage.py migrate
       ```
       ---
       - You should see all migrations being applied with 'OK' alongside them.
       ---
   - 6 - **Accessing the Application**:
       - Once the containers are running, you can access the application by opening a web browser and entering the following URL:
       ---
       ```shell
       http://localhost:8000
       ```
       - The application should be up and running.
       ---
   - **Important Notes**:
      -  Make sure that ports 8000 and 5432 (default PostgreSQL port) are not being used by any other processes on your machine. If they are occupied, you can update the ports in the docker-compose.yml file.
      -  Remember to replace <your_postgres_username>, <your_postgres_password>, and <your_openai_api_key> with appropriate values specific to your project or desired credentials.

<h2>That's it!</h2>
       
       
       
        
       
       
        
      
      
      





