function V = QM(A,tol)
    [n,~] = size(A);
    V = zeros(n,1);
    V1 = V;
    C = A;
    
    for i = 1:n
        V(i) = C(i,i);
    end
    
    for k = 1:100
        
        [Q,R] = GS(C);
        C = R*Q;
        
        disp(C);
        for i = 1:n
            V1(i) = C(i,i);
        end
        
        if norm(V-V1,2) < tol
            fprintf('k = %d iterations\n\n',k);
            break
        end
        
    end