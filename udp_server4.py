# -*- coding: utf-8 -*-
#4.0版本
from math import e
import sys
import threading
import time
import os
import glob
import socket
import json
from typing import OrderedDict
import smtplib
# email 用于构建邮件内容
from email.header import Header
from email.mime.text import MIMEText
import random

class Check_YZM(object):
    def __init__(self) -> None:
        super().__init__()
        self.checkyzm={}
        self.numbers=0
    
    def check_yzm(self,username,yzm):
        yzm_true=self.checkyzm[username]
        if yzm==yzm_true:
            return True
        else:
            return False
    
    def append_yzm(self,username,yzm):
        self.checkyzm[username]=yzm
    
    def clear_all(self):
        self.checkyzm={}

class Emailsender(object):
    '''
    发送邮箱
    {"1":{"email":"2285273839@qq.com","password":"3047881xfb","successtimes":0},"2":{"email":"2285273839@qq.com","password":"3047881xfb","usedtimes":0}}
    '''
    def __init__(self,email_queue):
        self.email_queue=email_queue
        self.length=len(self.email_queue)
        self.index=1
        self.email=self.email_queue[str(self.index)]["email"]
        self.password=self.email_queue[str(self.index)]["password"]
        self.to_='接收人'
        self.subject_='标题'
        self.main_message="%s 验证号码,请填写以完成注册，不要泄露"
        self.total=0#成功发送总数
        self.yzm_length=6#验证码长度默认为6
    def next(self):
        '''
        切换下一个
        '''
        if self.index==self.length:
            self.index=1
        else:
            self.index+=1
        self.email=self.email_queue[str(self.index)]["email"]
        self.password=self.email_queue[str(self.index)]["password"]

    def send_email(self,to_addr='1957894238@qq.com'):
        '''
        发送验证码，如果成功就返回验证码，如果失败就返回False
        '''
        fail_times=0
        while True:
            '''
            if fail_times>=self.length:
                return False
            '''
            
            smtp_server = 'smtp.qq.com'
            rand_yzm=self.rand_yzm()
            msg = MIMEText(self.main_message%(rand_yzm),'plain','utf-8')
            msg['From'] = Header("后台服务器")
            msg['To'] = Header(to_addr) 
            msg['Subject'] = Header(self.subject_)
            server = smtplib.SMTP_SSL(smtp_server)
            server.connect(smtp_server,465)
            server.login(self.email,self.password)
            server.sendmail(self.email,to_addr,msg.as_string())
            server.quit()
            
            
            self.email_queue[self.index]["seccesstimes"]+=1
            self.next()
            self.total+=1
            return data["username"],rand_yzm
            
        
    def rand_yzm(self)->str:
        yzm=""
        for i in range(self.yzm_length):
            x=random.randint(0,9)
            yzm+=str(x)
        #print(yzm)
        return yzm

def show_title(version:str):
    '''
    打印标题\n
    :param version: 版本信息 3.0
    '''
    print("                                          Server records  Version:%s"%version)
    print("----------------------------------------------------------------------------------------------------------------------")
    print("number".ljust(9),"data".ljust(10),"time".ljust(10),"ip".ljust(21),"username".ljust(15),"requests".ljust(10),"status".ljust(25),"during".ljust(10))
    print("----------------------------------------------------------------------------------------------------------------------")

def show(start,msg,usrn,rqs):
    '''
    在终端显示信息
    '''
    global num,addr
    num+=1
    timenow=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    end=time.time()
    d=end-start
    print(str("%d"%num).ljust(10)+timenow.ljust(22)+addr[0].ljust(22)+usrn.ljust(16)+rqs.ljust(11)+msg.ljust(25),str("%4f"%d).ljust(10))
    #print(str("%d"%3).ljust(10)+"2021-06-09 20:06:39".ljust(22)+"111.42.148.107".ljust(19)+"1201110107".ljust(16)+"010".ljust(11)+"login".ljust(25),str("%4f"%0.002564).ljust(10))

def data2byte(data:object)->bytes:
    '''
    将python数据转化为二进制数据
    '''
    str_data=json.dumps(data)
    byte_data=str_data.encode("utf-8")
    return byte_data

def byte2data(bytess:bytes)->object:
    '''
    将二进制数据转化为python数据
    '''
    str_data=bytess.decode("utf-8")
    data=json.loads(str_data)
    return data

def count_num(address,format='/*.txt')->int:
    '''
    获取文件夹中 format类型的文件数量
    :param address:必选参数 文件夹地址
    :param format:默认参数 '/*.txt'
    '''
    path_file_number=glob.glob(address+format)
    total=len(path_file_number)
    return total

def save_config(dic,address):
    '''
    将变量变为json数据储存
    :param dic :带储存的变量
    :param address :储存的文件地址
    '''
    with open(address,'w',encoding='utf-8') as json_file:
        json.dump(dic,json_file,ensure_ascii=False)

