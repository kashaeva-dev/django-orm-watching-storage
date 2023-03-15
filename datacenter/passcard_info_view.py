from django.shortcuts import render, get_object_or_404

from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration


def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits_qs = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in this_passcard_visits_qs:
        visit_info = dict()
        visit_info['entered_at'] = visit.entered_at
        visit_info['duration'] = format_duration(visit.get_duration())
        visit_info['is_strange'] = visit.is_visit_long()
        this_passcard_visits.append(visit_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
