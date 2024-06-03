import ckan.plugins as p
import ckan.plugins.toolkit as tk

class HealthPlugin(p.SingletonPlugin):
    p.implements(p.ITemplateHelpers)

    def get_helpers(self):
        return {'get_health_data': self.get_health_data}

    def get_health_data(self):
        # Esta função retornará dados de saúde simulados
        return [
            {'date': '2024-06-01', 'exercise': 'Running', 'duration': '30 minutes', 'calories': 300},
            {'date': '2024-06-02', 'exercise': 'Cycling', 'duration': '45 minutes', 'calories': 450},
        ]

    # Outros métodos podem ser adicionados para registrar dados de saúde
