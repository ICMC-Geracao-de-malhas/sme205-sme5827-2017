function [P] = Enumerate_Arranjo(n,k)
    P = [];
    for i = 1:k
        Division(i) = n-k+i;
    end
    [Base] = InitGrid(k,Division);
    for j = 0:Base(k+1)-1
        [f] = GridCoords(k,j,Base);
        for i = 1:k
            f(i) = f(i)+1;
        end
        P   = [P; f];
    end
    return
end