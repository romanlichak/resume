from django.db import models


class PersonalData(models.Model):
    fio = models.CharField(max_length=350)
    born = models.DateField(auto_now=False)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.fio


class DesireRole(models.Model):
    desire_role = models.CharField(max_length=50)

    def __str__(self):
        return self.desire_role


class Experience(models.Model):
    role = models.CharField(max_length=250)
    company = models.CharField(max_length=50)
    data_start = models.DateField(auto_now=False)
    data_end = models.DateField(auto_now=False)
    tasks = models.TextField(max_length=5000,
                               help_text="Введите свой опыт",
                               verbose_name="Опыт работы")
    briefly = models.TextField(max_length=5000,
                               help_text="Введите свой опыт",
                               verbose_name="Опыт работы")

    def __str__(self):
        return self.role


class Education(models.Model):
    univer = models.CharField(max_length=250)
    specialty = models.CharField(max_length=250)
    data_end = models.DateField(auto_now=False)

    def __str__(self):
        return self.univer


class AddEducation(models.Model):
    univer = models.CharField(max_length=250)
    specialty = models.CharField(max_length=250)
    data_end = models.DateField(auto_now=False)

    def __str__(self):
        return self.univer


class Skill(models.Model):
    about = models.TextField(max_length=2000,
                               help_text="Кратко о себе",
                               verbose_name="О себе")
    hobbies = models.TextField(max_length=2000,
                               help_text="Введите свое хобби",
                               verbose_name="Хобби")

    def __str__(self):
        return self.about







