from django.shortcuts import render
from hicharts.models import Passenger
from django.db.models import Count
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def json_example(request):
    return render(request, 'hicharts_ex.html')

def chart_data(request):
    print("hello")
    dataset = Passenger.objects \
        .values('embarked') \
        .exclude(embarked='') \
        .annotate(total=Count('embarked')) \
        .order_by('embarked')
    print(dataset)
    port_display_name = dict()
    for port_tuple in Passenger.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]
    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Titanic Survivors by Destination Port'},
        'series': [{
            'name': 'Embarkation Port',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }
    print(chart)
    return JsonResponse(chart)
    #return render(request, 'hicharts_ex.html')

def column_data(request):
    print("hello")
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')
    print(dataset)
    categories = list()
    survived_series_data = list()
    not_survived_series_data = list()

    for entry in dataset:
        categories.append('%s Class' % entry['ticket_class'])
        survived_series_data.append(entry['survived_count'])
        not_survived_series_data.append(entry['not_survived_count'])

    survived_series = {
        'name': 'Survived',
        'data': survived_series_data,
        'color': 'green'
    }

    not_survived_series = {
        'name': 'Survived',
        'data': not_survived_series_data,
        'color': 'red'
    }
    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'xAxis': {'categories': categories},
        'series': [survived_series, not_survived_series]
    }
    print(chart)
    return JsonResponse(chart)

def line_data(request):
    print("hello")
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')
    print(dataset)
    categories = list()
    survived_series_data = list()
    not_survived_series_data = list()

    for entry in dataset:
        categories.append('%s Class' % entry['ticket_class'])
        survived_series_data.append(entry['survived_count'])
        not_survived_series_data.append(entry['not_survived_count'])

    survived_series = {
        'name': 'Survived',
        'data': survived_series_data,
        'color': 'green'
    }

    not_survived_series = {
        'name': 'Survived',
        'data': not_survived_series_data,
        'color': 'red'
    }
    chart = {
        'chart': {'type': 'line'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'xAxis': {'categories': categories},
        'series': [survived_series, not_survived_series]
    }
    print(chart)
    return JsonResponse(chart)
