from typing import TypeVar, List

InitialShape = TypeVar(
    "InitialShape"
)  # https://raw.githubusercontent.com/Esri/pyprt/main/src/client/InitialShape.h

ModelGenerator = TypeVar(
    "ModelGenerator"
)  # https://raw.githubusercontent.com/Esri/pyprt/main/src/client/ModelGenerator.h


class GeneratedModel:
    """
    https://raw.githubusercontent.com/Esri/pyprt/main/src/client/GeneratedModel.h
    """

    def get_attributes(self) -> dict:
        """
        Returns a dictionary with the CGA rule attributes name and value used to generate this model.
        """
        return {}

    def get_cga_errors(self) -> List[str]:
        """
        Returns a list of the CGA and asset errors messages of this model. The asset error messages additionally contain the key and URI of the asset.
        """
        return []

    def get_cga_prints(self) -> str:
        """
        Returns a string with all the CGA print outputs of this model.
        """
        return ""

    def get_faces(self) -> List[int]:
        """
        Returns the vertex indices count per face of the generated 3D geometry. If the 'emitGeometry' entry of the encoder options dictionary has been set to False, this function returns an empty vector.
        """
        return []

    def get_indices(self) -> List[int]:
        """
        Returns the vertex indices of the generated 3D geometry, for all faces. If the 'emitGeometry' entry of the encoder options dictionary has been set to False, this function returns an empty vector.
        """
        return []

    def get_initial_shape_index(self) -> int:
        """
        Returns the index of the initial shape on which the generated geometry has been built. The ModelGenerator class is instantiated by specifying a list of InitialShape instances. This index indicates the corresponding InitialShape instance of that list.
        """
        return 0

    def get_report(self) -> dict:
        """
        Returns the CGA report of the generated 3D geometry. This report dictionary is empty if the CGA rule file employed does not output any report or if the 'emitReport' entry of the encoder options dictionary has been set to False.
        """
        return {}

    def get_vertices(self) -> List[float]:
        """
        Returns the generated 3D geometry vertex coordinates as a series of (x, y, z) triplets. Its size is 3 x the number of vertices. If the 'emitGeometry' entry of the encoder options dictionary has been set to False, this function returns an empty vector.
        """
        return []
