__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
https://www.codewars.com/kata/514a024011ea4fb54200004b

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 

For example:
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

def domain_name(url):
    """
    :param url: input url
    :return: domain only from the input url
    """

    domain = url

    # strip http:// or https://
    if domain.startswith("http://"):
        domain = domain[7:]
    elif domain.startswith("https://"):
        domain = domain[8:]

    # strip www.
    if domain.startswith("www."):
        domain = domain[4:]

    # strip extension and everything after it
    index = domain.find(".")
    if index != -1:
        domain = domain[:index]

    # return just the domain
    return domain
