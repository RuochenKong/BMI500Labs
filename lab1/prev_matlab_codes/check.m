A = [ 8,-1, 0, 0, 0, 0;
     -1, 2, 0, 0, 0, 0;
      0, 0, 4, 1, 0, 0;
      0, 0, 1,10, 1, 1;
      0, 0, 0, 1,12,-3;
      0, 0, 0, 1,-3,20];
  
x = [0;0;-25/6;-25/3;17/9;1];

disp(transpose(x)*A*x/(norm(x,2)^2))