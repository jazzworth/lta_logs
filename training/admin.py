from django.contrib import admin
from training.models import Balloon, PrivateAreaOfOperation, PrivateLessonPlan, PrivateLessonPlanElements, PrivateStandards

    
admin.site.register(PrivateAreaOfOperation)
admin.site.register(PrivateLessonPlan)
admin.site.register(PrivateLessonPlanElements)
admin.site.register(PrivateStandards)

