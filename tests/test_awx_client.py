from unittest.mock import patch, Mock
from common.awx_client import launch_job
#from pandas.mytest import DataFrame
from fastapi.testclient import TestClient




@patch("requests.post")
def test_launch_job_success(mock_post):
    # Mock the response object
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "job": 123,
        "url": "/api/v2/jobs/42/"
    }

    # Set the mock object to be returned by requests.post
    mock_post.return_value = mock_response

    # Inputs
    base_url = "http://awx.example.com"
    job_template_id = 100
    headers = {"Authorization": "Bearer fake-token"}
    extra_vars = {"key": "value"}

    # Call the function
    result = launch_job(base_url, job_template_id, headers, extra_vars)
    print(result)

    print(f"Function full path: {launch_job.__module__}.{launch_job.__name__}")
    print(f"Function name: {launch_job.__name__}")

    
    print(f"Function full path: {TestClient.__module__}.{TestClient.__name__}")
    print(f"Function name: {TestClient.__name__}")
    # Assertions
    assert result["status"] == "success"
    assert result["job_id"] == 123
    assert result["return_code"] == 200
    assert result["stdout"] == "http://awx.example.com/api/v2/jobs/42/"

    # Ensure post was called with correct arguments
    #mock_post.assert_called_once_with(
      #  "http://awx.example.com/api/v2/job_templates/100/launch/",
     #   headers=headers,
    #    json={"extra_vars": extra_vars}
   # )
