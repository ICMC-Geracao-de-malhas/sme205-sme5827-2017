n = 5;
t = 0:pi/(2*n):pi/2
x = sin(t)
y = cos(t)

N = 100;
for i = 0:N
    t     = i/N;
    px(i+1) = Bezier(n,x,t);
    py(i+1) = Bezier(n,y,t);
end

plot(x,y)
hold
plot(px,py)


function [pt] = Bezier(n,p,t)
    pt = 0.0;
    for i = 0:n
        pt = pt + B(n,i,t)*p(i+1);
    end
    return
end


function [x] = B(n,i,t)
    c = 1.0;
    for j = 0:i-1
        c = c*(n-j)/(i-j);
    end
    x = c*t^i*(1.0-t)^(n-i);
    return
end

