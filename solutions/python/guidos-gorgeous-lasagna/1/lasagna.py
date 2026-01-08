"""Functions used in preparing Guido's gorgeous lasagna.

    Learn about Guido, the creator of the Python language:
    https://en.wikipedia.org/wiki/Guido_van_Rossum

    This is a module docstring, used to describe the functionality
    of a module and its functions and/or classes.
"""

# TODO1: Define a constante 'EXPECTED_BAKE_TIME'.
EXPECTED_BAKE_TIME = 40  # tempo esperado de cozimento em minutos

# TODO2: Remova 'pass' e conclua a função 'bake_time_remaining()' abaixo.
def bake_time_remaining(actual_bake_time):
    """Calculate the bake time remaining.

    Args:
        actual_bake_time (int): Tempo decorrido no forno em minutos.

    Returns:
        int: Tempo restante de cozimento em minutos.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - actual_bake_time  

# TODO 3: Defina a função 'preparation_time_in_minutes()' abaixo.
# Você também pode considerar usar 'PREPARATION_TIME' aqui, se você tiver definido.
def preparation_time_in_minutes(number_of_layers):
    """Calculates the total time needed to prepare a specific number of lasagna layers.

    Args:
        number_of_layers (int): Número de camadas desejadas.

    Returns:
        int: Tempo total em minutos.
    """
    return number_of_layers * 2

# TODO 4: Define a função 'elapsed_time_in_minutes()' abaixo.
# Lembre-se de adicionar um docstring (você pode copiar e alterar o de bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculates the total baking time of the lasagna.

    Args:
        number_of_layers (int): Número de camadas adicionadas à lasanha.
        elapsed_bake_time (int): Tempo já decorrido no forno em minutos.

    Returns:
        int:  Tempo total de cozimento da lasanha em minutos.
    """
    # tempo em minutos para preparar cada camada
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time 
