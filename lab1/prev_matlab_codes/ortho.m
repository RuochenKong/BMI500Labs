function [Q,V] = ortho(A,tol)
    B = A;
    [n,~] = size(A);
    V = zeros(n,1);
    Q0 = GS(B);
    
    for k = 1:100
        B = A*Q0;
        Q = GS(B);

        stop = 1;
        for i = 1:n
            q = Q(:,i);
            q0 = Q0(:,i);
            check = norm(q-q0,2);
            check = min(2-check,check);
            if check >= tol
                stop = 0;
                break
            end
        end
        
        if stop == 1
            fprintf('k = %d iterations\n\n',k);
            break
        end
        
        Q0 = Q;
    end
    
   for i = 1:n
       q = Q(:,i);
       V(i) = transpose(q) * A * q; 
   end 
   