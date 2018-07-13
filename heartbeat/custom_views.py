from django.shortcuts import render
from django.forms.models import modelformset_factory
from heartbeat.models import Player
from otree.models import Session

def heartbeat_setup(request, session_code):
    sessions = Session.objects.filter(code=session_code)
    print(session_code)
    PlayerFormset = modelformset_factory(Player, extra=0, fields=['wristband_start_time'])
    if request.method == 'POST':
        formset = PlayerFormset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = PlayerFormset(queryset=Player.objects.filter(session__in=sessions))
    return render(request, 'heartbeat/WristbandSetup.html', { 'formset': formset })