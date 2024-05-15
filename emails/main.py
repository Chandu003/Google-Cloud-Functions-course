
def send_mail(request):
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    from flask import abort
    parameters = ('sender','receiver','message','subject')
    request_json = request.get_json(silent=True)
    sender, receiver, subject, message = ''
    if request and all(k in request_json for k in parameters):
        sender = request_json['sender']
        receiver = request_json['receiver']
        message = request_json['message']
        subject = request_json['subject']
    else:
        abort(400)
    message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject=subject,
        html_content=message)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        _ = sg.send(message)
        return 'OK', 200
    except Exception as e:
        return e, 400