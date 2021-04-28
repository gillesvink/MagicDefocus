# MagicTools
toolbar = nuke.menu('Nodes')
MagicMenu = toolbar.addMenu('MagicTools', icon='MagicTools.png')
MagicMenu.addCommand('MagicDefocus', 'nuke.createNode("MagicDefocus")')
