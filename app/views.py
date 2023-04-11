from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from app.models import *

def Show_dept(request):
    LOD = dept.objects.all()
    d = {'details' : LOD}
    return render(request, 'Show_dept.html', d)


def Show_emp(request):
    LOE = emp.objects.all()
    LOE = emp.objects.filter(hiredate__month='09')
    LOE = emp.objects.filter(hiredate__year='1981')
    LOE = emp.objects.filter(hiredate__day='03')
    LOE = emp.objects.filter(ename__startswith='s')
    LOE = emp.objects.filter(ename__endswith='s')
    LOE = emp.objects.filter(ename__contains='s')
    LOE = emp.objects.filter(sal__gt='1000')
    LOE = emp.objects.filter(ename__in=('SMITH','SCOTT', 'ALLEN'))
    LOE = emp.objects.filter(ename__regex=r'[a-zA-Z]{6}')
    LOE = emp.objects.filter(Q(deptno='20') & Q(sal__gt='1000'))
    LOE = emp.objects.filter(Q(ename__startswith='s') & Q(ename__endswith='h'))
    LOE = emp.objects.filter(Q(ename__startswith='s') | Q(ename__endswith='s'))
    LOE = emp.objects.all()
    
    
    d = {'detail' : LOE}
    return render(request, 'Show_emp.html', d)