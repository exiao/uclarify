from django.template import Library

register = Library()

@register.filter
def get_range( value ):
  """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
  """
  return range( int(value) )


@register.filter
def get_subtracted_range_by_5( value ):
  return range( 5 - int(value) )

@register.filter
def multiply(value, arg):
    # you would need to do any localization of the result here
    return value * arg