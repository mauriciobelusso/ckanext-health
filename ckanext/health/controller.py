from ckan.lib.base import BaseController, render

class HealthController(BaseController):
    def index(self):
        return render('health/health.html')
