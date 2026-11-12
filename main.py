from drafter import *
from dataclasses import dataclass
from bakery import assert_equal
from drafter import Header, bold

@dataclass
class Element:
    name: str
    symbol: str
    atomic_number: int
    atomic_mass: float
    common_charge: int



main_group_elements = [
    Element("Hydrogen", "H", 1, 1.008, 1),
    Element("Helium", "He", 2, 4.003, 0),
    Element("Lithium", "Li", 3, 6.94, 1),
    Element("Beryllium", "Be", 4, 9.012, 2),
    Element("Boron", "B", 5, 10.81, 3),
    Element("Carbon", "C", 6, 12.011, 4),
    Element("Nitrogen", "N", 7, 14.007, -3),
    Element("Oxygen", "O", 8, 15.999, -2),
    Element("Fluorine", "F", 9, 18.998, -1),
    Element("Neon", "Ne", 10, 20.180, 0),
    Element("Sodium", "Na", 11, 22.990, 1),
    Element("Magnesium", "Mg", 12, 24.305, 2),
    Element("Aluminum", "Al", 13, 26.982, 3),
    Element("Silicon", "Si", 14, 28.085, 4),
    Element("Phosphorus", "P", 15, 30.974, -3),
    Element("Sulfur", "S", 16, 32.06, -2),
    Element("Chlorine", "Cl", 17, 35.45, -1),
    Element("Argon", "Ar", 18, 39.948, 0),
    Element("Potassium", "K", 19, 39.098, 1),
    Element("Calcium", "Ca", 20, 40.078, 2),
    Element("Gallium", "Ga", 31, 69.723, 3),
    Element("Germanium", "Ge", 32, 72.630, 4),
    Element("Arsenic", "As", 33, 74.922, -3),
    Element("Selenium", "Se", 34, 78.971, -2),
    Element("Bromine", "Br", 35, 79.904, -1),
    Element("Krypton", "Kr", 36, 83.798, 0),
    Element("Rubidium", "Rb", 37, 85.468, 1),
    Element("Strontium", "Sr", 38, 87.62, 2),
    Element("Indium", "In", 49, 114.818, 3),
    Element("Tin", "Sn", 50, 118.710, 2),
    Element("Antimony", "Sb", 51, 121.760, 3),
    Element("Tellurium", "Te", 52, 127.60, -2),
    Element("Iodine", "I", 53, 126.904, -1),
    Element("Xenon", "Xe", 54, 131.293, 0),
    Element("Cesium", "Cs", 55, 132.905, 1),
    Element("Barium", "Ba", 56, 137.327, 2),
    Element("Thallium", "Tl", 81, 204.38, 1),
    Element("Lead", "Pb", 82, 207.2, 2),
    Element("Bismuth", "Bi", 83, 208.980, 3),
    Element("Polonium", "Po", 84, 209, 2),
    Element("Astatine", "At", 85, 210, -1),
    Element("Radon", "Rn", 86, 222, 0),
    Element("Francium", "Fr", 87, 223, 1),
    Element("Radium", "Ra", 88, 226, 2),
    Element("Nihonium", "Nh", 113, 286, 1),
    Element("Flerovium", "Fl", 114, 289, 2),
    Element("Moscovium", "Mc", 115, 290, 1),
    Element("Livermorium", "Lv", 116, 293, 2),
    Element("Tennessine", "Ts", 117, 294, -1),
    Element("Oganesson", "Og", 118, 294, 0)
]




transition_metals = [
    Element("Scandium", "Sc", 21, 44.956, 3),
    Element("Titanium", "Ti", 22, 47.867, 4),
    Element("Vanadium", "V", 23, 50.942, 5),
    Element("Chromium", "Cr", 24, 51.996, 3),
    Element("Manganese", "Mn", 25, 54.938, 2),
    Element("Iron", "Fe", 26, 55.845, 2),
    Element("Cobalt", "Co", 27, 58.933, 2),
    Element("Nickel", "Ni", 28, 58.693, 2),
    Element("Copper", "Cu", 29, 63.546, 2),
    Element("Zinc", "Zn", 30, 65.38, 2),
    Element("Yttrium", "Y", 39, 88.906, 3),
    Element("Zirconium", "Zr", 40, 91.224, 4),
    Element("Niobium", "Nb", 41, 92.906, 5),
    Element("Molybdenum", "Mo", 42, 95.95, 6),
    Element("Technetium", "Tc", 43, 98, 7),
    Element("Ruthenium", "Ru", 44, 101.07, 3),
    Element("Rhodium", "Rh", 45, 102.906, 3),
    Element("Palladium", "Pd", 46, 106.42, 2),
    Element("Silver", "Ag", 47, 107.868, 1),
    Element("Cadmium", "Cd", 48, 112.414, 2),
    Element("Hafnium", "Hf", 72, 178.49, 4),
    Element("Tantalum", "Ta", 73, 180.948, 5),
    Element("Tungsten", "W", 74, 183.84, 6),
    Element("Rhenium", "Re", 75, 186.207, 7),
    Element("Osmium", "Os", 76, 190.23, 4),
    Element("Iridium", "Ir", 77, 192.217, 3),
    Element("Platinum", "Pt", 78, 195.084, 2),
    Element("Gold", "Au", 79, 196.967, 3),
    Element("Mercury", "Hg", 80, 200.592, 2),
    Element("Rutherfordium", "Rf", 104, 267, 4),
    Element("Dubnium", "Db", 105, 268, 5),
    Element("Seaborgium", "Sg", 106, 269, 6),
    Element("Bohrium", "Bh", 107, 270, 7),
    Element("Hassium", "Hs", 108, 277, 8),
    Element("Meitnerium", "Mt", 109, 278, 0),
    Element("Darmstadtium", "Ds", 110, 281, 0),
    Element("Roentgenium", "Rg", 111, 282, 0),
    Element("Copernicium", "Cn", 112, 285, 2)
]




