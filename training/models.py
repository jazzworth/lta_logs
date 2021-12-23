from django.db import models
from user_profile.models import PilotInformation
from aircraft_profile.models import Balloon


class PrivateAreaOfOperation(models.Model):
    paoo_id = models.AutoField(primary_key=True, null=False)
    paoo_name = models.CharField(max_length=254, null=False)

    def __str__(self) -> str:
        return super().__str__()


class PrivateStandards(models.Model):
    ps_id = models.AutoField(primary_key=True, null=False)
    ps_name = models.CharField(max_length=254, null=False)
    ps_aoo = models.ForeignKey(PrivateAreaOfOperation, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()


class PrivateLessonPlan(models.Model):
    plp_id = models.AutoField(primary_key=True, null=False)
    plp_date = models.DateField(auto_now_add=True)
    plp_objective = models.TextField(max_length=1024)
    plp_instructor_action = models.TextField(max_length=1024)
    plp_student_action = models.TextField(max_length=1024)
    plp_completion_standards = models.TextField(max_length=1024)
    plp_flight_time = models.CharField(max_length=16)
    plp_notes = models.TextField(max_length=2048)
    plp_instructor_id = models.ForeignKey(PilotInformation, related_name='instructor', on_delete=models.CASCADE)
    plp_student_id = models.ForeignKey(PilotInformation, related_name='student', on_delete=models.CASCADE)
    plp_balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()

class PrivateLessonPlanElements(models.Model):
    plpe_id = models.AutoField(primary_key=True, null=False)
    plpe_student_action_no_assistance = models.BooleanField(default=False)
    plpe_student_action_some_assistance = models.BooleanField(default=False)
    plpe_student_action_needed_assistace = models.BooleanField(default=False)
    plpe_private_lesson_plan = models.ForeignKey(PrivateLessonPlan, on_delete=models.CASCADE)
    plpe_element = models.ForeignKey(PrivateStandards, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()


