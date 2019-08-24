import random                                                                           #以随机数模拟任意分两

from tkinter import *
window = Tk()                                                                             #创建窗口,显示本卦、之卦卦象
window.title('本卦⟹之卦')
gx = Canvas(window, width = 450, height = 450, bg = 'white')  
gx.pack()
def yang_img(x, n, clr):                                                               #绘制阳爻（自下向上）
   gx.create_line(x, (350 - n * 50), (x + 150), (350 - n * 50), width = 5, fill = clr)
def yin_img(x, n, clr):                                                                   #绘制阴爻
   gx.create_line(x, (350 - n * 50), (x + 50), (350 - n * 50), width = 5, fill = clr)
   gx.create_line((x + 100), (350 - n * 50), (x + 150), (350 - n * 50), width=5, fill = clr)

yao_name = ['初', '二', '三', '四', '五', '上']                                     #爻序号   
const = 1                                                                                    #标记变爻
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

   #过揲策数除以四得筮数，据此绘制爻象, 本卦变爻以红色，变得之卦爻以蓝色表示
   print('%s  爻: 筮数%d/4=%d, ' % (yao_name[k], s, (s / 4)), end = '')
   if s / 4 == 9:                              
      print('老阳☐')
      yang_img(50, k, clr = 'red')
      yin_img(250, k, clr = 'blue')
      const = 0
   elif s / 4 == 8:
      print('少阴--')
      yin_img(50, k, clr = 'black')
      yin_img(250, k, clr = 'black')
   elif s / 4 == 7:
      print('少阳―')
      yang_img(50, k, clr = 'black')
      yang_img(250, k, clr = 'black')
   else:
      print('老阴×')
      yin_img(50, k, clr = 'red')
      yang_img(250, k, clr = 'blue')
      const = 0
   print()

#六爻皆不变，只显示本卦卦象
if const == 1:
   gx.addtag_all('gua')
   gx.move('gua', 100, 0)
   gx.create_rectangle(300, 0, 455, 450, outline='white', fill='white')

window.mainloop()
