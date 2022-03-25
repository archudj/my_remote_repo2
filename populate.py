import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','archanajobs.settings')
import django
django.setup()

from jobsapp.models import *
from random import *
from faker import Faker

fake = Faker()
def phone_nogen():
    d1 = randint(6,9)
    num = str(d1)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Leader','Software Engineer','Associate Engineer'))
        feligibility = fake.random_element(elements=('B-tech','M-tech','MCA','Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phone_nogen()
        HydJobs_record = HydJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, email=femail, phone_no=fphonenumber)
        ChennaiJobs_record = ChennaiJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, email=femail, phone_no=fphonenumber)
        BglrJobs_record = BglrJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, email=femail, phone_no=fphonenumber)
        PuneJobs_record = PuneJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, email=femail, phone_no=fphonenumber)
n= int(input('Enter no of records to insert:'))
populate(n)
print(f'{n} Records inserted Successfully')
