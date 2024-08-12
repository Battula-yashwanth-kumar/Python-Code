class Dad:
    basketball=6
class Son(Dad):
    dance=1
    # basketball=9
class grandson(Son):
    dance=1

hello=grandson()
print(hello.basketball);