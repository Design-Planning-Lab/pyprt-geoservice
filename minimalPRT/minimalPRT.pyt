# -*- coding: utf-8 -*-

try:
    import arcpy
except:

    class arcpy:
        """mock class to mimic addmessage method"""

        @classmethod
        def AddMessage(cls, message: str):
            print(message)


import pyprt
import os


PYTHON_ENCODER = "com.esri.pyprt.PyEncoder"

print(os.__file__)

RPK_PATH = "C:\\Users\\SEED110\\Documents\\geoService\\publishPyPRT\\setbackPerEdge\\rpk\\SetbackPerEdge.rpk"


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Minimal"
        self.alias = "minimal"

        # List of tool classes associated with this toolbox
        self.tools = [Minimal]


class Minimal:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Minimal"
        self.description = "minimalPRT"

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = None
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        import sys

        arcpy.AddMessage(sys.path)

        # if not pyprt.pyprt.is_prt_initialized():
        #     pyprt.pyprt.initialize_prt()

        if pyprt.pyprt.is_prt_initialized():
            arcpy.AddMessage("activated")
        else:
            arcpy.AddMessage("not activated")

        coordArr = (0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, -100.0)

        shp = pyprt.InitialShape(coordArr)


        assert os.path.exists(RPK_PATH)

        m2 = pyprt.ModelGenerator([shp])  # model containing one site
        attrs = [
            {"/edgeattr/setbacks": [5.0, 5.0, 5.0]}
        ]  # reverts to default when using int
        encoder_args = {"emitGeometry": True, "emitReport": False}
        result = m2.generate_model(attrs, RPK_PATH, PYTHON_ENCODER, encoder_args)
        arcpy.AddMessage(len(result))
        return result

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return


if __name__ == "__main__":
    
    Minimal().execute([], None)
