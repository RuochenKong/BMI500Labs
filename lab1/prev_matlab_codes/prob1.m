function prob1

fprintf('-------------part b)-------------\n')
A = [0,1,0,0,1;
     1,0,1,1,1;
     0,1,0,0,0;
     0,1,0,0,1;
     1,1,0,1,0];
 
[n,~] = size(A);

[Q,V] = ortho(A,10^-8);

for i = 1:n
    fprintf('e-value %d: %2.8e\n',i,V(i))
end

fprintf('\nFinal Q(e-vectors):\n')
disp(Q);

s1 = sum(V);
s2 = transpose(V)*V;

fprintf('\nSum of E-valuse        : %2.8e\n',s1);
fprintf('Sum of squared E-valuse: %2.8e\n',s2);



fprintf('\n-------------part c)-------------\n')

 A = [0,1,1,1,1;
      1,0,0,0,0;
      1,0,0,1,0;
      1,0,1,0,1;
      1,0,0,1,0];
 
 
 
[n,~] = size(A);

[Q,V] = ortho(A,10^-8);

for i = 1:n
    fprintf('e-value %d: %2.8e\n',i,V(i))
end

fprintf('\nFinal Q(e-vectors):\n')
disp(Q);

s1 = sum(V);
s2 = transpose(V)*V;

fprintf('\nSum of E-valuse        : %2.8e\n',s1);
fprintf('Sum of squared E-valuse: %2.8e\n',s2);

