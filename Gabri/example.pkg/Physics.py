#Created by me, Gabriele Gatti, hope you like it
def main():
    print("Physics.py is working")

#Earth Gravity constant in m/(s^2)
GRAVITY = 9.81

#Light speed on void in meters per sec.
LIGHT = 299792452

#Distance Moon-Earth in meters
ME = 3.84*10**9

#Speed of sound on air in meters per sec.
SOUND = 340

#Astronomical Unit in meters
AU = 1.49*10**11

#Parsec in meters
PARSEC = 3.08*10**16

#Earth Mass in kilograms
EARTH_MASS = 5.98*10**24

#Sun Mass in kilograms
SUN_MASS = 1.98*10**30

#Moon Mass in kilograms
MOON_MASS = 7.342*10**22

#Earth Radius in meters
EARTH_RADIUS = 6378*10**3

#Sun Radius in meters
SUN_RADIUS = 69634*10**4

#Moon Radius in meters
MOON_RADIUS = 1731*10**3

#Universal Gravity Constant in [(Newton * meters^2) / (kilograms^2)]
G = 6.67*10**(-11)

#Light year in meters
LIGHT_YEAR = 9.46*10**15

#Proton Mass in kilograms
PROTON_MASS = 1.672*10**(-27)

#Electron Mass in kilograms
ELECTRON_MASS = 9.109*10**(-31)

#Neutron Mass in kilograms
NEUTRON_MASS = 1.674*10**(-27)

#Absolute Zero in Celsius Deg
ABS_ZERO = -273

#Avogadro Constant (with grams) in molecules per mole
AVOGADRO = 6.022*10**23

#Ideal Gasses Constant in [(Joule) / (Mole × Kelvin Deg.)]
R = 8.316

#Thermal Expansion Coefficient 1/273 <=> 0.036
THERM_EXPANSCOEFF = 1/273

#Planck Constant in [(meters^2 × kilograms) / (seconds)]
PLANCK = 6.626*10**(-34)

#Stefan-Boltzmann Constant in [Watt/(meters^2 * Kelvin^4)]
STEFBOLTZ = 5.67*10**(-8)

#Coulomb constant in [Newton × (meters^2) / (Coulomb^2)]
COULOMB = 8.988*10**9

#Dielectric constant on void in [Faraday/meters]
DIELECTRIC = 8.854*10**(-12)

#Electron Volt in Joule
EV = 1.602*10**(-19)

#Silver resistivity
SILVER_RESISTIVITY = 1.6*10**(-8)

#Copper resistivity
COPPER_RESISTIVITY = 1.7*10**(-8)

#Iron resistivity 
IRON_RESISTIVITY = 1.3*10**(-7)

#Steel resistivity
STEEL_RESISTIVITY = 1.8*10**(-7)

#Proportionality constant in [Newton/(Amprere**2)]
PROPORTION_CONST = 2.7*10**(-7)

#Weber in [Maxwell]
WEBER = 10**8

#Tesla in [Gauss]
TESLA = 10**6

#Atomic Mass Unit in kilograms
ATOM_MASSUNIT = 1.66043*10**(-27)

#Air Density in [kilograms/(meters**3)]
AIR_DENSITY = 1.29

#Water Density in [kilograms/(meters**3)]
WATER_DENSITY = 10**3

#Atmosphere in Pascal
ATM = 1.013*10**5

#Angstrom in meters
ANGSTROM = 10**(-19)

#Water viscosity at 0 Celsius deg, in [pascal*seconds]
WATER_VISCOSITY_DEG_0 = 1.8*10**(-3)

#Water viscosity at 20 Celsius deg, in [pascal*seconds]
WATER_VISCOSITY_DEG_20 = 10**(-3)

#Copper conducibility in [Watt/(meters*Kelvin)]
COPPER_CONDUCIBILITY = 384

#Gold conducibility in [Watt/(meters*Kelvin)]
GOLD_CONDUCIBILITY = 300

#Iron conducibility in [Watt/(meters*Kelvin)]
IRON_CONDUCIBILITY = 70

#Dry Air conducibility in [Watt/(meters*Kelvin)]
AIR_CONDUCIBILITY = 0.02

#Carbon Emissivity
CARBON_EMISSIVITY = 0.92

#Iron Emissivity
IRON_EMISSIVITY = 0.40

#Copper Emissivity
COPPER_EMISSIVITY = 0.30

#Silver Emissivity
SILVER_EMISSIVITY = 0.05

#Force formula
def force(mass,acceleration):
    print(mass*acceleration)

#Distance formula
def distance(speed,time):
    print(speed*time)

#Speed formula
def speed(distance,time):
    print(distance/time)

#Time formula
def time(distance,speed):
    print(distance/speed)

#Work formula
def work(force,distance):
    print(force*distance)

#Acceleration formula
def acceleration(force,mass):
    print(force/mass)

#Density formula
def density(weight,volume):
    print(weight/volume)

#Intensity formula
def intensity(power,area):
    print(power/area)

#Potential Energy formula
def potential_Ener(mass,acceleration,height):
    print(mass*acceleration*height)

#Kinetic Energy formula
def kinetic_Ener(mass,speed):
    print((1/2)*mass*(speed**2))

#Mechanic Energy formula
def mechanical_Ener(potential,kinetic):
    print(potential+kinetic)

#Momentum formula
def momentum(mass,speed):
    print(mass*speed)

#Power formula
def power(work,time):
    print(work/time)

