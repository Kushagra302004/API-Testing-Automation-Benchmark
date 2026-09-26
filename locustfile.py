from locust import HttpUser, between, task

class APIUser(HttpUser):
    wait_time = between(1, 2)
    @task(3)
    def get_user(self):
        self.client.get("/users/1", name="GET /users/{id}")
    @task(1)
    def list_users(self):
        self.client.get("/users", name="GET /users")
