from django.apps import AppConfig


class WtdegreecheckConfig(AppConfig):
    name = 'WTdegreecheck'

from django.contrib.admin.apps import AdminConfig
class WTAMUAdminConfig(AdminConfig):
    default_site = 'admin.WTAMUAdminSite'