import time

if __name__=='__main__':
    # Replacing %x and %o and converting the value to different bases:
    """
    format supports binary numbers
    
    """
    print('int:{0:d},hex:{0:x},oct:{0:o},bin:{0:b}'.format(42))

    # with Ox,Oo, or Ob as prefix
    print('int:{0:d},hex: {0:#x}, oct: {0:#o},bin:{0:#b}'.format(42))

    # Using the comma as a thousands separator:
    print('{:,}'.format(123456789))

    # Expressing a percentage:
    points = 19
    total = 22
    print('percentage: {:.2%}'.format(points/total))

    # Using datetime
    import datetime
    d = datetime.datetime(2010, 7, 4, 12, 15, 58)
    print('{:%Y-%m-%d %H:%M:%S}'.format(d))
    now_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print('now_time:',now_time)