# INITIALIZATION

import callr
api = callr.Api("harleywebservices_1","Junior4210@1")
testSMS = api.call('sms.send','SMS',"+12532057177","SKU #12345 needs replen",None)

def SendSMS():
    return testSMS