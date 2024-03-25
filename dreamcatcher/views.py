from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .charts import StressChartCreator, EnergyChartCreator, DurationChartCreator, ChartDecorator
from .forms import UserForm
from .models import Dream


def login_page(request):
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return descriere_categorie(request)
    return render(request, 'login.html')


def login_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            user = authenticate(username=username, password=password)
            if user is None:
                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                last_name=lastname)
                user.save()
                return render(request, 'success_register.html')
    else:
        form = UserForm()
    return render(request, 'login.html', {'form': form})


def login_register_view(request):
    return render(request, 'register.html')


def descriere_categorie(request):
    return render(request, 'descriere_categorie.html')


def rating(request):
    if request.method == 'POST':
        description = request.POST['description']
        category = request.POST['category']
        user = request.user.username
        dream = Dream(user=user, descriere=description, eticheta=category, stres=0, nivelEnergie=0, durata=0)
        dream.save()
    return render(request, 'rating.html')


@login_required
def statistici_view(request):
    if request.method == 'POST':
        duration = request.POST['duration']
        energy = request.POST['energy']
        stress = request.POST['stress']
        user = request.user.username

        dream = Dream.objects.latest('id')
        dream.durata = duration
        dream.nivelEnergie = energy
        dream.stres = stress
        dream.save()

    weeks = list(range(1, 53))
    months = list(range(1, 13))

    context = {'weeks': weeks, 'months': months}
    return render(request, 'statistici.html', context)


def back_to_statistici_view(request):
    weeks = list(range(1, 53))
    months = list(range(1, 13))

    context = {'weeks': weeks, 'months': months}
    return render(request, 'statistici.html', context)


def statistici_view_stres_week(request):
    if request.method == 'POST':
        week = request.POST.get('week_stres')
    stress_chart_creator = StressChartCreator()
    chart_creator_stress = ChartDecorator(stress_chart_creator)
    stress_chart_week = chart_creator_stress.create_chart_week(request, week=week)
    return stress_chart_week


def statistici_view_stres_month(request):
    if request.method == 'POST':
        month = request.POST.get('month_stres')
    stress_chart_creator = StressChartCreator()
    chart_creator_stress = ChartDecorator(stress_chart_creator)
    stress_chart_month = chart_creator_stress.create_chart_month(request, month=month, year=2023)
    return stress_chart_month


def statistici_view_energie_week(request):
    if request.method == 'POST':
        week = request.POST.get('week_energie')
    energy_chart_creator = EnergyChartCreator()
    chart_creator_energy = ChartDecorator(energy_chart_creator)
    energy_chart_week = chart_creator_energy.create_chart_week(request, week=week)
    return energy_chart_week


def statistici_view_energie_month(request):
    if request.method == 'POST':
        month = request.POST.get('month_energie')
    energy_chart_creator = EnergyChartCreator()
    chart_creator_energy = ChartDecorator(energy_chart_creator)
    energy_chart_month = chart_creator_energy.create_chart_month(request, month=month, year=2023)
    return energy_chart_month


def statistici_view_durata_week(request):
    if request.method == 'POST':
        week = request.POST.get('week_durata')
    duration_chart_creator = DurationChartCreator()
    chart_creator_duration = ChartDecorator(duration_chart_creator)
    duration_chart_week = chart_creator_duration.create_chart_week(request, week=week)
    return duration_chart_week


def statistici_view_durata_month(request):
    if request.method == 'POST':
        month = request.POST.get('month_durata')
    duration_chart_creator = DurationChartCreator()
    chart_creator_duration = ChartDecorator(duration_chart_creator)
    duration_chart_month = chart_creator_duration.create_chart_month(request, month=month, year=2023)
    return duration_chart_month
