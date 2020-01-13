from django.db import models
from multiselectfield import MultiSelectField


GENDER_CHOICES = (
    ('M', 'Мужской'),
    ('W', 'Женский')
)


TREATMENT_CHOICES = (
    ('free', 'Бесплатный'),
    ('paid', 'Платный')
)


DAY_CHOICES = (
    ('monday', 'Понедельник'),
    ('Tuesday', 'Вторник'),
    ('Wednesday', 'Среда'),
    ('Thursday', 'Четверг'),
    ('Friday', 'Пятница')
)


class Patient(models.Model):
    lastName = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, blank=True, null=True, verbose_name='Отчество')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    amb_card = models.IntegerField(verbose_name='Номер амбулаторной карты')
    employee_lastName = models.CharField(max_length=30, verbose_name='Фамилия сотрудника')
    place_of_residence = models.CharField(max_length=100, verbose_name='Место жительства')
    place_of_study = models.CharField(max_length=100, verbose_name='Место работы/учебы')
    number_passport = models.CharField(max_length=12, verbose_name='номер паспорта')
    treatment_type = models.CharField(default=0, max_length=10, choices=TREATMENT_CHOICES, verbose_name='Вид лечения')

    def __str__(self):
        return self.name


class Card(models.Model):
    patient = models.ForeignKey('dentistry.Patient', on_delete=models.CASCADE, related_name='card')
    insurance = models.IntegerField(verbose_name='Страховой полис')
    doctor = models.ForeignKey('dentistry.Employee', on_delete=models.CASCADE, related_name='card')

    def __str__(self):
        return self.patient.name


class Employee(models.Model):
    lastName = models.CharField(max_length=30, verbose_name='Фамилия', help_text='Фамиля Сотрудника')
    name = models.CharField(max_length=30, verbose_name='Имя', help_text='Имя Сотрудника')
    patronymic = models.CharField(max_length=30, blank=True, null=True, db_index=True,
                                  verbose_name='Отчество', help_text='Отчество Сотрудника')
    position = models.ForeignKey('dentistry.Position', on_delete=models.DO_NOTHING, related_name='employee',
                                 help_text='название должности')

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название должности')

    def __str__(self):
        return self.name


class Admission_time(models.Model):
    employee = models.ForeignKey('dentistry.Employee', on_delete=models.CASCADE, related_name='Admission_time')
    day = models.CharField(max_length=20, choices=DAY_CHOICES, verbose_name='День недели')
    time_start = models.TimeField(auto_now=False, auto_now_add=False)
    time_end = models.TimeField(auto_now=False, auto_now_add=False)


class Admission(models.Model):
    employee = models.ForeignKey('dentistry.Employee', on_delete=models.CASCADE, related_name='admission')
    patient = models.ForeignKey('dentistry.Patient', on_delete=models.CASCADE, related_name='admission')
    cause = models.CharField(max_length=100, verbose_name='Причина визита')
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.patient.name
