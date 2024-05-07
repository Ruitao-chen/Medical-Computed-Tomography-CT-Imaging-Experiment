function P = ForwardProjection(theta,N,N_d)
shep = [1,       0.69,      0.92,         0,         0,            0,      
    -0.8,      0.6624,    0.8740,         0,   -0.0184,           0,         
    -0.2,      0.1100,    0.3100,      0.22,          0,        -18,   
   -0.2,      0.1600,    0.4100,      -0.22,      0,            18,        
     0.1,       0.2100,     0.2500,          0,      0.35,         0,       
    0.1,       0.0460,     0.0460,          0,       0.1,         0,        
     0.1,       0.0460,     0.0460,          0,       0.1,         0,       
     0.1,       0.0460,     0.0230,      -0.08,    -0.605,         0,       
   0.1,       0.0230,     0.0230,          0,     -0.606,         0,       
  0.1,       0.0230,     0.0460,       0.06,     -0.605,         0,];
 
   theta_num = length(theta);
   P = zeros(N_d,theta_num);
   rho = shep(:,1).';
   ae = 0.5*N*shep(:,2).';
   be = 0.5*N*shep(:,3).';
   xe = 0.5*N*shep(:,4).';
   ye = 0.5*N*shep(:,5).';
   alpha = shep(:,6).';
   alpha = alpha*pi/180;
   theta = theta*pi/180;
   TT = -(N_d-1)/2:(N_d-1)/2;
   for k1 = 1: theta_num
       P_theta = zeros(1,N_d);
       for k2 = 1:max(size(xe))
           a = (ae(k2)*cos(theta(k1)-alpha(k2)))^2+(be(k2)*sin(theta(k1)-alpha(k2)))^2;
           temp = a-(TT-xe(k2)*cos(theta(k1))-ye(k2)*sin(theta(k1))).^2;
           ind = temp >0;
           P_theta(ind) = P_theta(ind) + rho(k2)*(2*ae(k2)*be(k2)*sqrt(temp(ind)))./a;
       end
       P(: , k1) = P_theta.';
   end
end