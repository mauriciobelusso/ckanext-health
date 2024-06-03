import ckan.plugins as p
import ckan.plugins.toolkit as tk

class HealthPlugin(p.SingletonPlugin):
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.ITemplateHelpers)
    p.implements(p.IConfigurer)

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('public', 'ckanext-health')

    def before_map(self, map):
        controller = 'ckanext.health.controllers:HealthController'
        map.connect('/health', controller=controller, action='index')
        return map

    def get_helpers(self):
        return {'get_health_data': self.get_health_data}

    def get_health_data(self):
        # Esta função retornará dados de saúde simulados
        return [
            {'date': '2024-06-01', 'exercise': 'Running', 'duration': '30 minutes', 'calories': 300},
            {'date': '2024-06-02', 'exercise': 'Cycling', 'duration': '45 minutes', 'calories': 450},
        ]
