# -*- coding: utf-8 -*-

import arcpy
from typing import List
import os
import json
import setbackPerEdge
from importlib import reload


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        param0 = arcpy.Parameter(
            displayName="Input Path",
            name="in_features",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        param0.value = "\\\\wsl.localhost/Ubuntu/home/cookiedan42/shiphats/setback-per-edge/data/sample-data1.json"
        # param0.value = "\\\\wsl.localhost/Ubuntu/home/cookiedan42/shiphats/setback-per-edge/data/sample-data2.json"

        return [param0]

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

    def execute(self, parameters: List[arcpy.Parameter], messages):
        """The source code of the tool."""

        reload(setbackPerEdge)
        dataPath = parameters[0].valueAsText

        assert os.path.exists(dataPath), "invalid path provided"
        if not setbackPerEdge.prt.is_prt_initialized():
            setbackPerEdge.prt.initialize_prt()
        arcpy.AddMessage("is initialized")
        assert setbackPerEdge.prt.is_prt_initialized(), "prt not initialized"
        arcpy.AddMessage("pre")
        with open(dataPath, "r") as fp:
            data = {"geometry": json.load(fp), "rpkName": "SetbackPerEdge"}
            res = setbackPerEdge.main(data)

        # prt.shutdown_prt()
        # never shutdown PRT?
        # running multiple tools is treated as same instance by the tool :(

        for i in res:
            arcpy.AddMessage(i)
        arcpy.AddMessage(res)
        arcpy.AddMessage("post")
        return res

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
