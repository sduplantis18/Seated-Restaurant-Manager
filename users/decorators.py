from os import name
from learning_log.settings import LOGIN_URL
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def customer_required(function=None, name=REDIRECT_FIELD_NAME,  login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a studen, 
    redirects to the log-in page if necessary. 
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_customer,
        login_url = login_url,
        redirect_field_name=REDIRECT_FIELD_NAME
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def manager_required(function=None, name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a studen, 
    redirects to the log-in page if necessary. 
    '''

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_manager,
        login_url = login_url,
        redirect_field_name=REDIRECT_FIELD_NAME
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


