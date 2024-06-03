import ckan.plugins as p
import ckan.plugins.toolkit as tk

class HealthPlugin(p.SingletonPlugin):
    p.implements(p.ITemplateHelpers)
    p.implements(p.IConfigurer)

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('public', 'ckanext-health')

    def get_helpers(self):
        return {'get_health_data': self.get_health_data}

    def get_health_data(self):
        return [
            {'date': '2024-06-01', 'exercise': 'Running', 'duration': '30 minutes', 'calories': 300},
            {'date': '2024-06-02', 'exercise': 'Cycling', 'duration': '45 minutes', 'calories': 450},
        ]
