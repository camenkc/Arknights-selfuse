# -*- coding:utf-8 -*-
# @author：LuffyLSX
# @version：1.0
# @update time：2019/8/31

import os,time
import cv2

localAdbDevice = ' 127.0.0.1:62025 '

def connect():
    try:
        print('连接成功')
    except:
        print('连接失败')

def click(x, y):
    print('NowClick %s %s'%(x,y))
    os.system('adb -s'+localAdbDevice+ 'shell input tap %s %s' % (x, y))

def swipe(fromX,fromY,toX,toY,time=2000):
    try:
        os.system('adb -s'+localAdbDevice+'shell input swipe %s %s %s %s %s '%(fromX,fromY,toX,toY,time))
    except:
        print('未能成功滑动')
def screenshot():
    path = os.path.abspath('.') + '\images'
    os.system('adb -s'+localAdbDevice+' shell screencap /data/screen.png')
    os.system('adb -s'+localAdbDevice+'pull /data/screen.png %s' % path)

def resize_img(img_path):
    img1 = cv2.imread(img_path, 0)
    img2 = cv2.imread('images/screen.png', 0)
    height, width = img1.shape[:2]
    ratio = 2560 / img2.shape[1]
    size = (int(width/ratio), int(height/ratio))
    return cv2.resize(img1, size, interpolation = cv2.INTER_AREA)

def Image_to_position(image, m = 0):
    image_path = 'images/' + str(image) + '.png'
    screen = cv2.imread('images/screen.png', 0)
    template = cv2.imread(image_path, 0)
    #template = resize_img(image_path)
    methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED]
    image_x, image_y = template.shape[:2]
    result = cv2.matchTemplate(screen, template, methods[m])
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(image + str(max_val))
    if max_val > 0.85:
        global center
        center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
        print(center)
        return center
    else:
        return False
    
def run(n):
    images = ['start-go1', 'start-go2', 'end', 'level up']
    round = 0
    # Image_to_position('start-go1')
    # time.sleep(2)
    # Image_to_position('start-go2')
    # while not Image_to_position('end'):
    #     time.sleep(5)
    while True:
        screenshot()
        now = ''
        for image in images:
            if Image_to_position(image, m = 0) != False:
                print(image)
                now = image
                time.sleep(0.5)
                click(center[0], center[1])
                
        if now == 'end':
            time.sleep(0.8)
            round = round + 1
            if round == n:
                break
        
def returnToIndex():
    while True:
        screenshot()
        now = ''
        if Image_to_position('houTuiJian', m = 0) != False:
            time.sleep(0.1)
            click(center[0], center[1])
        screenshot()
        if Image_to_position('huoDongGuanBiAnNiu', m = 0) != False:
            print('huoDongGuanBiAnNiu.png')
            time.sleep(0.1)
            click(center[0], center[1])
        screenshot()
        if Image_to_position('tuiChuQueRen', m = 0) != False:
            print('tuiChuQueRen.png')
            click(center[0], center[1])
            time.sleep(0.5)
        screenshot()
        if Image_to_position('zhuYeGanYuan',m = 0) != False:
            break


        
