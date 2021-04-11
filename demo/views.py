from django.conf import settings
from django.urls import reverse
from django.http import (HttpResponse, HttpResponseRedirect,
                         HttpResponseServerError)
#from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

from onelogin.saml2.auth import OneLogin_Saml2_Auth
from onelogin.saml2.settings import OneLogin_Saml2_Settings
from onelogin.saml2.utils import OneLogin_Saml2_Utils


def init_saml_auth(req):
    auth = OneLogin_Saml2_Auth(req, custom_base_path=settings.SAML_FOLDER)
    return auth


def prepare_django_request(request):
    result = {
        'https': 'on' if request.is_secure() else 'off',
        'http_host': request.META['HTTP_HOST'],
        'script_name': request.META['PATH_INFO'],
        'server_port': request.META['SERVER_PORT'],
        'get_data': request.GET.copy(),
        'post_data': request.POST.copy(),
        'query_string': request.META['QUERY_STRING']
    }
    return result

def index(request):
    print('in index')
    req = prepare_django_request(request)
    print("here----------___>",req,request)
    auth = init_saml_auth(req)
    errors = []
    not_auth_warn = False
    success_slo = False
    attributes = False
    paint_logout = False

    if 'sso' in req['get_data']:
        return HttpResponseRedirect(auth.login())

    elif 'slo' in req['get_data']:
        name_id = None
        session_index = None
        if 'samlNameId' in request.session:
            name_id = request.session['samlNameId']
        if 'samlSessionIndex' in request.session:
            session_index = request.session['samlSessionIndex']
        slo_built_url = auth.logout(name_id=name_id, session_index=session_index)
        request.session['LogoutRequestID'] = auth.get_last_request_id()
        print ('set logout id'+auth.get_last_request_id())		
        return HttpResponseRedirect(slo_built_url)


    if 'samlUserdata' in request.session:
        paint_logout = True
        if len(request.session['samlUserdata']) > 0:
            attributes = request.session['samlUserdata'].items()
    #return render_to_response('index.html', {'errors': errors, 'not_auth_warn': not_auth_warn, 'success_slo': success_slo, 'attributes': attributes,'paint_logout': paint_logout}, context_instance=RequestContext(request))
    return render(None,'index.html',
                              {'errors': errors,
                               'not_auth_warn': not_auth_warn,
                               'success_slo': success_slo,
                               'attributes': attributes,
                               'paint_logout': paint_logout})

def prepare_from_django_request(request):
	print('=======req===='+str(request))
	return {
        'http_host': request.META['HTTP_HOST'],
        'script_name': request.META['PATH_INFO'],
        'server_port': request.META['SERVER_PORT'],
        'get_data': request.GET.copy(),
        'post_data': request.POST.copy()
    }	
	
def acs (request):
	print ("in acs")
	req = prepare_django_request(request)
	auth = init_saml_auth(req)
	errors = []
	not_auth_warn = False
	success_slo = False
	attributes = False
	paint_logout = False
	request_id = None
	if 'slo' in req['get_data']:
	   print ("asdfasdfasdf in slo")
	if 'AuthNRequestID' in request.session:
		request_id = request.session['AuthNRequestID']
	if 'LogoutRequestID' in request.session:
		request_id = request.session['LogoutRequestID']
		request.session.flush()
		return HttpResponseRedirect('/')

	auth.process_response(request_id=request_id)
	errors = auth.get_errors()
	not_auth_warn = not auth.is_authenticated()
	if not errors:
		if 'AuthNRequestID' in request.session:
			del request.session['AuthNRequestID']
		request.session['samlUserdata'] = auth.get_attributes()
		request.session['samlNameId'] = auth.get_nameid()
		request.session['samlSessionIndex'] = auth.get_session_index()
		if 'RelayState' in req['post_data'] and OneLogin_Saml2_Utils.get_self_url(req) != req['post_data']['RelayState']:
			return HttpResponseRedirect(auth.redirect_to(req['post_data']['RelayState']))
	print ('in acs error'+str(errors))
	return HttpResponseRedirect("/")			
