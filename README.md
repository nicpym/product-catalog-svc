# product-catalog-svc

Product Catalog Service

## Project Structure

```plaintext
.
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
└── .dockerignore (optional)
```

## Building and Running the Service

1. **Clone the Repository**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Build the Docker Image**

    ```bash
    docker build -t product-catalog-svc .
    ```

3. **Run the Docker Container**

    ```bash
    docker run -p 8080:8080 product-catalog-svc
    ```

4. **Access the Service**

    Open your browser or use `curl` to access the service:

    ```bash
    curl http://localhost:8080
    ```

    You should see the message: `Hello, World!`

## Running the Application Locally without Docker

If you want to run the application locally without Docker:

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

1. Run the application:

    ```bash
    uvicorn main:app --reload
    ```
