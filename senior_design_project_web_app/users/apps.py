import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "senior_design_project_web_app.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import senior_design_project_web_app.users.signals  # noqa: F401
