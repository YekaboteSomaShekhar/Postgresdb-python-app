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

**Building the Docker Image**

- Using the docker build command:
```

docker build -t <yourusername>/postgres-python-app:latest .
```
- So it will start building the docker image.

<img width="902" height="737" alt="Screenshot 2025-12-05 164551" src="https://github.com/user-attachments/assets/71224209-b6e8-4720-aefa-783d18e71973" />


**Create Custom Docker Network**

- Create a custom docker network by using the command:

```
docker network create mynetwork
```

- In this case I have already created my own custom network called "mynetwork". So it says already exists.

<img width="892" height="78" alt="Screenshot 2025-12-05 164647" src="https://github.com/user-attachments/assets/f85dfebf-44ee-48c0-8db5-1827886af7c1" />

**Run PostgreSQL Container**

<img width="922" height="764" alt="Screenshot 2025-12-05 164754" src="https://github.com/user-attachments/assets/cdc004b7-2b6d-462a-a238-5d741b50629e" />

<img width="873" height="237" alt="Screenshot 2025-12-05 164817" src="https://github.com/user-attachments/assets/8e709dc6-d34b-4f6e-a1c7-5210f732b585" />

<img width="901" height="210" alt="Screenshot 2025-12-05 164848" src="https://github.com/user-attachments/assets/1aa50aca-be43-4c4a-96e1-145e07bd4791" />




