from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class WtdegreecheckConfig(AppConfig):
    name = 'WTdegreecheck'


class WTAMUAdminConfig(AdminConfig):
    default_site = 'admin.WTAMUAdminSite'