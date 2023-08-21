#!/usr/bin/env python3

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

class Person:
    def __init__(self, name = None, job = None):
        self._name = None
        self._job = None
        
        if name is not None:
            self.set_name(name)

        if job is not None:
            self.set_job(job)


    def get_name(self):
        return self._name
    
    def get_job(self):
        return self._job
    
    def set_name(self, value):
        if value is None:
            self._name = None
        elif isinstance(value, str) and (len(value) >= 1 and len(value) < 25):
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    
    def set_job(self, value):
        if value in APPROVED_JOBS:
             self._job = value
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)
