long = 512;
filename = '/home/pai4090/断层成像/1/data1.raw';
fid = fopen(filename, 'rb');
A = fread(fid, [long, long], 'float32');
fclose(fid);

% 第一种窗位显示
figure;
subplot(1, 2, 1);
imshow(A, []);
title('data1.raw []');

% 第二种窗位显示
subplot(1, 2, 2);
imshow(A, [min(A(:)), max(A(:))]);
title('data1.raw [min, max]');

figure;
subplot(2,1,1);
imshow(A,[0,0.5]);
title('data1.raw [0,0.5]')  

% 创建新的图形窗口，并在上方子图中显示 A（使用默认的显示范围 []），并设置标题
subplot(2,1,2);
imshow(A,[0.5,0.8]);
title('data1.raw [0.5,0.8]') 



filename = '/home/pai4090/断层成像/1/data2.abc';
fid = fopen(filename, 'rb');
width = fread(fid, [1, 1], 'int32');  % 读取图像宽度
height = fread(fid, [1, 1], 'int32');  % 读取图像高度
dataType = fread(fid, [1, 1], 'char');  % 读取数据类型标识字节

switch dataType
    case 0
        format = 'void';
    case 1
        format = 'bit';
    case 2
        format = 'char';
    case 3
        format = 'uint8';
    case 4
        format = 'int16';
    case 5
        format = 'uint16';
    case 6
        format = 'int32';
    case 7
        format = 'uint32';
    case 8
        format = 'int64';
    case 9
        format = 'uint64';
    case 10
        format = 'single';
    case 11
        format = 'double';
end

fseek(fid, 128, 'bof');  % 跳过文件头部分
D = fread(fid, [height,width], format);  % 读取图像数据
fclose(fid);

% 显示图像
figure;
subplot(1, 2, 1);
imshow(D, []);
title('data2.abc');

subplot(1, 2, 2);
imagesc(D);
title('data2.abc 伪彩色');


figure;
% 使用不同的伪彩图
imagesc(D);
colormap jet;  % 使用 "jet" 伪彩图方案
colorbar;  % 显示颜色条
title('data2.abc 伪彩色 (jet)');

% 使用不同的伪彩图
figure;
imagesc(D);
colormap hot;  % 使用 "hot" 伪彩图方案
colorbar;  % 显示颜色条
title('data2.abc 伪彩色 (hot)');