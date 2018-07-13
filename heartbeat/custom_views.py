from django.shortcuts import render
from django.forms.models import modelformset_factory
from heartbeat.models import Player
from otree.models import Session

# custom wristband setup page
def heartbeat_setup(request, session_code):
    # get the current session by session_code
    sessions = Session.objects.filter(code=session_code)
    # creat a set of forms, each form for one player, only include wristband_start_time field
    PlayerFormset = modelformset_factory(Player, extra=0, fields=['wristband_start_time'])
    if request.method == 'POST':
        # if we receive valid data, store it.
        formset = PlayerFormset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        # prepare the actual formset, limit to players in the current session
        formset = PlayerFormset(queryset=Player.objects.filter(session__in=sessions))

    # render the WristbandSetup page with the correct formset.
    return render(request, 'heartbeat/WristbandSetup.html', { 'formset': formset })