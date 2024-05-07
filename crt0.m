long=512;  % 定义变量 long，并赋值为 512
filename='/home/pai4090/断层成像/1/data1.raw';  % 定义变量 filename，并赋值为文件路径
fid=fopen(filename,'r');  % 打开文件并返回文件标识符 fid
A=fread(fid,[long,long],'float32');  % 从文件 fid 中读取大小为 long x long 的浮点数矩阵到变量 A
figure;
subplot(1,2,1);
imshow(A,[]);
title('data1.raw []')  % 创建新的图形窗口，并在左侧子图中显示 A（使用默认的显示范围 []），并设置标题
subplot(1,2,2);
imshow(A,[0,1]);
title('data1.raw [0,1]')  % 在右侧子图中显示 A（使用显示范围 [0, 1]），并设置标题

figure;
subplot(2,1,1);
imshow(A,[]);
title('data1.raw []')  % 创建新的图形窗口，并在上方子图中显示 A（使用默认的显示范围 []），并设置标题
subplot(2,1,2);
imshow(A,[0,1]);
title('data1.raw [0,1]')  % 在下方子图中显示 A（使用显示范围 [0, 1]），并设置标题

filename='/home/pai4090/断层成像/1/data2.abc';  % 定义变量 filename，并赋值为文件路径
fid=fopen(filename,'rb');  % 以二进制模式打开文件并返回文件标识符 fid
A=fread(fid,[1,1],'int');  % 从文件 fid 中读取一个整数到变量 A
B=fread(fid,[1,1],'int');  % 从文件 fid 中读取一个整数到变量 B
C=fread(fid,[1,1],'char');  % 从文件 fid 中读取一个字符到变量 C
switch C
    case 0
        format='void';
    case 1
        format='bit';
    case 2
        format='char';
    case 3
        format='unsigned char';
    case 4
        format='short';
    case 5
        format='unsigned short';
    case 6
        format='int';
    case 7
        format='unsigned int';
    case 8
        format='long';
    case 9
        format='unsigned long';
    case 10
        format='float';
    case 11
        format='double';
end
fseek(fid,128,'bof');  % 从文件开头偏移 128 个字节
D=fread(fid,[B,A],format);  % 从文件 fid 中按照指定的格式读取大小为 B x A 的数据到变量 D
figure;imshow(D,[]);title('data2.abc')  % 创建新的图形窗口，并显示 D（使用默认的显示范围 []），并设置标题
figure;imagesc(D);title('data2.abc伪彩')  % 创建新的图形窗口，并使用伪彩色显示 D，并设置标题