#Potential Gravitational Energy
def potent_GravEner(mass,height):
    print(mass*GRAVITY*height)

#Potential Elastic Energy
def potent_ElasticEner(elasticConstant,distance):
    print((1/2)*elasticConstant*(distance**2))

#Poiseuille law 
def law_Poiseuille(tubeRadius,pressureVariation,fluidViscosity,tubeLength):
    print((3.1416*(radius**4)*pressureVariation)/(8*fluidViscosity*tubeLength))

#Stokes law 
def law_Stokes(fluidViscosity,radius,speed):
    print((-6)*3.1416*fluidViscosity*radius*speed)

#Universal Gravitational Law (Gravitational Attraction Law)
def grav_attract(mass1,mass2,distance):
    print((G*mass1*mass2)/(distance**2))

#Gravitational Field from a point-like material
def grav_Field(mass,distance):
    print((G*mass)/(distance**2))

#Potential Gravitatonal Energy of an isolated system composed by two point-like materials, each with specific mass, at a specific distance separating them
def potent_GravEner2(mass1,mass2,distance):
    print(((-G)*mass1*mass2)/(radius))

#Escape Speed
def escape_speed(mass,radius):
    print(((G*mass)/(radius))*(0.5))

#Gay-Lussac first law  (Volume variation)
def law_Lussac1(volume,celsiusDeg_Temperature):
    print(volume*(1+(1/273)*(celsiusDeg_Temperature)))

#Gay-Lussac second law (Pressure Variation)
def law_Lussac2(pressure,celsiusDeg_Temperature):
    print(pressure*(1+(1/273)*(celsiusDeg_Temperaure)))

#Fourier Law (of conduction)
def law_Fourier(termicConducibility,area,kelvinDeg_HeatVariation,time,width):
    print((termicConducibility*area*kelvinDeg_HeatVariation*time)/(width))

#Irradied Heat 
def irradiedHeat(emissivity,area,kelvinDeg_CorpTemperature,kelvinEnviromentTemperature,time):
    print(emissivity*STEFBOLTZ*area*(kelvinDeg_CorpTemperature-kelvinEnviromentTemperature)*time)

#Doppler effect (when listener get closer to the sound source) 
def doppler_A(speed,frequence):
    print((1+(speed/340))*frequence)

#Doppler effect (when listener get far away from sound source)
def doppler_B(speed,frequence):
    print((1-(speed/340))*frequence)

#Coulomb law formula
def law_Coulomb(charge1,charge2,distance):
    print(coulomb*(((charge1*charge2)**2)**(0.5))/(distance**2))

#Gauss theorem, Flux of electric field
def gauss_Flux(charge):
    print(charge/DIELECTRIC)

#Electric Potential Energy on electric Field formula from a point-like charge
def electPotent_Ener(charge1,charge2,distance):
    print((charge1*charge2)/(4*3.1416*DIELECTRIC*distance))

#Electric Potential Difference between two point from the charge position
def electPotent_Diff(charge,distance1,distance2):
    print((charge/(4*3.1416*DIELECTRIC))*((1/distance1)-(1/distance2)))

#Capacity of a conducer
def capacity(charge,potential):
    print(charge/potential)

#Density of energy of Electric Field
def energy_Dens(electricFieldModule):
    print((1/2)*DIELECTRIC*(electricFieldmodule**2))

#First Ohm law
def law_Ohm1(resistance,currentIntensity):
    print(resistance*currentIntensity)

#Second Ohm law
def law_Ohm2(resistivity,length,area):
    print(resistivity*lenght/area)

#Joule law
def law_Joule(resistance,currentIntensity):
    print(resistance*(currentIntensity**2))

#Magnetic Induction module
def magnetic_induct(magneticForce,currentIntensity,length):
    print(magneticForce/(currentIntensity*length))

#Ampere law
def law_Ampere(currentInt1,currentInt2,length,distance):
    print((PROPORTION_CONST*currentInt1*currentInt2*length)/distance)

#Energetic Density Mean 
def energ_DensM(wavingElectricFieldWidth):
    print((1/2)*DIELECTRIC*(wavingElectricFieldWidth**2))

#Relativistic time (Expansion of times)
def relativ_Time(travelerTime,speed):
    print(travelerTime/((1-((speed**2)/(LIGHT**2)))**(0.5)))

#Lorentz factor
def lorentz_factor(speed):
    print(1/((1-((speed**2)/(LIGHT**2)))**(0.5)))

#Relativistic distance (Compression of distances)
def relativ_Dist(nonTravelerDistance,speed):
    print(((1-(speed**2/LIGHT**2))**(0.5))*nonTravelerDistance)

#Relativistic Mass (Increment of Mass)
def relativ_Mass(travelerMass,speed):
    print(travelerMass/((1-((speed**2)/(LIGHT**2)))**(0.5)))

#Relativistic Momentum (Increment of Momentum)
def relativ_Momen(travelerMomentum,speed):
    print((travelerMomentum*speed)/((1-((speed**2)/(LIGHT**2)))**(0.5)))

#Relative Energy
def relativ_Energ(travelerEnergy,speed):
    print((travelerEnergy*(LIGHT**2))/((1-((speed**2)/(LIGHT**2)))**(0.5)))

#Quantic energy
def quantic_En(frequence):
    print(PLANCK*frequence)

#Created by me, Gabriele Gatti, hope you like it
if __name__ == '__main__':
    main()