from chrono import Chrono

t=Chrono(1,46,9)
#a=1
t2=Chrono(2,46,9)
t3=Chrono(1,46,9)
assert t==t3  # t.__eq__(t2)
t.clone()