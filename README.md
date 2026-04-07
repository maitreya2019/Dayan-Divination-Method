# 大衍筮法演示程序

这是一个展示《周易》大衍筮法数学原理的python脚本，核心算法是用高斯正态分布生成随机数来模拟筮法“四营”中的“分两”，这一随机过程是产生不同筮数及其对应卦象的关键。此程序还配有按照邵雍先天卦序的反序排列的六十四卦卦爻辞文档，可根据先天数理的二进制法则将卦象转换为相应的序数，达到依据卦象、变爻查找相应卦爻辞来占卜的目的。

运行python脚本需安装tk模块，也可直接下载exe打包文件双击运行，文本库yi.txt需与脚本或exe放于同一文件夹内。程序自动按大衍筮法的“四营”步骤（卦一、分两、过揲、归奇）生成筮数，并显示本卦、之卦卦象，及占卜所需卦爻辞，无需手动输入。

This is a Python script that demonstrates the mathematical principles of the Dayan divination method from the I Ching (Book of Changes). The core algorithm uses a Gaussian distribution to generate random numbers, simulating the "dividing into two" step within the "Four Operations" of the divination process. This random process is key to producing different divination numbers and their corresponding hexagrams. The program also includes a document containing the hexagram and line texts for the sixty-four hexagrams, arranged in the reverse order of Shao Yong's Xiantian hexagram sequence. Based on the binary rules of Xiantian numerological principles, each hexagram can be converted into a corresponding ordinal number, allowing the program to look up the relevant hexagram and line texts for divination based on the resulting hexagram and changing lines.

To run the Python script, the tkinter module must be installed. Alternatively, you can directly download the packaged executable (.exe) file and double-click to run it. The text database file yi.txt must be placed in the same folder as the script or the .exe file. The program automatically generates divination numbers following the four steps of the Dayan method (designating one, dividing into two, counting by fours, and setting aside the remainder), and displays the resulting primary hexagram (ben gua), the derived hexagram (zhi gua), as well as the hexagram and line texts needed for divination — all without any manual input.
