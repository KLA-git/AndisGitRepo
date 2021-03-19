def bewölkerung(n):
    counter = 0
    g1=12.3
    g2=19.1
    g3=15.5
    g4=16.3
    while counter < n:
        counter +=1
        g4=g4*0.972+g3*0.066
        g3=g3*0.925+g2*0.0029
        g2=g2*0.97+g1*0.066
        g1=g1*0.93+g2*0.02
    print(g1,g2,g3,g4)


add(5)