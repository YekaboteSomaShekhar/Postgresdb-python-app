# Postgresdb-python-app

### Postgres-Python App (Dockerized)

This project is a beginner-friendly demonstration of how to:

- Create a simple Python application
- Connect to a PostgreSQL database
- Create a table
- Insert a row
- Read & display data in a table format
- Dockerize the application
- Run both containers using a custom Docker network
- Push the final application image to Docker Hub

### Project Structure
postgres-python-app/

    ├── app.py
 
    ├── requirements.txt
 
    └── Dockerfile
    
### Outputs

**Building the Docker Image:**

- Using the docker build command:
```

docker build -t <yourusername>/postgres-python-app:latest .
```
- So it will start building the docker image.

<img width="902" height="737" alt="Screenshot 2025-12-05 164551" src="https://github.com/user-attachments/assets/71224209-b6e8-4720-aefa-783d18e71973" />

**Create Custom Docker Network:**

- Create a custom docker network by using the command:

```
docker network create network_name
```

- In this case I have already created my own custom network called "mynetwork". So it says already exists.

<img width="892" height="78" alt="Screenshot 2025-12-05 164647" src="https://github.com/user-attachments/assets/f85dfebf-44ee-48c0-8db5-1827886af7c1" />

**Run PostgreSQL Container:**

- Run the below the command to run the postgreSQL container.

```
docker run -d --name postgres-db --network mynetwork -e POSTGRES_USER=testuser -e POSTGRES_PASSWORD=testpass -e POSTGRES_DB=testdb postgres:15
```

<img width="922" height="764" alt="Screenshot 2025-12-05 164754" src="https://github.com/user-attachments/assets/cdc004b7-2b6d-462a-a238-5d741b50629e" />
<img width="873" height="237" alt="Screenshot 2025-12-05 164817" src="https://github.com/user-attachments/assets/601c3fca-d0a9-4ae0-9fa9-3ecc6c752245" />

**Expected output:**

- Python app is connected to postgreSQL database. So the output will be like this:  

<img width="903" height="174" alt="Screenshot 2025-12-05 172255" src="https://github.com/user-attachments/assets/31f53c70-0236-4fc3-8107-098c57385adb" />

**How to Push the docker image to dockerhub?**

- Using the docker push command, we can push the docker image into the dockerhub.

```
docker push yourusername/postgres-python-app:latest
```

<img width="907" height="388" alt="Screenshot 2025-12-05 172711" src="https://github.com/user-attachments/assets/074c2377-4b03-4b0f-9c1c-f33b729bd94f" />