def shouHuoJiJian():
    returnToIndex()
    time.sleep(0.1)
    screenshot()
    if Image_to_position('zhuYeJiJian', m = 0) != False:
        print('zhuYeJiJian.png')
        time.sleep(0.1)
        click(center[0], center[1])
    
    time.sleep(5)
    
    screenshot()
    if Image_to_position('jiJianTiXing', m = 0) != False:
        print('jiJianTiXing.png')
        time.sleep(0.1)
        click(center[0], center[1])    
    
    for i in range(0,10):
        time.sleep(0.3)
        click(212,700)
    time.sleep(0.1)
    click(400,200)
    
    
    #撤下所有干员
    screenshot()
    if Image_to_position('jinZhuZongLan', m = 0) != False:
            print('jinZhuZongLan.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(2)
    
    
    
    screenshot()
    if Image_to_position('cheXiaGanYuan', m = 0) != False:
            print('cheXiaGanYuan.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1)
    
    
    
    
    click(1200,200)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)
    
    click(1200,370)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)
    
    click(1200,580)
    time.sleep(0.1) 
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)      
    
    click(1200,715)
    time.sleep(0.1)
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)  
        
    #滑动
    swipe(1050,648,1026,140)
    click(1207,140)
    
    click(1207,243)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)       
    
    click(1207,399)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(1)   
    
    click(1207,554)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)  

    #滑动
    swipe(1050,648,1026,140)
    click(1207,140)
    
    click(1207,117)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5) 

    click(1207,232)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)

    click(1207,415)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)

    click(1207,563)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)

    click(1207,705)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)

    #滑动
    swipe(1050,648,1026,140)
    click(1207,140)
    
    click(1207,220)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)


    click(1207,376)
    time.sleep(0.1)    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)    

        
    screenshot()
    if Image_to_position('houTuiJian', m = 0) != False:
        print('houTuiJian.png')
        click(center[0], center[1])
        time.sleep(0.5)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #放置所有干员
    
    screenshot()
    if Image_to_position('jinZhuZongLan', m = 0) != False:
            print('jinZhuZongLan.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1)
    
    
    click(673,214)
    time.sleep(0.1)    
    click(485,242)
    time.sleep(0.1)
    click(485,522)
    time.sleep(0.1)
    click(638,235)
    time.sleep(0.1)
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)
    
    click(673,365)
    time.sleep(0.1)    
    click(485,242)
    time.sleep(0.1)
    click(485,522)
    time.sleep(0.1) 
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)
    
    click(673,569)
    time.sleep(0.1)    
    click(485,242)
    time.sleep(0.1)
    click(485,522)
    time.sleep(0.1) 
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)    
    
    click(673,710)
    time.sleep(0.1)    
    click(485,242)
    time.sleep(0.1)
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)     
    
    
    #滑动
    swipe(1050,648,1026,140)
    click(1207,140)
    
    click(673,336)
    time.sleep(0.1)    
    click(485,242)
    time.sleep(0.1)
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)    
    
    click(673,492)
    time.sleep(0.1)    
    click(485,242)
    time.sleep(0.1) 
    click(485,515)
    time.sleep(0.1)
    click(626,245)
    time.sleep(0.1)
    click(626,529)
    time.sleep(0.1)
    click(773,242)
    time.sleep(0.1)
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
            print('tuiChuQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)    
    
    click(673,654)
    time.sleep(0.1)    
    click(485,242)
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)    
    time.sleep(1)
    #滑动
    swipe(1050,648,1026,140)
    click(1207,140)
    
    click(673,145)
    time.sleep(0.1)    
    click(485,242)
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)    
    
    click(673,298)
    time.sleep(0.1)    
    click(485,242)
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)    
    
    click(673,471)
    time.sleep(0.1)    
    click(485,242)
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)     
    
    click(673,650)
    time.sleep(0.1)    
    click(485,242)
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)     
    
    #滑动
    swipe(1050,648,1026,140)
    click(1207,140)
    
    click(673,220)
    time.sleep(0.1)    
    click(485,242)
    time.sleep(0.1) 
    click(485,515)
    time.sleep(0.1)
    click(626,245)
    time.sleep(0.1)
    click(626,529)
    time.sleep(0.1)
    click(773,242)
    time.sleep(0.1)
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
            print('tuiChuQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)
    
    click(673,388)
    time.sleep(0.1)    
    click(485,242)
    screenshot()
    if Image_to_position('jiJianQueRen', m = 0) != False:
            print('jiJianQueRen.png')
            time.sleep(0.1)
            click(center[0], center[1])
    time.sleep(1.5)     
    
    screenshot()
    if Image_to_position('houTuiJian', m = 0) != False:
        print('houTuiJian.png')
        click(center[0], center[1])
        time.sleep(0.5)    
    
    
    
    
    ############################
    #收取会客室线索
    swipe(1167,368,200,368,500)
    click(1092,220)
    time.sleep(1.5)
    click(415,602)
    time.sleep(1.5)
    
    click(391,244)
    time.sleep(1.5)
    screenshot()
    if Image_to_position('quXiaXianSuo', m = 0) != False:
        print('quXiaXianSuo.png')
    else:
        click(1072,233)
    time.sleep(1.5)
    
    click(165,489)
    time.sleep(1.5)
    screenshot()
    if Image_to_position('quXiaXianSuo', m = 0) != False:
        print('quXiaXianSuo.png')
    else:
        click(1072,233)
    time.sleep(1.5)

    click(307,313)
    time.sleep(1.5)
    screenshot()
    if Image_to_position('quXiaXianSuo', m = 0) != False:
        print('quXiaXianSuo.png')
    else:
        click(1072,233)
    time.sleep(1.5)

    click(384,517)
    time.sleep(1.5)
    screenshot()
    if Image_to_position('quXiaXianSuo', m = 0) != False:
        print('quXiaXianSuo.png')
    else:
        click(1072,233)
    time.sleep(1.5)

    click(509,209)
    time.sleep(1.5)
    screenshot()
    if Image_to_position('quXiaXianSuo', m = 0) != False:
        print('quXiaXianSuo.png')
    else:
        click(1072,233)
    time.sleep(1.5)

    click(600,463)
    time.sleep(1.5)
    screenshot()
    if Image_to_position('quXiaXianSuo', m = 0) != False:
        print('quXiaXianSuo.png')
    else:
        click(1072,233)
    time.sleep(1.5)

    click(728,259)
    time.sleep(1.5)
    screenshot()
    if Image_to_position('quXiaXianSuo', m = 0) != False:
        print('quXiaXianSuo.png')
    else:
        click(1072,233)
    time.sleep(1.5)

    click(425,656)
    time.sleep(1.5)
    
    screenshot();
    if Image_to_position('houTuiJian', m = 0) != False:
        print('houTuiJian.png')
        click(center[0],center[1])
        time.sleep(0.5)
    
    
    #捐3个线索
    click(412,608)
    time.sleep(1.5)
    click(1196,393)
    time.sleep(1.5)
    
    click(272,252)
    time.sleep(0.5)
    click(1195,147)
    time.sleep(0.5)
    '''
    click(272,252)
    time.sleep(0.5)
    click(1195,279)
    time.sleep(0.5)
    
    click(272,252)
    time.sleep(0.5)
    click(1195,431)
    time.sleep(0.5)
    '''  #这里注释掉捐赠另俩个的代码
    screenshot();
    if Image_to_position('juanZenGuanBi', m = 0) != False:
        print('juanZenGuanBi.png')
        click(center[0],center[1])
        time.sleep(0.5)    
    
    
    #收取新线索
    screenshot();
    if Image_to_position('shouQuXinXianSuo', m = 0) != False:
        print('shouQuXinXianSuo.png')
        click(center[0],center[1])
        time.sleep(0.5)    
    
    screenshot();
    if Image_to_position('lingQuXianSuo', m = 0) != False:
        print('lingQuXianSuo.png')
        click(center[0],center[1])
        time.sleep(0.5)    
    
    
    screenshot()
    if Image_to_position('houTuiJian', m = 0) != False:
            click(center[0], center[1])
            time.sleep(0.5) 
            
    screenshot()
    if Image_to_position('houTuiJian', m = 0) != False:
            click(center[0], center[1])
            time.sleep(0.5)
            
    screenshot()
    if Image_to_position('houTuiJian', m = 0) != False:
            click(center[0], center[1])
            time.sleep(0.5)
    
    screenshot()
    if Image_to_position('tuiChuQueRen', m = 0) != False:
        print('tuiChuQueRen.png')
        click(center[0], center[1])
        time.sleep(0.5)

def shouQuXinYong():
    returnToIndex()
    
    screenshot()
    if Image_to_position('caiGouZhongXin', m = 0) != False:
        print('caiGouZhongXin.png')
        click(center[0], center[1])
        time.sleep(0.5)
        
    screenshot()
    if Image_to_position('xinYongJiaoYiSuo', m = 0) != False:
        print('xinYongJiaoYiSuo.png')
        click(center[0], center[1])
        time.sleep(0.5)

    click(1026,45)
    time.sleep(0.5)
    click(1026,45)
    time.sleep(0.5)
    
    temp=0
    screenshot()
    while Image_to_position('jianJia75', m = 0) != False:#买完所有-75的物品
        print('jianJia75.png')
        click(center[0], center[1])
        time.sleep(0.5)
        
        screenshot()
        if Image_to_position('gouMaiWuPin', m = 0) != False:
            temp+=1
            print('gouMaiWuPin.png')
            click(center[0], center[1])
            time.sleep(0.5)
            click(center[0], center[1])
            time.sleep(0.5)
        screenshot()
        if temp>=3:
            break
    returnToIndex()

def shouQuRenWu():
    returnToIndex()
    
    screenshot()
    if Image_to_position('zhuYeRenWu', m = 0) != False:
        print('zhuYeRenWu.png')
        click(center[0], center[1])
        time.sleep(0.5)
    
    screenshot()
    if Image_to_position('riChangRenWu', m = 0) != False:
        print('riChangRenWu.png')
        click(center[0], center[1])
        time.sleep(0.5) 
        
    screenshot()
    while Image_to_position('dianJiLingQu', m = 0) != False:
        print('dianJiLingQu.png')
        click(center[0],center[1])
        time.sleep(1.5)
        click(center[0],center[1])
        time.sleep(1.5)
        click(center[0],center[1])
        time.sleep(1.5)
        screenshot()
    
    screenshot()
    if Image_to_position('zhouChangRenWu', m = 0) != False:
        print('zhouChangRenWu.png')
        click(center[0], center[1])
        time.sleep(0.5)
        screenshot()
        while Image_to_position('dianJiLingQu', m = 0) != False:
            print('zhuYeRenWu.png')
            click(center[0],center[1])
            time.sleep(1.5)
            click(center[0],center[1])
            time.sleep(1.5)
            click(center[0],center[1])
            time.sleep(1.5)
            screenshot()
  
    returnToIndex()
    
    
    
if __name__ == '__main__':
    connect()
    '''for i in range(int(input('输入刷图次数' + '\n'))):
        run()
        time.sleep(3)'''
    C1=False
    C2=False
    C3=False
    print('是否需要收取基建（1/0）：')
    if int(input())==1:
        C1=True;
    
    print('是否需要收取每日信用（1/0）：')
    if int(input())==1:
        C2=True;
    
    print('是否需要收取任务（1/0）：')
    if int(input())==1:
        C3=True;
    
    returnToIndex()
    if C1:
        shouHuoJiJian()#基建收菜  1280*720窗口模式下95%稳定性
    if C2:
        shouQuXinYong()#信用商店收取
    if C3:
        shouQuRenWu()#收取任务奖励
    
    
    #run(int(input('输入刷图次数' + '\n')))
    os.system('adb kill-server -s'+localAdbDevice)
    