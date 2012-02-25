


##### Views #####

def dashboard(request):
    feed = build_feed(request.user.get_profile())
    return

def login(request):
    return

def register(request):
    return



##### Functions #####

def build_feed(profile):
    return