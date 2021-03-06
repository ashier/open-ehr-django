from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from contactus.models import UserEmail
from open-ehr.contactus.forms import EmailForm
from open-ehr.settings import media_url
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_user(request):
    error_msg="none"
    error_type="none"
   #req_method=request.method
    if request.method == 'POST':
        form=EmailForm(request.POST)
        if not request.POST.get('email',''):
            error_msg="Enter Email ID"
            error_type="error"
        if (error_type=="none"):
            if form.is_valid():
                data=request.POST.get('email')
                p=UserEmail(email=data,email_verfied_status='T',email_verification_token='ttt')
                p.save()
                error_msg="Thanks"
                error_type="success"
            else:
                error_msg="Enter Proper Email ID"
                error_type="error"
    #return render_to_response('contactus.html',{'type': error_type,'errors': error_msg})
    if error_type=="none":
        return render_to_response('contactus/contactus.html')
    else:
        #return render_to_response('contactus.html',{'type' : error_type, 'errors':error_msg, 'rmethod': req_method})
        #return HttpResponseRedirect("http://www.open-ehrhx.com/")
        return HttpResponse(error_type)




def thanks(request):
    return render_to_response('thanks.html')
