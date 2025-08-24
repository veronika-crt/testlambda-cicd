from locust import HttpUser, task, between
import os

class LambdaUser(HttpUser):
    wait_time = between(1, 2)
    host = os.getenv("LAMBDA_URL", "http://localhost:8080")  # Set your deployed Lambda/API Gateway URL

    @task
    def hello_lambda(self):
        self.client.get("/")

    @task
    def greet_lambda(self):
        self.client.post("/greet", json={"name": "PerformanceTest"})