def read_config(address):
    '''
    读取文件
    :param address :文件地址
    :return :python数据(object)
    '''
    with open(address,'r',encoding='utf-8') as json_file:
        dic=json.load(json_file)
    return dic

def read_q_a(q_address,a_address,num_q_a):
    '''
    返回两个字典 {1:"inasdiasndi aisd",2:"asdaswwwweee"}
    :param q_address:题目储存地址
    :param a_address:答案储存地址
    :num_q_a:数量
    '''
    a_dic={}
    q_dic={}
    for x in range(1,num_q_a+1):
        with open(q_address+'/q%d.txt'%x,'r',encoding="utf-8") as file1:
            txt1=""
            text=file1.readlines()
            for i in text:
                txt1=txt1+i
            q_dic[x]=txt1
        with open(a_address+'/a%d.txt'%x,'r',encoding="utf-8") as file1:
            txt2=""
            text=file1.readlines()
            for i in text:
                txt2=txt2+i
            a_dic[x]=txt2
            
    return q_dic,a_dic

def search(q:str)->list:
    '''
    搜题返回答案列表
    '''
    answer_dict=[]
    answer='none'
    if len(q)<10:
        for i in range(1,total+1):
            if q in q_dic[i]:
                answer=a_dic[i]
                answer_dict.append(answer)
                #break
    else:
        for i in range(1,total+1):
            if q[4:-4] in q_dic[i]:
                answer=a_dic[i]
                answer_dict.append(answer)
    
    return answer_dict

def analyse(bytess,addr,soc):
    '''
    相当于主函数
    '''
    global config
    global data_changed
    global user_dic
    global num
    global message
    global online_user_dic
    global upload_by_user_address
    global a_p_address
    start=time.time()
    '''
    分析指令
    data_dict={"Request":"030","question":"请问今天是星期几"}
    '''
    data=byte2data(bytess)
    key=data["Request"]

    #搜题
    if key=="030":
        question=data["question"]
        ans=search(question)
        quantity=len(ans)
        
        data_dict={"state":"031","quantity":quantity,"answers":ans}
        byte_data=data2byte(data_dict)
        #一次不能发送太多
        while sys.getsizeof(byte_data)>=60000:
            
            ans=ans[1:]
            data_dict={"state":"031","quantity":quantity,"answers":ans}
            byte_data=data2byte(data_dict)
        soc.sendto(byte_data,addr)
        
        if quantity>0:
            message="%d result(s)"%quantity
            
            user_dic[data["username"]][1]+=1
        else:
            message="not find"
        show(start,message,data["username"],key)
        
    
    #登录
    elif key=="010":
        exists=False#账户是否存在
        pswd_true=False
        usrn=data["username"]
        pswd=data["password"]
        
        return_dict={"state":"011","recived":0,"contributed":0,"news":"welcome to use the tool"}
        #检查账号密码是否正确
        if usrn in user_dic.keys():
            exists=True
            if user_dic[usrn][0]==pswd:
                pswd_true=True
        
        if (exists,pswd_true)==(True,True):
            return_dict["state"]="011"
            return_dict["recived"]=user_dic[usrn][1]
            return_dict["contributed"]=user_dic[usrn][2]
            #return_dict={"state":"011","recived":0,"contributed":0,"news":"welcome to use the tool"}
            
            #将用户添加到在线字典 记录时间戳
            online_user_dic[usrn]=[start]
            
            byte_data=data2byte(return_dict)
            soc.sendto(byte_data,addr)
            
            message="login"
            show(start,message,usrn,key)
            
        elif exists==False:
            #data_dict=("state":"012","reason":"密码错误")
            return_dict["state"]="012001"
            return_dict["reason"]="账号不存在"
            byte_data=data2byte(return_dict)
            soc.sendto(byte_data,addr)
            message="login failed error:%s"%return_dict["state"]
            show(start,message,"unknown",key)
            
        elif pswd_true==False:
            return_dict["state"]="012002"
            return_dict["reason"]="密码错误"
            byte_data=data2byte(return_dict)
            soc.sendto(byte_data,addr)
            message="error:%s"%(return_dict["state"])
            show(start,message,usrn,key)
            

    #注销
    elif key=="020":
        usrn=data["username"]
        del online_user_dic[usrn]
        show(start,"log off",usrn,key)
        
        return
    
    #上传题目
    elif key=="040":
        '''
        将用户上传的题目和答案储存起来,json文件
        '''
        #temp_dict={"author":"上传人","question":"今天星期几?","type":"C","answer":"星期六","time":"上传时的时间戳","description":"问题的描述"}
        temp_dict={}
        
        #将时间戳格式化为文本
        timeArray = time.localtime(int(start))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        temp_dict={"type":data["type"],"author":data["author"],"question":data["question"],"answer":data["answer"],"time":otherStyleTime,"description":data["description"]}
        temp_dict=data
        temp_dict["time"]=otherStyleTime
        #文件名字
        usrn=data["username"]
        user_dic[usrn][2]+=1#上传的题目+1
        contributed=user_dic[usrn][2]
        filename="%s-%d"%(usrn,contributed)
        
        #将文件储存到服务器
        save_config(temp_dict,upload_by_user_address+"/%s"%filename)
        
        #向客户端返回状态
        return_dict={"state":"041","message":"上传成功","contributed":contributed}
        byte_data=data2byte(return_dict)
        soc.sendto(byte_data,addr)
        
        #终端显示状态
        show(start,"uploaded",data["username"],key)
        
    
    #建立连接
    elif key=="000":
        show(start,"internet connected","unknown",key)
        #return_data1={"state":"001"}
        #byte_data1=data2byte(return_data1)
        #soc.sendto(byte_data1,addr)
        return_data1={"state":"094"}
        byte_data2=data2byte(return_data1)
        soc.sendto(byte_data2,addr)
        return

    #检查用户名是否存在
    elif key=="070":
        checkname=data["checkname"]
        if checkname in user_dic.keys():
            return_dict={"state":"071","checkname":checkname}
        else:
            return_dict={"state":"072","checkname":checkname}
        byte_data=data2byte(return_dict)
        soc.sendto(byte_data,addr)
        show(start,"check name:%s"%checkname,"unknown",key)

    #注册
    elif key=="080":
        checkname=data["checkname"]
        if checkname in user_dic.keys():
            #失败
            return_dict={"state":"082","checkname":checkname}
            show(start,"registration fail","unknown",key)
        else:
            #成功
            user_dic[checkname]=[data["password"],0,0]#创建用户
            return_dict={"state":"081","checkname":checkname}
            threading.Thread(target=save_config,args=(user_dic,a_p_address)).start()#开启线程储存档案
            show(start,"registration success",checkname,key)
        byte_data=data2byte(return_dict)
        soc.sendto(byte_data,addr)
    
    #发送验证码
    elif key=="090":
        yzm=email_sender.send_email(data["email"])
        if yzm :
            check_yzm.append_yzm(yzm[0],yzm[1])
            data_dict={"state":"091","email":data["email"],"verification_code":yzm[1]}
            soc.sendto(data2byte(data_dict),addr)
            show(start,"regist yzm :%s"%yzm[1],"unknown",key)
        else:
            show(start,"regist yzm :%s"%yzm[0],"unknown",key)

    else:
        '''
        未知指令
        '''
        message='unknown request'
        show(start,message,data["username"],key)
    
    #告知用户状态
    data_changed=True
    return_dict={"state":"100","down":user_dic[data["username"]][1],"up":user_dic[data["username"]][2],"can":9999}
    soc.sendto(data2byte(return_dict),addr)
    
