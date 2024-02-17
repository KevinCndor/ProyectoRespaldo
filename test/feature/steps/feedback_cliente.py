from behave import *

use_step_matcher("re")


@step("que el Cliente a realizado el pago y el proceso de envío de la compra ha finalizado")
def step_impl(context):

    return True


@step(
    "el Cliente envíe una Calificación menor o igual a cinco estrellas del Producto y del Servicio, y mencione los motivos de su Calificación.")
def step_impl(context):

    return True


@step("la valoración total de calificaciones del (?P<item_de_calificacion>.+) aumentarán")
def step_impl(context, item_de_calificacion):

    return True


@step(
    "el vendedor podrá visualizar que el (?P<porcentaje>.+) de calificaciones de (?P<cantidad>.+) estrellas son por las (?P<causas>.+) correspondientes al (?P<item_de_calificacion>.+).")
def step_impl(context, porcentaje, cantidad, causas, item_de_calificacion):

    return True