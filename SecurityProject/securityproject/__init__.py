from pyramid.session import SignedCookieSessionFactory
my_session_factory = SignedCookieSessionFactory('DNkb8BXD1eZuOQUsFjHj0OXQ1YMjU0K8iAHsnCBwTj7V0p9ju27M5NHy0TjkyysB', httponly = True)
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import engine_from_config
from .models import (
    DBSession,
    Base,
    )

from pyramid.config import Configurator
from pyramid_mailer.mailer import Mailer


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    authn_policy = AuthTktAuthenticationPolicy(
        'yHWnm37QQhIuKCoaMV3B2eUYxI9irkkq0qxNJSFLJszWuFp4ZcMYn8pTw70d4Ziq', http_only=True, include_ip=True, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    #config.include('pyramid_mailer')
    config.registry['mailer'] = Mailer.from_settings(settings)
    config.set_session_factory(my_session_factory)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('css', 'CompanyFace/css', cache_max_age=3600)
    config.add_static_view('js', 'CompanyFace/js', cache_max_age=3600)
    config.add_static_view('img', 'CompanyFace/img', cache_max_age=3600)
    config.add_static_view('fonts', 'CompanyFace/fonts', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('logout','logout')
    config.add_route('login', 'login')
    config.add_route('register', 'register')
    config.add_route('validate', 'validate')
    config.add_route('db', 'db')
    config.scan()
    return config.make_wsgi_app()
