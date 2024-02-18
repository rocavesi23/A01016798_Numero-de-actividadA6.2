"""
Este módulo contiene pruebas unitarias para la clase Customer.
"""
import unittest
import os
import json
# Importación relativa hacia arriba y dentro de la carpeta reservations
from customer import Customer


class TestCustomer(unittest.TestCase):
    """
    Pruebas unitarias para la clase Customer.
    """
    def setUp(self):
        """
        Prepara el contexto necesario para las pruebas.
        """
        self.customer = Customer("EdBaldwin", "ed.baldwin@nasa.gov.us",
                                 "1234567890", "Happy Valley 123")

    def test_create_customer(self):
        """
        Verifica que se pueda crear un cliente correctamente.
        """
        print("\nPrueba de creación de customer: Verificando que"
              "se pueda crear un customer correctamente.")
        self.customer.create_customer()
        self.assertTrue(os.path.exists("EdBaldwin_customer.json"),
                        f"EL cliente {self.customer.name} no se pudo crear")

    def test_display_customer_info(self):
        """
        Verifica que se pueda visualizar la información de un cliente
        correctamente.
        """
        print("Prueba de mostrar información de customer: Verificando "
              "que se pueda mostrar la info de un customer correctamente.")
        self.customer.display_info()

    def test_modify_info(self):
        """
        Verificar que se pueda modificar la información de un cliente
        correctamente
        """
        print("Prueba de modificar la información de customer: Verificando "
              "que se pueda modificar la info de un customer correctamente.")
        new_name = "GordoStevens"
        new_email = "gordo_stevens@example.com"
        new_mobile_phone = "0987654321"
        new_address = "456 Calle Nueva"
        self.customer.modify_info(name=new_name, email=new_email,
                                  mobile_phone=new_mobile_phone,
                                  address=new_address)

        if os.path.exists("EdBaldwin_customer.json"):
            with open("EdBaldwin_customer.json", 'r',
                      encoding='utf-8') as file:
                customer_data = json.load(file)
                self.assertEqual(customer_data['name'], new_name,
                                 "test_modify_info: name not updated.")
                self.assertEqual(customer_data['email'], new_email,
                                 "test_modify_info: email not updated.")
                self.assertEqual(customer_data['mobile_phone'],
                                 new_mobile_phone,
                                 "test_modify_info: mobile_phone not updated.")
                self.assertEqual(customer_data['address'], new_address,
                                 "test_modify_info: address not updated.")
        else:
            print("file EdBaldwin_customer.json not found.")

    def test_delete_customer(self):
        """
        Verificar que se pueda eliminar un cliente correctamente
        """
        print("Prueba de eliminar la información de customer: Verificando "
              "que se pueda eliminar la info de un customer correctamente.")
        filename = f"{self.customer.name}_customer.json"
        self.customer.delete_customer()
        self.assertFalse(os.path.exists(filename),
                         f"EL archivo {filename} no fue eliminado.")

    def test_create_customer_with_invalid_data(self):
        """
        Verifica que no se pueda crear un cliente con datos inválidos.
        """
        print("Prueba de crear un customer: Verificando que NO se"
              " pueda crear un customer con datos inválidos.")
        invalid_customer = Customer("", "", "", "")
        with self.assertRaises(ValueError):
            invalid_customer.create_customer()

    def test_modify_info_with_invalid_data(self):
        """
        Verifica que no se pueda modificar la información de un cliente
        con datos inválidos.
        """
        print("Prueba de modificar un customer: Verificando que NO se"
              " pueda modificar un customer con datos inválidos.")
        with self.assertRaises(ValueError):
            self.customer.modify_info(name="", email="",
                                      mobile_phone="", address="")

    def test_delete_nonexistent_customer(self):
        """
        Verificar que no se pueda eliminar un cliente que no existe.
        """
        print("Prueba de eliminar un customer: Verificando que NO se"
              " pueda crear un customer que no existe.")
        nonexistent_customer = Customer("Nonexistent", "", "", "")
        with self.assertRaises(FileNotFoundError):
            nonexistent_customer.delete_customer()

    def test_display_nonexistent_customer_info(self):
        """
        Verificar que no se pueda visualizar la información de un
        cliente que no existe.
        """
        print("Prueba de mostrar un customer: Verificando que NO se"
              " pueda mostrar un customer que no existe.")
        nonexistent_customer = Customer("Nonexistent", "", "", "")
        with self.assertRaises(FileNotFoundError):
            nonexistent_customer.display_info()

    def test_modify_nonexistent_customer_info(self):
        """
        Verificar que no se pueda modificar la información de un
        cliente que no existe.
        """
        print("ejecutando test_modify_nonexistent_customer_info...")
        nonexistent_customer = Customer("Nonexistent", "", "", "")
        with self.assertRaises(FileNotFoundError):
            nonexistent_customer.modify_info(name="NewName",
                                             email="new@example.com",
                                             mobile_phone="1234567890",
                                             address="New Address")

    def tearDown(self):
        # Limpiar después de las pruebas
        if os.path.exists("EdBaldwin_customer.json"):
            pass
        # Dejamos comentada esta linea porque el borrado del archivo
        # lo hace el método delete_customer
        # os.remove("EdBaldwin_customer.json")


if __name__ == "__main__":
    # Crear una instancia de TestSuite
    suite = unittest.TestSuite()

    # Agregar los métodos de prueba a la suite en el orden deseado
    suite.addTest(TestCustomer('test_create_customer'))
    suite.addTest(TestCustomer('test_display_customer_info'))
    suite.addTest(TestCustomer('test_modify_info'))
    suite.addTest(TestCustomer('test_create_customer_with_invalid_data'))
    suite.addTest(TestCustomer('test_modify_info_with_invalid_data'))
    suite.addTest(TestCustomer('test_delete_nonexistent_customer'))
    suite.addTest(TestCustomer('test_display_nonexistent_customer_info'))
    suite.addTest(TestCustomer('test_delete_customer'))

    # Crear un TextTestRunner personalizado
    runner = unittest.TextTestRunner()

    # Ejecutar las pruebas
    runner.run(suite)
