function [Grid] = GridCoords(n,i,Base) 
   copy = i;
   for j = n:-1:2
      aux = mod(copy,Base(j));
      Grid(j) = (copy-aux)/Base(j);
      copy = aux;
   end
   Grid(1) = copy;
   return
end  