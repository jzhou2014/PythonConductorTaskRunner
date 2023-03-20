import os
from pydantic import BaseSettings
from conductor.client.configuration.configuration import Configuration

from dotenv import load_dotenv

load_dotenv()


class FastAPISettings(BaseSettings):
    app_name: str = "Workflow Python"
    admin_email: str = "jin_zhou@unigroup.com"


server_url = f"{os.environ.get('CONDUCTOR_URL_BASE')}"
print(f"Polling conductor at {server_url}")
conductor_config = Configuration(
    server_api_url=server_url,
    debug=os.environ.get("CONDUCTOR_DEBUG") == "true",
)


fast_api_settings = FastAPISettings()
