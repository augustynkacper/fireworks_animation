def get_roots(W, a,b,c,start, end):
    if a==0:return
    delta = b*b - 4*a*c
    x1 = (-b - delta**0.5)/(2*a)
    x2 = (-b + delta**0.5)/(2*a)
    if end[0] > start[0]: 
        x = int(min(x1, x2))
        if x<0:
            return -50
        return x-50
    x = int(max(x1, x2))
    if x>W:
        return W+50
    return x+50

def get_coefficients(H, start, end):
    x1, y1 = end
    x2, y2 = start
    y1 = H - y1
    y2 = H - y2
    if x1==x2:return
    a=(y2-y1)/(x2-x1)**2
    b=-2*x1*a
    c=y1+((x1/(x2-x1))**2)*(y2-y1)
    return a, b, c

def get_velocity(W, root, end):
    if root<end[0]: root+=25
    else: root-=25
    d = abs(root-end[0])
    if d/W > 0.6:  return 12
    elif d/W >0.1 and d/W < 0.2:  return 2
    elif d/W >=0.1 and d/W < 0.3:  return 4
    elif d/W<0.05:  return 0.5
    elif d/W < 0.1:  return 1
    else:  return 7