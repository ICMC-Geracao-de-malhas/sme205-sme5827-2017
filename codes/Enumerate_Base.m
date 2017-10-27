function [P] = Enumerate_Base(n,k)
    P = [];
    for i = 1:k
        Division(i) = n;
    end
    [Base] = InitGrid(k,Division);
    for j = 0:Base(k+1)-1
        [f] = GridCoords(k,j,Base);
        %f = f+1;
        [lex] = Lexico(k,f);
        if lex == 1
            P   = [P; f];
        end
    end
    return
end


function [lex] = Lexico(k,f)
    for i = 1:k-1
        if f(i) > f(i+1)
            lex = 0;
            return
        end
    end
    lex = 1;
    return
end