inner_transition_metals = [
    Element("Lanthanum", "La", 57, 138.905, 3),
    Element("Cerium", "Ce", 58, 140.116, 3),
    Element("Praseodymium", "Pr", 59, 140.908, 3),
    Element("Neodymium", "Nd", 60, 144.242, 3),
    Element("Promethium", "Pm", 61, 145, 3),
    Element("Samarium", "Sm", 62, 150.36, 3),
    Element("Europium", "Eu", 63, 151.964, 3),
    Element("Gadolinium", "Gd", 64, 157.25, 3),
    Element("Terbium", "Tb", 65, 158.925, 3),
    Element("Dysprosium", "Dy", 66, 162.500, 3),
    Element("Holmium", "Ho", 67, 164.930, 3),
    Element("Erbium", "Er", 68, 167.259, 3),
    Element("Thulium", "Tm", 69, 168.934, 3),
    Element("Ytterbium", "Yb", 70, 173.045, 3),
    Element("Lutetium", "Lu", 71, 174.967, 3),
    Element("Actinium", "Ac", 89, 227, 3),
    Element("Thorium", "Th", 90, 232.038, 4),
    Element("Protactinium", "Pa", 91, 231.036, 5),
    Element("Uranium", "U", 92, 238.029, 6),
    Element("Neptunium", "Np", 93, 237, 5),
    Element("Plutonium", "Pu", 94, 244, 4),
    Element("Americium", "Am", 95, 243, 3),
    Element("Curium", "Cm", 96, 247, 3),
    Element("Berkelium", "Bk", 97, 247, 3),
    Element("Californium", "Cf", 98, 251, 3),
    Element("Einsteinium", "Es", 99, 252, 3),
    Element("Fermium", "Fm", 100, 257, 3),
    Element("Mendelevium", "Md", 101, 258, 3),
    Element("Nobelium", "No", 102, 259, 2),
    Element("Lawrencium", "Lr", 103, 266, 3)
]



elements = (
    main_group_elements
    + transition_metals
    + inner_transition_metals
)



@dataclass
class PolyatomicIon:
    name: str
    formula: str
    charge: int


ions = [
    PolyatomicIon("Ammonium", "NH4", 1),
    PolyatomicIon("Acetate", "C2H3O2", -1),
    PolyatomicIon("Benzoate", "C7H5O2", -1),
    PolyatomicIon("Bicarbonate", "HCO3", -1),
    PolyatomicIon("Bisulfate", "HSO4", -1),
    PolyatomicIon("Bisulfite", "HSO3", -1),
    PolyatomicIon("Bromate", "BrO3", -1),
    PolyatomicIon("Chlorate", "ClO3", -1),
    PolyatomicIon("Chlorite", "ClO2", -1),
    PolyatomicIon("Cyanide", "CN", -1),
    PolyatomicIon("Formate", "CHO2", -1),
    PolyatomicIon("Hydroxide", "OH", -1),
    PolyatomicIon("Hypochlorite", "ClO", -1),
    PolyatomicIon("Iodate", "IO3", -1),
    PolyatomicIon("Nitrate", "NO3", -1),
    PolyatomicIon("Nitrite", "NO2", -1),
    PolyatomicIon("Perchlorate", "ClO4", -1),
    PolyatomicIon("Periodate", "IO4", -1),
    PolyatomicIon("Permanganate", "MnO4", -1),
    PolyatomicIon("Thiocyanate", "SCN", -1),
    PolyatomicIon("Carbonate", "CO3", -2),
    PolyatomicIon("Chromate", "CrO4", -2),
    PolyatomicIon("Dichromate", "Cr2O7", -2),
    PolyatomicIon("Oxalate", "C2O4", -2),
    PolyatomicIon("Peroxide", "O2", -2),
    PolyatomicIon("Selenate", "SeO4", -2),
    PolyatomicIon("Silicate", "SiO3", -2),
    PolyatomicIon("Sulfate", "SO4", -2),
    PolyatomicIon("Sulfite", "SO3", -2),
    PolyatomicIon("Thiosulfate", "S2O3", -2),
    PolyatomicIon("Biphosphate", "HPO4", -2),
    PolyatomicIon("Arsenate", "AsO4", -3),
    PolyatomicIon("Phosphate", "PO4", -3),
    PolyatomicIon("Borate", "BO4", -3)
]


