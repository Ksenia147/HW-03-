from django import template


register = template.Library()

@register.filter()
def censor(value):
   censor_word = ["воображаемого", "способах"]

   return ' '.join([i[0]+'*' * (len(i)-1) if i in censor_word else i for i in value.split()])
