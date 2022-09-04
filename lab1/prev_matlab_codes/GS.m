function [Q,R] = GS(A)

    [n,~] = size(A);
    Q = zeros(n,n); 
    
    for i = 1:n
        c = A(:,i);
        for j = 1:i-1
            e = Q(:,j);
            if norm(e - zeros(n,1),2) >= 10^-8
                u = transpose(c)*e;
                d = transpose(e)*e;
                c = c - u/d*e;
            end
        end
        if norm(c - zeros(n,1),2) >= 10^-8
            c = c/norm(c,2);
        end
        Q(:,i) = c;
    end
        
    R = transpose(Q)*A;
    
 
    