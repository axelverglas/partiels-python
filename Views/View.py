import re
import datetime


class View:

    def is_valid_date(self, date_str):
        """
        Vérifie si la chaîne de caractères est une date valide au format JJ/MM/AAAA.

        Args:
            date_str (str): La chaîne de caractères représentant la date.

        Returns:
            bool: True si la date est valide, sinon False.
        """
        try:
            datetime.datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def is_valid_alpha(self, input_string):
        """
        Vérifie si la chaîne contient uniquement des caractères alphabétiques
        (et des espaces).

        Args:
            input_string (str): Chaîne à vérifier.

        Returns:
            bool: True si valide, sinon False.
        """
        return re.fullmatch(r'[A-Za-zÀ-ÖØ-öø-ÿ\s]{2,}', input_string) is not None

    def get_valid_date_input(self, prompt):
        """
        Demande une date au format JJ/MM/AAAA jusqu'à obtenir une entrée valide.

        Args:
            prompt (str): Invite pour l'utilisateur.

        Returns:
            str: Date valide.
        """
        while True:
            date = input(prompt)
            if self.is_valid_date(date):
                return date
            else:
                print("Date invalide. Réessayez.")

    def get_valid_alpha_input(self, prompt):
        """
        Demande une chaîne alphabétique jusqu'à obtenir une entrée valide.

        Args:
            prompt (str): Invite pour l'utilisateur.

        Returns:
            str: Chaîne alphabétique valide.
        """
        while True:
            input_string = input(prompt)
            if self.is_valid_alpha(input_string):
                return input_string
            else:
                print("Entrée invalide. Réessayez avec au moins deux caractères alphabétiques.")

    def get_valid_int_input(self, prompt, default_value=None):
        """
        Demande un entier jusqu'à obtenir une entrée valide. Utilise la valeur par défaut
        si l'utilisateur n'entre rien et qu'une valeur par défaut est fournie.

        Args:
            prompt (str): Invite pour l'utilisateur.
            default_value (int, optional): Valeur par défaut si rien n'est entré.

        Returns:
            int: Entier valide ou valeur par défaut.
        """
        while True:
            input_string = input(prompt)
            if input_string == "" and default_value is not None:
                return default_value
            elif input_string.isdigit():
                return int(input_string)
            else:
                print("Entrée invalide, veuillez entrer un caractère numérique.")
