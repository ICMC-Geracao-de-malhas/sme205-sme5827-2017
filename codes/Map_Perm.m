function [F] = Map_Perm(n,f)
    for i = 1:n
        F(i) = 0;
    end
    for i = 1:n
        if F(f(i)) == 0
            F(f(i)) = i;
        else
            for j = n:-1:f(i)+1
                F(j) = F(j-1);
            end
            F(f(i)) = i;
        end
    end
    return
end

