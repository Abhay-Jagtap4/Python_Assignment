import time
import logging
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Set up logging
logger = logging.getLogger(__name__)

# Signal Receiver
@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    logger.info("Signal execution started...")
    time.sleep(5)  # Simulating a delay
    logger.info("Signal execution finished...")

# Trigger Function
def create_user():
    logger.info("Creating user...")
    start_time = time.time()
    
    User.objects.create(username="testuser")  # This should trigger the signal
    
    end_time = time.time()
    logger.info(f"User creation completed in {end_time - start_time:.2f} seconds")

# Running the function
create_user()
