import xmlrpc.client
import datetime

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    for n in range(1, 20):
        print("Is {} even? {}".format(n, str(proxy.is_even(n))))


proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

today = proxy.today()
# convert the ISO8601 string to a datetime object
converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
print("Today: %s" % converted.strftime("%d.%m.%Y, %H:%M"))