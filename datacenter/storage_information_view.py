from django.shortcuts import render

from datacenter.models import Visit, format_duration


def storage_information_view(request):

    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []

    for visit in visits:
        visit_info = dict()
        visit_info['who_entered'] = visit.passcard.owner_name
        visit_info['entered_at'] = visit.entered_at
        visit_info['duration'] = format_duration(visit.get_duration())
        non_closed_visits.append(visit_info)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
