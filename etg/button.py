#---------------------------------------------------------------------------
# Name:        etg/button.py
# Author:      Kevin Ollivier
#
# Created:     27-Aug-2011
# Copyright:   (c) 2011 by Wide Open Technologies
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx"
MODULE    = "_core"
NAME      = "button"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  =    [
                'wxBitmapButton',
                'wxButton'
            ]
    
#---------------------------------------------------------------------------

def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)
    
    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.
    
    c = module.find('wxBitmapButton')
    c.find('wxBitmapButton.bitmap').default = 'wxNullBitmap'
    c.find('Create.bitmap').default = 'wxNullBitmap'
    tools.fixWindowClass(c)
    
    tools.removeVirtuals(c)
    tools.addWindowVirtuals(c)
    
    c = module.find('wxButton')
    tools.fixWindowClass(c)
    
    tools.removeVirtuals(c)
    tools.addWindowVirtuals(c)
    
    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.addGetterSetterProps(module)
    tools.runGenerators(module)
    
    
#---------------------------------------------------------------------------
if __name__ == '__main__':
    run()
