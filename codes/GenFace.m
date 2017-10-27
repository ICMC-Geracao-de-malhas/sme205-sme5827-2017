function [Face m] = GenFace(n,k) 
   Face = []; 
   for i = 1:n-k
      Division(i) = 2*n;
   end
   [Base]  = InitGrid(n-k, Division);
   m = 0;
   for g = 0:Base(n-k+1)-1
      [F]      = GridCoords(n-k,g,Base);
      [isface] = IsFace(n,n-k,F);
      if isface == 1
         Face = [Face; F];
         m    = m+1;
      end
   end
   return;
end


function [isface] = IsFace(dim,n,F)
   for i = 1:n-1
      for j = i+1:n
         if F(i) >= F(j)
            isface = 0;
            return;        
         end
         if mod(F(i),dim) == mod(F(j),dim)
            isface = 0;
            return;        
         end
      end
   end 
   isface = 1;
   return;
end
