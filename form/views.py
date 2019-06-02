from django.db import IntegrityError
from django.shortcuts import render
from django.views import View

from . import queries
from .models import Entry


class Form(View):
    def get(self, request):
        return render(request, 'form/entry.html', {
            'entries': queries.latest_entries()
        })

    def post(self, request):
        ctx = {
            'entries': queries.latest_entries()
        }
        e = Entry(
            name=request.POST['name'],
            color=request.POST['color'],
            pet=request.POST['pet']
        )
        try:
            e.save()
            ctx['success_message'] = 'Success!'
        except IntegrityError:
            ctx['error_message'] = 'Error: Your name is already posted.'
        return render(request, 'form/entry.html', ctx)
