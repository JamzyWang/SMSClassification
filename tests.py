#-*- coding: utf-8 -*-

from mmseg import Algorithm, dict_load_defaults

def cuttest(text):
    wlist = [word for word in Algorithm(text)]
    tmp = "/".join(wlist)
    print tmp
    print "================================"

def benchmark(text):
    import time
    dict_load_defaults()
    print ">>>> load dict done!"

    for i in range(100):
        begin = time.time()
        wlist = [word for word in Algorithm(text)]
        end = time.time()
        print ">>>> times: %f" % float(end-begin)

if __name__=="__main__":
    cuttest(u"你昨天去哪了啊")
    cuttest(u"我的手机丢了。")
    cuttest(u"我是房东，这个月的房租打到这个账号。")
    cuttest(u"明天这个项目必须完成。")
    cuttest(u"一次性交一百元。")
    cuttest(u"你也喜欢看小时代？。")
    cuttest(u"昨天皇马又输了，真他妈扫兴。")