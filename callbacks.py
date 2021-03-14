def knobChangedCallback():
    node = nuke.thisGroup()
    knob = nuke.thisKnob()
    knobValue = knob.value()
    knobs = node.knobs()

    if knob.name() == "method":
        depthKnobs = ["math", "center", "dof", "focal_point", "breathing"]
        for knobName in depthKnobs:
            knobs[knobName].setEnabled(knobValue != "2d")
    if knob.name() == "render":
        if knobValue == "focal plane setup":
            nuke.toNode("ZDefocus1")["output"].setValue("focal-plane setup")
        else:
            nuke.toNode("ZDefocus1").knob("output").setValue("result")
        nuke.toNode("bokeh_knobs").knob("preview_filter").setValue(False)

    elif knob.name() == "breathing":
        breathingKnobs = ["breathing_amount", "breathing_invert"]
        for knobName in breathingKnobs:
            knobs[knobName].setEnabled(knobValue != False)
        focusAnimated = knobs['center'].isAnimated()
        if not focusAnimated and knobValue != False:
            nuke.message("The focus plane is not animated. Make sure to animate this before using the breathing setting.")

    elif knob.name() == "gamma_correction":
        knobs["gamma_correction_amount"].setEnabled(knobValue != False)

    else:
        pass
knobChangedCallback()

def knobChangedCallback():
    node = nuke.thisGroup()
    knob = nuke.thisKnob()
    knobValue = knob.value()
    knobs = node.knobs()
    nonUniformKnobs = ["catseye", "barndoors", "softness", "overscan", "preserveedge", "quality_nonuniform", "farm", "softness", "overscan"]
    controlKnobs = {'catseye': ['catseye_amount'],
                    'barndoors': ["barndoors_width", "barndoors_height"],
                    'preserveedge': ["preserve_edge_amount"],}

    if knob.name() == "enable_non_uniform": #Non-uniform bokeh main knob
        if not knobValue: #Disable always when non-uniform disabled
            for key in controlKnobs.keys():
                nonUniformKnobs.extend(controlKnobs[key])

        else: #Keep disabled if disabled
            for controlName in controlKnobs.keys():
                if node.knob(controlName).getValue():
                    value_list = controlKnobs[controlName]
                    for knobName in controlKnobs[controlName]:
                        knobs[knobName].setEnabled(True)

        for knobName in nonUniformKnobs: #Enable all specified switches
            knobs[knobName].setEnabled(knobValue != False)

    elif knob.name() in controlKnobs.keys(): #Switch for all controlKnobs
        for knobName in controlKnobs[knob.name()]:
            knobs[knobName].setEnabled(knobValue != False)
    else:
        pass
knobChangedCallback()

def knobChangedCallback():
    node = nuke.thisGroup()
    knob = nuke.thisKnob()
    knobValue = knob.value()
    knobs = node.knobs()
    bokeh = ["ring_color", "inner_color", "ring_size", "outer_blur", "inner_blur", "chroma_spread", "noise_size", "noise_intensity", "noise_blur", "noise_seed"]
    bladed = ["corners", "angle", "edge_flattening"]

    if knob.name() == "filter_type":
        if knobValue == "disc":
            for knobName in bokeh:
                knobs[knobName].setEnabled(True)
            for knobName in bladed:
                knobs[knobName].setEnabled(False)

        else:
            knobValue = knobValue == "bladed"
            bokeh.extend(bladed)
            for knobName in bokeh:
                knobs[knobName].setEnabled(knobValue != False)

    else:
        pass
knobChangedCallback()
