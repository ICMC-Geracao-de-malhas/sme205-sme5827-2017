function [P] = Enumerate_Perm(n)
    P = [];
    for i = 1:n
        Division(i) = i;
    end
    [Base] = InitGrid(n,Division);
    for k = 0:Base(n+1)-1
        [f] = GridCoords(n,k,Base);
        f = f+1;
        [F] = Map_Perm(n,f);
        P   = [P; F];
    end
    return
end
