a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

delta=(b**2)-(4*a*c)
print(delta)


birincik=( -b +( delta ** 0.5)) /(2*a)
ikincik=-b /(2*a)

print("Denklemin birinci kökü: {}\nİkinci Kökü: {}".format(birincik,ikincik))

print("Kök: {}x2+{}x+{}".format(a,b,c))