def Save_config():
    global data_changed,last_time,user_dic
    while True:
        now=time.time()
        if now-last_time>10 and data_changed==True:
            save_config(user_dic,a_p_address)
            last_time=now
            data_changed=False
            show(now,"data saved","server 4.0","none")
        time.sleep(1)
        
if __name__=="__main__":
    #配置文件地址
    last_time=time.time()
    config_address=r"/root/sse/udp_server4_config.json"###配置储存路径
    message=""
    online_user_dic={}#在线的用户人数
    num=0#记录消息条数
    data_changed=False
    #读取配置文件
    config=read_config(config_address)
    print("email sender is ready")
    a_adr=config["a_address"]#答案存放地址
    q_adr=config["q_address"]#题目存放地址
    total=int(config["num_a_q"])#题库中答案（题目）的数量
    a_p_address=config["Account_and_password_address"]#注册用户信息
    t_a_p_address=config["temp_Account_and_password_address"]#
    upload_by_user_address=config["upload_by_user_address"]#用户上传的文件存放位置
    local_IP=config["local_IP"]#本地ip
    public_IP=config["public_IP"]#公网ip
    port=config["port"]#端口
    print("Configuration read successfully")
    #邮件系统
    email_sender=Emailsender(config["email"])
    check_yzm=Check_YZM()
    print("Email Sender Setup completed %d(s)"%(len(email_sender.email_queue)))
    

    
    q_dic,a_dic=read_q_a(q_adr,a_adr,total)
    print("Question bank completed")
    
    user_dic=read_config(a_p_address)#服务器注册的用户人数
    t_user_dic=read_config(t_a_p_address)#备用的，以防万一
    print("User information read")
    
    config_save_thread=threading.Thread(target=Save_config)
    config_save_thread.start()
    print("data save thread was opened")

    skt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定地址和端口
    skt.bind((local_IP,port))
    print("Internet connected")
    print("start reciving message")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("\n\n\n")
    show_title("4.0")

    
    while True:
        data,addr = skt.recvfrom(1024*200)
        job=threading.Thread(target=analyse,args=(data,addr,skt))
        job.start()
