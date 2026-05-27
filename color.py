# Color

reset = "\033[0m"

# Colores
colores = {
    # Colores primarios y derivados
    "rojo": "\033[38;5;196m",
    "rojo_oscuro": "\033[38;5;88m",
    
    "verde": "\033[38;5;46m",
    "verde_claro": "\033[38;5;120m",
    "verde_oscuro": "\033[38;5;22m",
    "lima": "\033[38;5;118m",
    "verde_neón": "\033[38;5;82m",
    
    "azul": "\033[38;5;21m",
    "azul_claro": "\033[38;5;75m",
    "azul_neón": "\033[38;5;27m",
    "marino": "\033[38;5;19m",
    
    # Colores cálidos
    "amarillo": "\033[38;5;226m",
    "naranja": "\033[38;5;208m",
    "naranja_claro": "\033[38;5;215m",
    "dorado": "\033[38;5;220m",
    "salmon": "\033[38;5;209m",
    "carne": "\033[38;5;217m",
    "chocolate": "\033[38;5;94m",
    
    # Rosas y violetas
    "rosado": "\033[38;5;213m",
    "lavanda": "\033[38;5;183m",
    "fucsia": "\033[38;5;201m",
    "rosa_neón": "\033[38;5;198m",
    "violeta": "\033[38;5;129m",
    "morado": "\033[38;5;93m",
    "vino": "\033[38;5;88m",
    
    # Azules especiales y afines
    "celeste": "\033[38;5;51m",
    "cian": "\033[38;5;14m",
    "aguamarina": "\033[38;5;79m",
    "turquesa": "\033[38;5;44m",
    
    # Neutros
    "gris": "\033[38;5;250m",
    "gris_oscuro": "\033[38;5;240m",
    "plata": "\033[38;5;7m"
}

# Función pintar
def pintar(texto, color):
    from color import colores, reset
    
    if color in colores:
        print(f"{colores[color]}{texto}{reset}")
    else:
        print(f"{colores['rojo']}Color '{color}' no encontrado.{reset}")