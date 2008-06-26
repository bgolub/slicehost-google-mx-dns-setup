#!/usr/bin/env python

import sys
from pyactiveresource import ActiveResource

if not len(sys.argv) == 3:
    print 'usage: %s zone_id api_password' % sys.argv[0]
    sys.exit()

zone_id = sys.argv[1]
api_password = sys.argv[2]

api_site = 'https://%s@api.slicehost.com/' % api_password

class Zone(ActiveResource):
    class Meta:
        site = api_site
        
class Record(ActiveResource):
    class Meta:
        site = api_site

data = (
    ('MX', 'ASPMX.L.GOOGLE.COM.',      10),
    ('MX', 'ALT1.ASPMX.L.GOOGLE.COM.', 20),
    ('MX', 'ALT2.ASPMX.L.GOOGLE.COM.', 20),
    ('MX', 'ASPMX2.GOOGLEMAIL.COM.',   30),
    ('MX', 'ASPMX3.GOOGLEMAIL.COM.',   30),
    ('MX', 'ASPMX4.GOOGLEMAIL.COM.',   30),
    ('MX', 'ASPMX5.GOOGLEMAIL.COM.',   30),
    ('TXT', 'v=spf1 include:aspmx.googlemail.com ~all', 0),
)

z = Zone.find(id=zone_id)[0]
for d in data:
    r = Record(data=d[1], record_type=d[0], aux=d[2], zone_id=z.id, name=z.origin)
    print r.save()
