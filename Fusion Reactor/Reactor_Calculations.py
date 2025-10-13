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

#This is Grad-Shafranov magnetic flux claculation
def get_input_with_range(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(f"{prompt} (range {min_val} to {max_val}): "))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value out of range. Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

mu0_range = (0.0000001, 0.0000005)           # Magnetic permeability (T·m/A)
r_range = (0.1, 5.0)               # Radial coordinate in meters
dp_dpsi_range = (-1e5, 1e5)        # Pressure gradient in Pascal per Weber (or appropriate units)
dF2_dpsi_range = (-10, 10)         # Gradient of squared toroidal field (T^2/unit psi)

# Collects inputs from user
mu0 = get_input_with_range("Enter magnetic permeability mu0", *mu0_range)
r = get_input_with_range("Enter radial coordinate r", *r_range)
dp_dpsi = get_input_with_range("Enter dp/dpsi (pressure gradient w.r.t psi)", *dp_dpsi_range)
dF2_dpsi = get_input_with_range("Enter dF^2/dpsi (gradient of squared toroidal field)", *dF2_dpsi_range)

print(f"\nInputs accepted:")
print(f"mu0 = {mu0}")
print(f"r = {r}")
print(f"dp/dpsi = {dp_dpsi}")
print(f"dF^2/dpsi = {dF2_dpsi}")

print("Toroidal Flux Gradient:",(mu0*r*r*dp_dpsi)-(dF2_dpsi))

#This is the calculation of the energy for particle transport
Gamma_range = (1e24, 1e27) #Particle flux in m^-2*s^-1
S_range = (1e14, 1e19) #Source term resulting in diffusion and convection

#Gets inputs from the user
Gamma = get_input_with_range("Enter the flux of the particle in the reactor:",*Gamma_range)
S = get_input_with_range("Enter the flux from source term:",*S_range)

print(f"\ninputs accepted:")
print(f"Gamma = {Gamma}")
print(f"S = {S}")
print("Total particle density:",(-Gamma)+(S)) #in m^-3

print("Now let's calculate the diffusive flux as it is practically more expensive for manual testing.")

#Calculating diffusive flux
v_n_range = (10, 250) #convective flux in mu_m/min

v_n = get_input_with_range("Enter the convective flux value in micrometers/min:",*v_n_range)

print(f"Total convective flux = {v_n}")

print("Diffusive flux:",(Gamma)-(v_n))




