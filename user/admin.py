from django.contrib import admin

from .models import NatalChartAnalysis, zodaic, dailyhoroscopes, weeklyhoroscopes, monthlyhoroscopes, yearlyhoroscopes

# Register your models here.
admin.site.register(NatalChartAnalysis)
admin.site.register(zodaic)
admin.site.register(dailyhoroscopes)
admin.site.register(weeklyhoroscopes)
admin.site.register(monthlyhoroscopes)
admin.site.register(yearlyhoroscopes)