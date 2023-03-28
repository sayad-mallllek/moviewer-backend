from django.db.models.signals import class_prepared, post_init
from django.dispatch import receiver
from movies.factory import (
    create_initial_data_if_none_exists,
)  # Replace `MyModel` with your actual model name


# @receiver(post_init)
# def run_on_first_app_run(sender, **kwargs):
#     print("jello")
#     if sender.name == "myapp":  # Replace `myapp` with your actual app name
#         create_initial_data_if_none_exists()
#         pass
