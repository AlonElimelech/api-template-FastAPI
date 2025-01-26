import requests
import asyncio
from fastapi import BackgroundTasks



def launch_job(base_url: str,job_template_id: int, headers: str, extra_vars: dict, callback: str ,background_tasks: BackgroundTasks):
    url = f"{base_url}/api/v2/job_templates/{job_template_id}/launch/"
    response = requests.post(url, headers=headers, json={"extra_vars": extra_vars})

    if response.status_code != 201:
        raise Exception(f"Failed to launch job: {response.status_code} - {response.text}")
    job_id = response.json().get("job")
    background_tasks.add_task(polling_awx_job_status, base_url, job_id, headers, callback)


    return response.json()

def polling_awx_job_status(base_url: str, job_id: int, headers: str, callback_url: str):
    url = f"{base_url}/api/v2/jobs/{job_id}/"
    while True:
        response = requests.get(url, headers=headers)

        try:
            if response.status_code != 200:
                raise Exception(f"Failed to fetch status for job {job_id}")
            
            job_status = response.json().get("status")
            
            # Step 4: Check if job is completed
            if job_status in ["successful", "failed"]:
                notify_argo_workflow(callback_url, job_id, job_status)
                return
            
        except Exception as e:
            print(f"Error polling AWX: {e}")
        
        asyncio.sleep(10)  # Sleep for 10 seconds before polling again

def notify_argo_workflow(callback_url: str, job_id: str, status: str):
    payload = {
        "job_id": job_id,
        "status": status,
    }
    try:
        response = requests.post(callback_url, json=payload)
        if response.status_code != 200:
            print(f"Failed to notify Argo Workflow: {response.text}")
    except Exception as e:
        print(f"Error notifying Argo Workflow: {e}")

