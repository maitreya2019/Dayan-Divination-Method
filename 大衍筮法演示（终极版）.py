#!/usr/bin/python
#-*- coding: utf-8 -*-
#本程序以计算机算法演示大衍筮法占卜过程
#读取按先天二进制卦序排列的周易经文文档为64*8的二维数组，1行为一卦，每行8列内容依次为：0卦名、1卦辞、(2-7)六爻辞、8用辞(除乾坤外为空)
yi_xiantian = open('yi.txt', encoding='utf-8')
yi_line = yi_xiantian.readlines()                                                      #逐行读取文本为数组行
yi_txt = []
for yi_col in yi_line:                                                                       #每行内容以'|'为标志分隔成数组列
   yi_col = yi_col.split('|')
   yi_txt.append(yi_col)
def print_gua(n):                                                                            #输出第n卦卦辞(坤0-乾63)
   print('《%s》：%s' % (yi_txt[n][0], yi_txt[n][1]))
def print_yao(n, m):                                                                      #输出第n卦第m爻爻辞(初0-上5，6为乾坤用辞)
   print('《%s》%s' % (yi_txt[n][0], yi_txt[n][m + 2]))

from tkinter import *
window = Tk()                                                                             #创建窗口，显示本卦、之卦卦象
window.title('大衍筮法')
gx = Canvas(window, width = 450, height = 450, bg = 'white')  
gx.pack()
def yang_img(x, n, clr):                                                               #绘制阳爻（自下向上，等间隔）
   gx.create_line(x, (350 - n * 50), (x + 150), (350 - n * 50), width = 5, fill = clr)
def yin_img(x, n, clr):                                                                   #绘制阴爻
   gx.create_line(x, (350 - n * 50), (x + 50), (350 - n * 50), width = 5, fill = clr)
   gx.create_line((x + 100), (350 - n * 50), (x + 150), (350 - n * 50), width = 5, fill = clr)
def gua_name(n1, n2):                                                                 #显示卦名
   gx.create_text(125, 400, text = yi_txt[n1][0], font = ('新宋体', 20))
   gx.create_text(225, 400, text = '之', font = ('楷体', 20))
   gx.create_text(325, 400, text = yi_txt[n2][0], font = ('新宋体', 20))

import random                                                                           #以随机数模拟任意分两
gua_ben = gua_zhi = 0                                                               #本卦之卦序数
yao_name = ['初', '二', '三', '四', '五', '上']                                     #爻序号
yao_trans = []                                                                             #以动态数组记录变爻
j_list = [4, 1, 2, 3]                                                                        #归奇数组(余0转为余4)
for k in range(6):                                                                         #六爻成一卦
   s = 49                                                                                       #大衍之数五十，其用四十有九
   for i in range(3):                                                                       #四营为一变，三变生一爻
      l = round(random.gauss(s / 2, (s - 10) / 6))                          #分两，左手策数(正态分布取随机数)
      r = s - l                                                                                  #右手策数
      l1 = l - 1                                                                                #挂一,从左手策数减一
      j = j_list[(l1 % 4)] + j_list[(r % 4)] + 1                                     #揲之以四，左右手策数除四余数加挂一数总和为归奇数
      print('第%d变: 策数%d, 左手%d, 右手%d, 挂扐%d' % ((i +1), s, l, r, j))
      s -= j                                                                                     #归奇于扐，除去归奇数的过揲数为下一变策数
   #过揲策数除以四得筮数，据此绘制爻象, 本卦常爻为黑色，变爻为红色，变得之卦爻为蓝色
   print('%s 爻: 筮数%d/4=%d, ' % (yao_name[k], s, (s / 4)), end = '')
   if (s / 4) % 2 != 0:                                                                   #筮数为奇，本卦阳爻
      gua_ben += 2 ** (5 - k)                                                      #爻象转换为本卦、之卦先天二进制序数，阳爻为1，阴爻为0
      if s / 4 == 9:                                                                         #筮数九，老阳
         print('老阳☐')
         yang_img(50, k, clr = 'red')
         yin_img(250, k, clr = 'blue')
         yao_trans.append(k)
      else:                                                                                     #筮数七，少阳
         print('少阳―')
         yang_img(50, k, clr = 'black')
         yang_img(250, k, clr = 'black')
         gua_zhi += 2 ** (5 - k)
   else:                                                                                        #筮数为偶，本卦阴爻
      if s / 4 == 6:                                                                         #筮数六，老阴
         print('老阴×')
         yin_img(50, k, clr = 'red')
         yang_img(250, k, clr = 'blue')
         gua_zhi += 2 ** (5 - k)
         yao_trans.append(k)
      else:                                                                                     #筮数八，少阴
         print('少阴--')
         yin_img(50, k, clr = 'black')
         yin_img(250, k, clr = 'black')
   print()
gua_name(gua_ben, gua_zhi)                                               #显示本卦之卦卦名

#变爻总数为数组长度，以此决定占法(依据朱子《易学启蒙·考变占》)
trans_sum = len(yao_trans)                                                       
if trans_sum == 0:                                                                     #无变爻
   gx.addtag_all('gua')                                                                #只显示本卦卦象
   gx.move('gua', 100, 0)
   gx.create_rectangle(300, 0, 455, 450, outline='white', fill='white')
   print('无变爻, 以本卦卦辞占：')
   print_gua(gua_ben)                                                              #输出本卦卦辞
else:                                                                                           #有变爻
   print('%d爻变, ' % (trans_sum), end = '')                                 #输出变爻数
   if trans_sum < 3:                                                                      #一或二爻变
      print('以本卦变爻占：')
      for k in yao_trans:                                                             #输出本卦变爻爻辞
         print_yao(gua_ben, k)
   elif trans_sum == 3:                                                                #三爻变
      print('以本卦、之卦卦辞占：')
      print_gua(gua_ben)                                                           #输出本卦之卦卦辞
      print_gua(gua_zhi)
   elif trans_sum > 3 and trans_sum  < 6:                                  #四或五爻变
      print('以之卦不变爻占：')
      yao_const_set = set([0, 1, 2, 3, 4, 5]) - set(yao_trans)          #以集合差集算法求得不变爻序数
      yao_const = list(yao_const_set)
      for k in yao_const:                                                             #输出之卦不变之爻爻辞
         print_yao(gua_zhi, k)
   else:                                                                                        #六爻皆变
      if gua_ben != 0 and  gua_ben != 63:                                #非乾坤互变的情况
         print('以之卦卦辞占：')
         print_gua(gua_zhi)                                                        #输出之卦卦辞
      else:                                                                                     #乾之坤或坤之乾
         print('《%s》之《%s》：' % (yi_txt[gua_ben][0], yi_txt[gua_zhi][0]))
         print_yao(gua_ben, 6)                                                     #输出乾用九或坤用六

window.mainloop()
