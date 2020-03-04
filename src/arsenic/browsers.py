from arsenic.session import Session, CompatSession


class Browser:
    defaults = {}
    session_class = Session
    capabilitieskey= 'desiredCapabilities'

    def __init__(self, **overrides):
        self.capabilities = {**self.defaults, **overrides}

class Frowser(Browser):
    def __init__(self, foptions, **args):
      self.capabilities = {**self.defaults, foptions, **args}


class Firefox(Frowser):
    capabilitieskey= 'capabilities'
    defaults = {
        "browserName": "firefox",
        "acceptInsecureCerts": True,
    }


class Chrome(Browser):
    session_class = CompatSession
    defaults = {"browserName": "chrome"}


class PhantomJS(Browser):
    session_class = CompatSession
    defaults = {
        "browserName": "phantomjs",
        "version": "",
        "platform": "ANY",
        "javascriptEnabled": True,
    }


class InternetExplorer(Browser):
    session_class = Session
    defaults = {
        "browserName": "internet explorer",
        "version": "",
        "platform": "WINDOWS",
    }


IE = InternetExplorer
