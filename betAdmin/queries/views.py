from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from betAdmin.queries.classes.query_class import QueryFilter


from betAdmin.core.models import Param


@login_required()
def index(request):
    template_name = 'statement.html'
    query_result = []

    if request.method == 'POST':
        params = request.POST['params']
        period = request.POST['period']
        value = request.POST['value']
        team = request.POST['team']
        condition = QueryFilter.get_element_comparison_filter(request.POST['condition'])

        query_result = QueryFilter.sql_get(params, condition['filter'],value, period, team)

    else:

        print('get')

    context = {
        'params' : Param.objects.all(),
        'filters_params' : QueryFilter.get_comparison_filters(),
        'periods_param' :  QueryFilter.get_periods_param(),
        'teams_param' :  QueryFilter.get_teams_param(),
        'query_result' : query_result
    }

    return render(request, template_name, context)
