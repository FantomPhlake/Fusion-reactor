from sympy import symbols, Function, diff

# Defining necessary symbols
psi, mu0, r, p, F = symbols('psi mu0 r p F')
n, t, Gamma, S, D, v = symbols('n t Gamma S D v')
n_D, n_T, sigma_v, E_f = symbols('n_D n_T sigma_v E_f')

# Grad-Shafranov equation (symbolic form)
grad_shafranov = diff(psi, r, r) + diff(psi, r)/r == -mu0*r**2*diff(p, psi) - (1/2)*diff(F**2, psi)

# Particle and energy transport equation
particle_transport = diff(n, t) == -diff(Gamma, r) + S
flux = Gamma == -D*diff(n, r) + v*n

# Fusion power density formula
fusion_power = symbols('P_f') == n_D*n_T*sigma_v*E_f