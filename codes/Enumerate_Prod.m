function [P] = Enumerate_Prod(n,Division)
    P = [];
    [Base] = InitGrid(n,Division);
    for k = 0:Base(n+1)-1
        [f] = GridCoords(n,k,Base);
        P   = [P; f];
    end
    return
end