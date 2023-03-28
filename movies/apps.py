from django.apps import AppConfig


class MoviesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "movies"

    def ready(self) -> None:
        from movies.factory import (
            create_initial_data_if_none_exists,
        )

        # create_initial_data_if_none_exists()
        return super().ready()
