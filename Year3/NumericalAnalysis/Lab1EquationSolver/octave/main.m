[xf, fval] = fsolve(@f, [0]);
[xg, gval] = fsolve(@g, [0]);

fprintf('Non linear solvers\n')
fprintf('f function root: %.11f\n', xf)
fprintf('f(root) = %f\n', fval)
fprintf('g function root: %.11f\n', xg)
fprintf('g(root) = %f\n', gval)

coeff = [2, 48, -67, -722, -141, 988, -288, -14];
res = roots(coeff);

fprintf('Algebraic equation solver\n')
coeff
res