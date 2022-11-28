from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    @task
    def hello(self):
        self.client.get("/")
