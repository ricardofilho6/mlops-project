import logging
from dotenv import load_dotenv
import dagshub

load_dotenv()

dagshub.init(
    repo_owner="ricardofilho6",
    repo_name="mlops-project"
)


# Configure the logging strategy
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler()
    ]
)
