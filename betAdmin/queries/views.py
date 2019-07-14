from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from betAdmin.core.models import Param


@login_required()
def index(request):
    template_name = 'statement.html'

    context = {
        'params' : Param.objects.all()
    }
    return render(request, template_name, context)
