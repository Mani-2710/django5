from django.shortcuts import render, redirect
from .models import NatalChartAnalysis, zodaic


# Create your views here.
def horoscopes(request):
    return render(request, 'user/horoscopes.html')


def daily(request):
    return render(request, 'user/daily.html')


def weekly(request):
    return render(request, 'user/weekly.html')


def monthly(request):
    return render(request, 'user/monthly.html')


def yearly(request):
    return render(request, 'user/yearly.html')


def service(request):
    return render(request, 'user/service.html')


def chartanalysis(request):
    return render(request, 'user/chartanalysis.html')


def reading(request):
    return render(request, 'user/reading.html')


from .models import dailyhoroscopes


def save_horoscope(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        birth_day = request.POST.get("birth-day")
        birth_month = request.POST.get("birth-month")
        birth_year = request.POST.get("birth-year")

        if name and birth_day and birth_month and birth_year:
            dailyhoroscope = dailyhoroscopes(
                name=name,
                birth_day=birth_day,
                birth_month=birth_month,
                birth_year=birth_year
            )
            dailyhoroscope.save()

            return redirect('horoscope-success')  # Redirect to a success page or any other desired page

    return redirect('Home-horoscope')
