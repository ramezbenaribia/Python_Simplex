[rownum,colnum]=size(matrice) ;

Zj= zeros(1,colnum) ;

coeff_v_b= zeros(1,rownum);

result = Cj - Zj(1:end-1) ;


while any(result > 0 )
    
    
    % chercher la position de la variable entrante
    x= find(result==max(result));
    
     % chercher les variables sortantes 
     Vs = matrice(:,end) ./ matrice(:,x);
     for i=1 :rownum 
        if (Vs(i) < 0)
            Vs(i) = Vs(i) * (-1) / 0 ;
        end
     end
     
     % Chercher la position de la variable sortante
     y= find(Vs==min(Vs));
    
     disp('les variabels sortantes : ');
     disp(Vs);
    disp('position de la variable entrante :');
    disp(x);
    disp('position de la variable sortante : ');
    disp(y) ;
    disp('pivot :'); 
    disp(matrice(y , x)) ;
    
    %changer la variable sortante par la variable entrante
    coeff_v_b(y) = Cj(x) ;
    
    %Changer la matrice et etablir la méthode de pivot de  Gauss
    matrice(y,:) = matrice(y,:) ./ matrice(y,x) ;
    
    for i=1 :rownum
        if (i ~= y) 
            matrice(i,:) = matrice(i,:) - matrice(i,x) .* matrice(y,:) ;
            if (matrice(i,end)<0)
                matrice(i,:) = matrice(i,:) *(-1) ;
            end
        end
    end
    
    % Changer Zj
    for i=1 :colnum
        Zj(i) = coeff_v_b *matrice(:,i) ;
    end
    
    disp('Cj : ');
    disp(Cj);
   
    disp('matrice : ');
    disp(matrice);
    
    
     disp('coeff est  : ');
    disp(coeff_v_b);
    
    
    disp('Zj : ');
    disp(Zj);
    result = Cj - Zj(1:end-1) ;
    
    disp('resultat :');
    disp(result);
    
end


disp('la solution optimale est : ') ;



for i=1 :(length(Cj)-rownum)
    xi= find(coeff_v_b == Cj(i)) ;
    sprintf('la solution x%d = %d',i , matrice(xi,end)) 
end

sprintf('Z= %d',Zj(end))


