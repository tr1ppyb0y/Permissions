from django.db import models

class HeadQuater(models.Model):
    # id is auto generated.
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)


class Company(models.Model):
    # id is auto generated.
    parent = models.ForeignKey(HeadQuater, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150, null=False, blank=False, unique=True)


class Organization(models.Model):
    # id is auto generated.
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)


class PurchaseGroup(models.Model):
    # id is auto generated.
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)

class Location(models.Model):
    # id is auto generated.
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)

class Plant(models.Model):
    # id is auto generated.
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)


class StorageLocation(models.Model):
    # id is auto generated.
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)

class Department(models.Model):
    # id is auto generated.
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)


class CostCenter(models.Model):
    # id is auto generated.
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    # foreign key also act as one-to-one.
    department = models.ForeignKey(Department, on_delete=models.CASCADE)    # unique = True?
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
