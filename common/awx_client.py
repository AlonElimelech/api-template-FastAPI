import requests

class AWXClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def launch_job(self, job_template_id: int, extra_vars: dict):
        url = f"{self.base_url}/api/v2/job_templates/{job_template_id}/launch/"
        response = requests.post(url, headers=self.headers, json={"extra_vars": extra_vars})

        if response.status_code != 201:
            raise Exception(f"Failed to launch job: {response.status_code} - {response.text}")

        return response.json()
