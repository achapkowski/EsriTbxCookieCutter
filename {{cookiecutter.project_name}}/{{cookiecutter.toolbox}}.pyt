"""
@author: {{cookiecutter.author}}
@contact: {{cookiecutter.email}}
@version: {{cookiecutter.release}}
@description: {{cookiecutter.short_description}}
@requirements:
@copyright: {{cookiecutter.copyright}}, {{cookiecutter.year}}
"""
import os
import sys
import traceback

import arcpy
from arcpy import env
from arcpy import da
if sys.version_info.major == 3:
    from arcpy import mp as mapping
else:
    from arcpy import mapping

env.overwriteOutput = True

#--------------------------------------------------------------------------
class FunctionError(Exception):
    """ raised when a function fails to run """
    pass

#--------------------------------------------------------------------------
def trace():
    """
        trace finds the line, the filename
        and error message and returns it
        to the user
    """
    import traceback
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    # script name + line number
    line = tbinfo.split(", ")[1]
    # Get Python syntax error
    #
    synerror = traceback.format_exc().splitlines()[-1]
    return line, __file__, synerror


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "{{cookiecutter.toolbox}}"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [{{cookiecutter.tool}}]


class {{cookiecutter.tool}}(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "{{cookiecutter.tool}}"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        try:
            return
        except arcpy.ExecuteError:
            line, filename, synerror = trace()
            arcpy.AddError("error on line: %s" % line)
            arcpy.AddError("error in file name: %s" % filename)
            arcpy.AddError("with error message: %s" % synerror)
            arcpy.AddError("ArcPy Error Message: %s" % arcpy.GetMessages(2))
        except FunctionError as f_e:
            messages = f_e.args[0]
            arcpy.AddError("error in function: %s" % messages["function"])
            arcpy.AddError("error on line: %s" % messages["line"])
            arcpy.AddError("error in file name: %s" % messages["filename"])
            arcpy.AddError("with error message: %s" % messages["synerror"])
            arcpy.AddError("ArcPy Error Message: %s" % messages["arc"])
        except:
            line, filename, synerror = trace()
            arcpy.AddError("error on line: %s" % line)
            arcpy.AddError("error in file name: %s" % filename)
            arcpy.AddError("with error message: %s" % synerror)
        return
