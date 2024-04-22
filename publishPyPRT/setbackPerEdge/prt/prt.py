from .types import GeneratedModel, InitialShape, ModelGenerator
from typing import Iterable, TypeVar, List
import pyprt.pyprt as pyprt


def initialize_prt():
    """
    Initialization of PRT. PyPRT functionalities are blocked until the initialization is done.
    """
    pyprt.initialize_prt()


def is_prt_initialized() -> bool:
    """
    This function returns True if PRT is initialized, False otherwise.
    """
    return pyprt.is_prt_initialized()


def shutdown_prt():
    """
    Shutdown of PRT. The PRT initialization process can be done only once per session/script. Thus, `initialize_prt()` cannot be called after shutdown_prt().
    """
    pyprt.shutdown_prt()


def prtShapeFromArr(coordArr: Iterable[float]) -> InitialShape:  # type: ignore
    """
    Constructs an InitialShape with one polygon by accepting a list of direct vertex coordinates.
    The vertex order is expected to be counter-clockwise.
    """
    return pyprt.InitialShape(coordArr)


def makeModelGenerator(shp: Iterable) -> ModelGenerator:
    return pyprt.ModelGenerator(shp)
