from .checker import CSPChecker
from .cspcheck_whitelist import CSPCheckWhitelist

class CSPScriptWhitelistBypassChecker(CSPChecker):
    def myoptions(cls):
        return {'angular':list, 'jsonp':list, 'jsonpeval':list}
    
    def check(self, headers, opt_options=dict()):
        me = self.__class__.__name__
        if me in opt_options.keys():
            options = opt_options[me]
        else:
            options = {}
        return CSPCheckWhitelist(self.getcsp(headers)).check(options)
