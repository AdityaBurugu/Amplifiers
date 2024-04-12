from Other_Func import format_value
def CE_Amplifier(VCC,Vce,Ic,B,Av):
    Ic=eval(Ic)
    re = (26*10**-3)/(Ic)
    Rc = round(Av*re,2)

    Re = (VCC-Ic*Rc-Vce)/(Ic)

    Vdrop_across_Re = Ic*Re
    VBE = 0.7       #fixed
    Base_Voltage = (Vdrop_across_Re+VBE)


    ratio = ((VCC-Base_Voltage)/Base_Voltage)

    R2_max = B/10*Re

    R2 = eval(input(f'''Select R2 Value less than {format_value(R2_max)}Ω:'''))
    if R2>0 and R2<=round(R2_max):
        R1 = ratio*R2

        Rc = format_value(Rc)
        Re = format_value(Re)
        R1 = format_value(R1)
        R2 = format_value(R2)

        return Rc,Re,R1,R2
    else:
        return None,None,None,None