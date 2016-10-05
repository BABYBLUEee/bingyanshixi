function theta = Itertheta(X,y,theta,alpha)
  m=length(y);
theta = theta - alpha*(1/m)*(X')*(X*theta-y);