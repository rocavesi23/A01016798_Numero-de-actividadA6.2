"""
Este módulo define la clase Customer para manejar las operaciones
relacionadas con los clientes como la creación, eliminación,
visualización y modificación de información del cliente.
"""
import json
import os


class Customer:
    """
    Clase que representa un cliente y maneja operaciones relacionadas con
    los clientes como la creación, eliminación, visualización y modificación
    de información del cliente.
    """
    def __init__(self, name, email, mobile_phone=None, address=None):
        """
        Constructor de la clase Customer.

        Args:
            name (str): Nombre del cliente.
            email (str): Correo electrónico del cliente.
            mobile_phone (str, opcional): Número de teléfono móvil del cliente.
            address (str, opcional): Dirección del cliente.
        """

        self.name = name
        self.email = email
        self.mobile_phone = mobile_phone
        self.address = address

    def create_customer(self):
        """
        Crea un archivo JSON con la información del cliente.
        """
        if not self.name or not self.email or not self.mobile_phone \
           or not self.address:
            raise ValueError("Todos los campos son obligatorios.")

        customer_data = {
            'name': self.name,
            'email': self.email,
            'mobile_phone': self.mobile_phone,
            'address': self.address
        }
        with open(f"{self.name}_customer.json", 'w', encoding='utf-8') as file:
            json.dump(customer_data, file)

    def delete_customer(self):
        """
        Elimina el archivo JSON del cliente.
        """
        filename = f"{self.name}_customer.json"

        if os.path.exists(filename):
            os.remove(f"{self.name}_customer.json")
        else:
            raise FileNotFoundError(f"{filename} not found.")

    def display_info(self):
        """
        Muestra la información del cliente almacenada en el archivo JSON.
        """
        filename = f"{self.name}_customer.json"
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                customer_data = json.load(file)
                print("\tCustomer Information:")
                print(f"\t\tName: {customer_data['name']}")
                print(f"\t\tEmail: {customer_data['email']}")
                print(f"\t\tMobile Phone: {customer_data['mobile_phone']}")
                print(f"\t\tAddress: {customer_data['address']}")
        else:
            raise FileNotFoundError(f"{filename} not found.")

    def modify_info(self, name=None, email=None, mobile_phone=None,
                    address=None):
        """
        Modifica la información del cliente en el archivo JSON.

        Args:
            name (str, opcional): Nuevo nombre del cliente.
            email (str, opcional): Nuevo correo electrónico del cliente.
            mobile_phone (str, opcional): Nuevo número de teléfono móvil
            del cliente.
            address (str, opcional): Nueva dirección del cliente.
        """
        if not name or not email or not mobile_phone or not address:
            raise ValueError("Todos los campos son obligatorios.")

        filename = f"{self.name}_customer.json"
        if os.path.exists(filename):
            with open(filename, 'r+', encoding='utf-8') as file:
                customer_data = json.load(file)
                if name:
                    customer_data['name'] = name
                if email:
                    customer_data['email'] = email
                if mobile_phone:
                    customer_data['mobile_phone'] = mobile_phone
                if address:
                    customer_data['address'] = address
                file.seek(0)
                json.dump(customer_data, file)
                file.truncate()
        else:
            print(f"Customer {self.name}_customer.json not found.")
