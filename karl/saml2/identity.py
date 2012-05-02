from pyramid.view import view_config


@view_config(name='sso', renderer='templates/login.pt')
def sign_on(context, request):
    """ Perform the SAML2 SSO dance.

    - If the request already has valid credentials, process the 'SAMLRequest'
      query string value and return a POSTing redirect.

    - If processing the POSTed login form, authenticate.

    - If no authenticated user is known, display the login form.
    """
    return {'hidden': request.GET.items()}
