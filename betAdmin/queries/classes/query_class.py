from django.db import connection
from betAdmin.core.models import Event
from django.db.models.expressions import RawSQL


class QueryFilter():
    
    @staticmethod
    def get_comparison_filters():
        params = [
            {
            'value': '1',
            'filter' : '>',
            'name' : 'Maior que'
            },
            {
            'value': '2',
            'filter' : '>=',
            'name' : 'Maior ou igual'
            },{
            'value': '3',
            'filter' : '<',
            'name' : 'Menor que'
            },
            {
            'value': '4',
            'filter' : '<=',
            'name' : 'Menor ou igual'
            },
        ]
        return params

    @staticmethod
    def get_periods_param():
        periods = [
            {
                'value' : 'ALL',
                'name' : 'Total',
            },
            {
                'value' : '1ST',
                'name' : '1º Tempo',
            },
            {
                'value' : '2ST',
                'name' : '2º Tempo',
            }
        ]

        return periods

    @staticmethod
    def get_teams_param():
        teams = [
            {
                'value' : True,
                'name' : 'Casa'
            },
            {
                'value' : False,
                'name' : 'Fora'
            },
            {
                'value' : None,
                'name' : 'Ambos'
            }
        ]

        return teams


    @staticmethod
    def get_element_comparison_filter(value):
        for param in QueryFilter.get_comparison_filters():
            if param['value'] == value:
                return param
        return None

    @staticmethod
    def sql_get(params, condition, value, period, team):
        sql_base = """SELECT DISTINCT(match.global_match_id) from event
            inner join param on event.param_id = param.id
            inner join match on event.match_id = match.id
            where param.id = {0} 
            and event.value {1} {2}
            and event.period = '{3}'
            """.format(params,condition, value, period)
        
        if team != "None":
            sql_base += """and event.team = {0}""".format(team)
        
        print(sql_base)

        row = Event.objects.raw(sql_base)
        print(len(row))
        print(type(row))

        return row
            