@dataclass
class Calculation:
    formula: str
    calculation_type: str
    result: str


@dataclass
class State:
    main_group_elements: list[Element]
    transition_metals: list[Element]
    inner_transition_metals: list[Element]
    calculations: list[Calculation]
    current_formula: str
    current_result: str
    selected_calculation: str
# Combine all three element lists
elements = (
    main_group_elements
    + transition_metals
    + inner_transition_metals
)


# -------------------------
# HOME PAGE
# -------------------------

@route
def index():
    return Page([
        Header("ChemTools"),
        Text("Choose a Tool"),
        Button("Chemical Formula Calculator", "chemical_calculator"),
        Button("Periodic Table", "periodic_table"),
        Button("Polyatomic References", "ref_page")
    ])


# -------------------------
# CHEMICAL CALCULATOR
# -------------------------

@route
def chemical_calculator():
    return Page([
        Header("Molar Mass Calculator: COMING SOON"),
        Text("Enter a chemical formula to calculate its molar mass."),
        Button("Back Home", "index")
    ])


# -------------------------
# PERIODIC TABLE
# -------------------------

@route
def periodic_table():

    # Find elements using their atomic numbers
    element_lookup = {}

    for element in elements:
        element_lookup[element.atomic_number] = element

    PT_data = [
        Header("Interactive Periodic Table"),
        Text("Select an element to view its information.")
    ]

    # Create one clickable element tile
    def make_tile(number):
        if number == 0:
            return Div(
                "",
                style_width="70px",
                style_height="90px",
                style_margin="2px"
            )

        element = element_lookup[number]

        return Button(
            str(element.atomic_number)
            + "\n" + element.symbol
            + "\n" + element.name,

            "element_details",
            [Argument("symbol", element.symbol)],

            style_width="70px",
            style_height="85px",
            style_margin="2px",
            style_padding="3px",
            style_font_size="12px",
            style_white_space="pre-line",
            style_background_color="#dbeafe",
            style_color="#1e293b",
            style_border="2px solid #64748b",
            style_border_radius="8px"
        )

    # Atomic numbers in their correct periodic table positions
    periods = [
        [1] + [0] * 16 + [2],

        [3, 4] + [0] * 10 + [5, 6, 7, 8, 9, 10],

        [11, 12] + [0] * 10 + [13, 14, 15, 16, 17, 18],

        list(range(19, 37)),

        list(range(37, 55)),

        [55, 56, 0] + list(range(72, 87)),

        [87, 88, 0] + list(range(104, 119))
    ]

    # Display the seven periods
    for period in periods:
        tiles = []

        for number in period:
            tiles.append(make_tile(number))

        PT_data.append(
            Row(*tiles)
        )

    PT_data.append(Header("Lanthanides (57-71)"))

    lanthanide_tiles = []
    for number in range(57, 72):
        lanthanide_tiles.append(make_tile(number))

    PT_data.append(Row(*lanthanide_tiles))

    PT_data.append(Header("Actinides (89-103)"))

    actinide_tiles = []
    for number in range(89, 104):
        actinide_tiles.append(make_tile(number))

    PT_data.append(Row(*actinide_tiles))

    PT_data.append(Button("Back Home", "index"))

    return Page(PT_data)

# -------------------------
# ELEMENT DETAILS
# -------------------------

@route
def element_details(symbol: str):
    for element in elements:
        if element.symbol == symbol:
            return Page([
                Header(element.name),
                Text("Symbol: " + element.symbol),
                Text("Atomic Number: " + str(element.atomic_number)),
                Text("Atomic Mass: " + str(element.atomic_mass)),
                Text("Common Charge: " + str(element.common_charge)),
                Button("Back to Periodic Table", "periodic_table"),
                Button("Back Home", "index")
            ])

    return Page([
        Header("Element Not Found"),
        Text("We could not find that element."),
        Button("Back to Periodic Table", "periodic_table")
    ])


# -------------------------
# POLYATOMIC REFERENCE PAGE
# -------------------------

@route
def ref_page():

    ions_by_charge = {
        1: [],
        -1: [],
        -2: [],
        -3: []
    }

    # Organize ions by charge
    for ion in ions:
        ions_by_charge[ion.charge].append(ion)

    ion_data = [
        Header("Polyatomic Ion Reference"),
        Text("A quick reference guide to common polyatomic ions.")
    ]

    # Display each charge category
    for charge, charge_ions in ions_by_charge.items():

        if charge > 0:
            charge_label = "+" + str(charge)
        else:
            charge_label = str(charge)

        ion_data.append(
            Header("Charge: " + charge_label)
        )

        # Create rows for the table
        ion_rows = []

        for ion in charge_ions:
            ion_rows.append([
                ion.name,
                ion.formula,
                str(ion.charge)
            ])

        # Add organized table to page
        ion_data.append(
            Table(
                ion_rows,
                ["Ion Name", "Formula", "Charge"]
            )
        )

    ion_data.append(Button("Back Home", "index"))

    return Page(ion_data)

# -------------------------
# START WEBSITE
# -------------------------

start_server()

