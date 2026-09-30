"""
Module de base robuste et typé (Python 3.10+).
"""
import sys


def process_items(items: list[str], config: dict | None = None) -> int:
    """
    Traite une séquence de chaînes de caractères.

    Args:
        items: Liste des éléments à traiter.
        config: Dictionnaire de configuration optionnel.

    Returns:
        Code de sortie (0 pour succès, >0 pour erreur).
    """
    if not items:
        print("Erreur : La liste d'éléments est vide.", file=sys.stderr)
        return 1

    for item in items:
        print(f"Traitement de {item}")

    return 0


if __name__ == "__main__":
    sys.exit(process_items(sys.argv[1:]))
