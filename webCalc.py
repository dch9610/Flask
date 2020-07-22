def Obs(h,w):
     stdW = (h-100)*0.85
     Ob= w/stdW*100
     if Ob <=90:
        return '저체중', '/static/image/저체중.jpeg'
     elif Ob <=110:
        return '정상', '/static/image/정상.png'
     elif Ob <=120:
        return '과체중', '/static/image/과체중.jpeg'
     else:
        return '비만', '/static/image/비만.jpeg'
