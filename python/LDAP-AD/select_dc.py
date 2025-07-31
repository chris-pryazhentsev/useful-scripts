import random
import dns.resolver
import ldap3

def choose_domaincontroller():
    DOMAIN = "ldap.MYDOMAIN.com"
    resolver = dns.resolver.Resolver()
    srv_records=resolver.resolve('_ldap._tcp.'+ DOMAIN, 'SRV')

    domain_controllers = []

    for host in srv_records:
        domain_controllers.append(str(host.target))

    return random.choice(domain_controllers)

print(choose_domaincontroller())