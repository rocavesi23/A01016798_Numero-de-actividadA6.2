"""
Este módulo contiene pruebas unitarias para la clase Hotel.
"""
import unittest
import os
from hotel import Hotel


class TestHotel(unittest.TestCase):
    """
    Pruebas unitarias para la clase Hotel.
    """

    def setUp(self):
        """
        Prepara el contexto necesario para las pruebas.
        """
        self.hotel = Hotel("California", "123 Main St", "1234567890")

    def test_create_hotel(self):
        """
        Verifica que se pueda crear un hotel correctamente.
        """
        print("\nPrueba de creación de hotel: Verificando que se pueda "
              "crear un hotel correctamente.")

        self.assertIsInstance(self.hotel, Hotel)
        self.assertEqual(self.hotel.name, "California")
        self.assertEqual(self.hotel.location, "123 Main St")
        self.assertEqual(self.hotel.phone, "1234567890")

        self.hotel.create_hotel()
        self.assertTrue(os.path.exists(f"{self.hotel.name}_hotel.json"),
                        f"El hotel {self.hotel.name} no se pudo crear.")

    def test_delete_hotel(self):
        """
        Verifica que se pueda eliminar un hotel correctamente.
        """
        print("Prueba de eliminar un hotel: Verificando que se "
              "pueda eliminar un hotel correctamente.")
        self.hotel.delete_hotel()

    def test_display_hotel_info(self):
        """
        Verifica que se pueda visualizar la información del hotel
        correctamente.
        """
        print("Prueba de mostrar información: Verificando que se pueda "
              "consultar la información del hotel correctamente.")
        self.hotel.display_hotel_info()

    def test_modify_info(self):
        """
        Verificar que se pueda modificar la información del hotel
        correctamente.
        """
        print("Prueba de modificar información: Verificando que se pueda "
              "modificar la información del hotel correctamente.")
        new_name = "Marriot"
        new_address = "250 Reforma St"
        new_phone_number = "0987654321"
        self.hotel.modify_hotel_info(name=new_name, location=new_address,
                                     phone=new_phone_number)
        self.assertEqual(self.hotel.name, new_name)
        self.assertEqual(self.hotel.location, new_address)
        self.assertEqual(self.hotel.phone, new_phone_number)

    def test_reserve_room(self):
        """
        Verificar que se pueda reservar una habitación correctamente.
        """
        print("Prueba de reservar una habitación: Verificando que se pueda "
              "reservar una habitación correctamente.")
        # Positive scenario
        room_number = "101"
        guest_name = "Roberto Avelar"
        check_in_date = "2024-02-15"
        check_out_date = "2024-02-20"
        self.hotel.reserve_room(room_number, guest_name,
                                check_in_date, check_out_date)

        # Negative scenario: Attempting to reserve an already reserved room
        print("Prueba de reservar una habitación: Verificando que NO se "
              "pueda reservar una habitación ya reservada.")
        self.assertFalse(self.hotel.reserve_room(room_number, "Jane Doe",
                                                 "2024-02-16", "2024-02-18"))

        # Negative scenario: Attempting to reserve a room with invalid dates
        print("Prueba de reservar una habitación: Verificando que NO se "
              "pueda reservar una habitación con fechas inválidas.")
        self.assertFalse(self.hotel.reserve_room("102", "Jane Doe",
                                                 "2024-02-20", "2024-02-15"))

    def test_cancel_reservation(self):
        """
        Verificar que se pueda cancelar una reserva correctamente.
        """
        print("Prueba de cancelar una reservación: Verificando que se "
              "pueda cancelar una reservación correctamente.")
        # Positive scenario
        room_number = "103"
        guest_name = "Carlos Sigüenza"
        check_in_date = "2024-02-15"
        check_out_date = "2024-02-20"
        self.hotel.reserve_room(room_number, guest_name,
                                check_in_date, check_out_date)

        room_number = "103"
        self.assertTrue(self.hotel.cancel_reservation(room_number))

        # Negative scenario: Attempting to cancel a reservation for
        # a non-existent room
        print("Prueba de cancelar una reservación: Verificando que NO se "
              "pueda cancelar una reservación para una habitación no "
              "existente.")
        self.assertFalse(self.hotel.cancel_reservation("102"))

    def tearDown(self):
        """
        Limpiar después de las pruebas.
        """
        filename = f"{self.hotel.name}_hotel.json"
        # Clean up any files created during tests
        if os.path.exists(filename):
            pass
        # Dejamos comentada esta linea porque el borrado del archivo
        # lo hace el método delete_hotel
        # os.remove("EdBaldwin_customer.json")


if __name__ == "__main__":

    # Crear una instancia de TestSuite
    suite = unittest.TestSuite()

    # Agregar los métodos de prueba a la suite en el orden deseado
    suite.addTest(TestHotel('test_create_hotel'))
    suite.addTest(TestHotel('test_display_hotel_info'))
    suite.addTest(TestHotel('test_modify_info'))
    suite.addTest(TestHotel('test_reserve_room'))
    suite.addTest(TestHotel('test_cancel_reservation'))
    suite.addTest(TestHotel('test_delete_hotel'))

    # Crear un TextTestRunner personalizado
    runner = unittest.TextTestRunner()

    # Ejecutar las pruebas
    runner.run(suite)
