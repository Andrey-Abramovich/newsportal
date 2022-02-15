from django import template


register = template.Library()


@register.filter(name='censor')
def censor(value):
    censor_list = []
    value1 = (str(value)).split()
    with open('news/templatetags/censor_list.txt', 'r') as f:
        censor_list = f.read().split(", ")
    for i, n in enumerate(censor_list):
        n = n.lower()
        for j, m in enumerate(value1):
            m = m.lower()
            if n == m:
                value1[j] = '***'
        value = ' '.join(value1)
    return str(value)