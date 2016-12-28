# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:42:16 2016

@author: crisov
"""
import string
import zipfile

#构造任意进制数,模拟全排列
def lunzhuan(maxnum, list_dict, param):
    pswd="";
    while param <> 0 and len(list_dict) <> 0:
        pswd=list_dict[param%len(list_dict)]+pswd;
        param=param/len(list_dict);
    return pswd;

#源zip路径和目标zip路径
sourceFile="D://1.zip";
destFile="D://1";
#密码最多几位：
MaxNUM = 4;
#在这里写好zip路径
zFile=zipfile.ZipFile(sourceFile);
#输入字典
list_dictHack=[];
list_dictHack.append(raw_input("Please enter possible password:"));
try:
    while list_dictHack[len(list_dictHack)-1] <> "":
        list_dictHack.append(raw_input("Please enter possible password:"));
except:
    print "Something went wrong with the dict, no dict created";
    list_dictHack=[];
finally:
    print "Dict section has done!";

list_dictHack.sort();
list_dictHack.remove("");
#选择模式
int_choice=raw_input("Please choose the mode you want to use:\n1. easy mode\n2. digit number mode\
                     \n3. violent mode\n");


if int_choice == '1':
    pass;
elif int_choice == '2':
    list_dictHack+=list(string.digits);
    pass;
elif int_choice == '3':
    list_dictHack=list(string.digits+string.ascii_letters);
    pass;
    

for i in range(0,len(list_dictHack)**MaxNUM):
    pw=lunzhuan(MaxNUM,list_dictHack,i);
    print pw;
    try:
        zFile.extractall(path=destFile,pwd=pw);
        print "Hack succeed!";
        print "The hacking number is: "+pw;
        break;
    except:
        if i==len(list_dictHack)**MaxNUM-1:
            print "hack failed";
        pass;
        
zFile.close();
print("Everything has done");