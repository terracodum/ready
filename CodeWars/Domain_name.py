def domain_name(url):
    if "//" in url:
        ind = url.index("//")
        name = url[ind+2::]
    fin = name.find(".")
    if "www." in name:
        name = name[fin+1::]
        fin = name.find(".")
        name = name[:fin:]
    else:
        name = name[:fin:]
    return name

print(domain_name("http://www.zombie-bites.com"))