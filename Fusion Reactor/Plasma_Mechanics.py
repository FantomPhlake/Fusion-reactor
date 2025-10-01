import plasmapy

#Now we are starting with the plasma mechanics of the fusion reactor

print("Plasma Mechanics\n")

# Grad-Shafranov equation
print("Grad-Shafranov equation:")
print("  Δ*ψ = - μ₀ r² dp/dψ - (1/2) dF²/dψ")
print("  where:")
print("    ψ   = Poloidal magnetic flux")
print("    μ₀  = Permeability of free space")
print("    r   = Minor radius")
print("    p   = Plasma pressure")
print("    F   = Poloidal current function")
#Further explaining Grad-Shafranov equation
print("the Grad-Shafranov equation gives the toroidal magnetic flux of the tungsten magnets that are used in the fusion reactor.")

# Particle and energy transport equation
print("Particle and energy transport equation:")
print("  ∂n/∂t = - ∇·Γ + S")
print("  Γ = -D ∇n + v n   (diffusive + convective flux)")
print("  where:")
print("    n   = Particle density")
print("    Γ   = Particle flux")
print("    S   = Source term")
print("    D   = Diffusion coefficient")
print("    v   = Convective velocity")
#Further explaining particle and energy transport equation
print("This formula is based on the gyrokinetic plasma kinetic equation. in simple terms this equation can be used to calculate the flux and temperature gradient in fusion reators." \
"This equation can be further used to derive the non leakage probability as well. ")

# Fusion power density formula
print("Fusion power density formula:")
print("  P_f = n_D n_T <σv> E_f")
print("  where:")
print("    P_f   = Fusion power density")
print("    n_D   = Deuterium density")
print("    n_T   = Tritium density")
print("    <σv>  = Fusion reactivity")
print("    E_f   = Energy released per fusion reaction")
#Further explaining fusion powe density formula
print("The fusion power density formula can be used to calculate the total power output due to the density and number of colissions happening inside the plasma flux zone." \
"The fusion reactivity also varies with increase in temperature (directly proportional) and also for deuterium-deuterium fusion the n values change to (n^2)/2")