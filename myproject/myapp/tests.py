import threading
import logging
from django.contrib.auth.models import User

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to create a user and trigger the signal
def create_user():
    logger.info(f"Main Function: Running in thread {threading.get_ident()}")
    User.objects.create(username="testuser")

