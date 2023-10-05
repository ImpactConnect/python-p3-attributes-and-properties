#!/usr/bin/env python3


class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]


    def __init__(self, name, job):
        self._name = name  
        self._job = job  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) <= 25:
            self._name = value.title()  
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")

person = Person("john doe", "Engineer")
print(person.name)  
print(person.job)  

person.name = "Buddy The Super Amazing Fantastic Person With a Very Long Name"

person.job = "Driver"

