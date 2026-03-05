

def orquest_sesion_login(x):
    x.clean_format_inputs()
    x.username_text_format()
    x.username_length()
    x.password_lenght()
    x.password_banned()
    x.safe_password_format()
    x.email_format_ok()
    x.email_domain_ok()
    return x.process_ok()
   
