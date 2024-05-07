function P = ForwardProjection1(theta,N,N_d)

point = [ 1,     0.005,      0.005,          0.5,       0,           0,];
   theta_num = length(theta);
   P = zeros(N_d,theta_num);
   rho = point(:,1).';
   ae = 0.5*N*point(:,2).';
   be = 0.5*N*point(:,3).';
   xe = 0.5*N*point(:,4).';
   ye = 0.5*N*point(:,5).';
   alpha = point(:,6).';
   alpha = alpha*pi/180;
   theta = theta*pi/180;
   TT = -(N_d-1)/2:(N_d-1)/2;
   for k1 = 1: theta_num
       P_theta = zeros(1,N_d);
       for k2 = 1:max(size(xe))
           a=(ae(k2)*cos(theta(k1)-alpha(k2)))^2+(be(k2)*sin(theta(k1)-alpha(k2)))^2;
           temp = a-(TT-xe(k2)*cos(theta(k1))-ye(k2)*sin(theta(k1))).^2;
           ind = temp >0;
       P_theta(ind)=P_theta(ind)+rho(k2)*(2*ae(k2)*be(k2)*sqrt(temp(ind)))./a;
       end
       P(: , k1) = P_theta.';
   end
end